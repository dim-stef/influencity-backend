# Generated by Django 2.2.4 on 2020-11-14 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_auto_20201114_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaybackId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.CharField(max_length=30)),
                ('playback_id', models.CharField(max_length=100)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playback_ids', to='posts.PostVideo')),
            ],
        ),
    ]