# Generated by Django 2.2.4 on 2020-08-20 01:50

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200820_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tier',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='coach', chained_model_field='tier', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='tiers.Tier'),
        ),
    ]