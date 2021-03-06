
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags

from .files_handle import ThumbnailImageField


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class TagModel(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PostModel(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField()

    image = ThumbnailImageField(upload_to='./article/')

    time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)

    tags = models.ManyToManyField(TagModel, blank=True)

    views = models.IntegerField(default=0)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title

    def get_time(self):
        return self.time.strftime("%b")

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
