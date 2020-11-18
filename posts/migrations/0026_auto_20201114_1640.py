# Generated by Django 2.2.4 on 2020-11-14 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_postvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvideo',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='posts.Post'),
        ),
    ]