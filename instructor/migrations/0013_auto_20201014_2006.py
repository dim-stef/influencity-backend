# Generated by Django 2.2.4 on 2020-10-14 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0012_auto_20200927_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coachavatar',
            name='coach',
        ),
        migrations.AddField(
            model_name='coach',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='instructor.CoachAvatar'),
        ),
    ]
