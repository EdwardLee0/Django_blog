# Generated by Django 2.0 on 2018-01-27 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postmodel_tag'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentModel',
        ),
    ]
