# Generated by Django 2.2.4 on 2020-11-24 01:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0016_auto_20201124_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='surrogate',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
    ]
