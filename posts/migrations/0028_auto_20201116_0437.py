# Generated by Django 2.2.4 on 2020-11-16 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_playbackid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
