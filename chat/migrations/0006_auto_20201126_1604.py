# Generated by Django 3.0.9 on 2020-11-26 16:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20201126_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='surrogate',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
        ),
    ]
