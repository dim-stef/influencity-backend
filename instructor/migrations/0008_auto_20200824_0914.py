# Generated by Django 2.2.4 on 2020-08-24 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0007_auto_20200824_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachavatar',
            name='coach',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='instructor.Coach'),
        ),
    ]
