# Generated by Django 2.0 on 2018-01-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180129_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]