# Generated by Django 2.2.4 on 2020-11-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0014_auto_20201014_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='bio',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]
