# Generated by Django 2.2.4 on 2020-08-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200820_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, height_field='height', null=True, upload_to='media/images', width_field='width'),
        ),
    ]
