# Generated by Django 3.1 on 2021-04-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_milestonecompletionreport_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestonecompletionreport',
            name='coach_feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
