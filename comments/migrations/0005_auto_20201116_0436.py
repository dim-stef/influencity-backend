# Generated by Django 2.2.4 on 2020-11-16 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20201116_0435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='updated_at',
            new_name='updated',
        ),
    ]