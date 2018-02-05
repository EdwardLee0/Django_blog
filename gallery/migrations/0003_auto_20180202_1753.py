# Generated by Django 2.0 on 2018-02-02 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_gallerymodel_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='item',
            new_name='gallery',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='title',
        ),
    ]
