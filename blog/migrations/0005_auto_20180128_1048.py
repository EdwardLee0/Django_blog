# Generated by Django 2.0 on 2018-01-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180128_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='tag',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.TagModel'),
        ),
    ]