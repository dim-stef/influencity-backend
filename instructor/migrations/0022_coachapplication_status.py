# Generated by Django 3.0.9 on 2021-02-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0021_coachapplication_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='coachapplication',
            name='status',
            field=models.CharField(choices=[('PD', 'Pending'), ('AP', 'Approved'), ('RJ', 'Rejected')], default='PD', max_length=2),
        ),
    ]
