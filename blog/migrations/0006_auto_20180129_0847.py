# Generated by Django 2.0 on 2018-01-29 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180128_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='picture',
            field=models.ImageField(upload_to='./upload/'),
        ),
    ]
