# Generated by Django 2.2.4 on 2020-10-30 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20201022_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='milestone',
            old_name='level',
            new_name='description',
        ),
    ]
