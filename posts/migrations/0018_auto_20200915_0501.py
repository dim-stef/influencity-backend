# Generated by Django 2.2.4 on 2020-09-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20200915_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='chained_posts',
            field=models.ManyToManyField(blank=True, null=True, related_name='parent_post', to='posts.Post'),
        ),
    ]