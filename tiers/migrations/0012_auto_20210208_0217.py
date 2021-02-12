# Generated by Django 3.1 on 2021-02-08 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0011_tier_subscriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tier',
            name='tier',
            field=models.CharField(choices=[('FR', 'Free'), ('T1', 'Tier 1'), ('T2', 'Tier 2')], default='FR', max_length=2),
        ),
    ]
