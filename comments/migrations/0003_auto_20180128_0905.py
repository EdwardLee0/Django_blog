# Generated by Django 2.0 on 2018-01-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180127_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
