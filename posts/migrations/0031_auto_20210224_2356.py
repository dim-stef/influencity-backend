# Generated by Django 3.1 on 2021-02-24 23:56

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0013_remove_tier_subscriptions'),
        ('posts', '0030_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='tiers.tier'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tiers',
            field=smart_selects.db_fields.ChainedManyToManyField(auto_choose=True, chained_field='coach', chained_model_field='coach', horizontal=True, null=True, related_name='all_posts', to='tiers.Tier'),
        ),
    ]
