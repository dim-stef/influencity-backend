# Generated by Django 3.1 on 2021-06-16 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0033_auto_20210514_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestonecompletionreport',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milestone_completion_reports', to='projects.team'),
        ),
    ]
