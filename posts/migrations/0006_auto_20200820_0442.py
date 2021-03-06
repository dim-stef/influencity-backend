# Generated by Django 2.2.4 on 2020-08-20 01:42

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200820_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tier',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='coach', chained_model_field='tier', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', show_all=True, to='tiers.Tier'),
        ),
    ]
