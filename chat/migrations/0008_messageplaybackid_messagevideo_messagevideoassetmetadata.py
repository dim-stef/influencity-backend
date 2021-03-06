# Generated by Django 3.1 on 2021-03-14 17:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_chatroom_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageVideoAssetMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passthrough', models.UUIDField(default=uuid.uuid1)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.message')),
            ],
        ),
        migrations.CreateModel(
            name='MessageVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passthrough', models.UUIDField(verbose_name=uuid.uuid1)),
                ('asset_id', models.CharField(max_length=120)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='chat.message')),
            ],
        ),
        migrations.CreateModel(
            name='MessagePlaybackId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.CharField(max_length=30)),
                ('playback_id', models.CharField(max_length=100)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playback_ids', to='chat.messagevideo')),
            ],
        ),
    ]
