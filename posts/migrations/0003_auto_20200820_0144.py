# Generated by Django 2.2.4 on 2020-08-19 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0001_initial'),
        ('posts', '0002_auto_20200817_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='tiers.Tier'),
        ),
        migrations.AlterField(
            model_name='post',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='instructor.Coach'),
        ),
    ]
