# Generated by Django 2.2.4 on 2020-10-23 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expertisefields', '0003_auto_20200824_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertisefieldavatar',
            name='expertise_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='expertisefields.ExpertiseField'),
        ),
    ]
