# Generated by Django 3.1 on 2021-03-12 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='awards')),
                ('is_primary', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='award',
            name='description',
        ),
        migrations.RemoveField(
            model_name='award',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='award',
            name='is_primary',
        ),
        migrations.AddField(
            model_name='award',
            name='award',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='awards.awardbase'),
        ),
    ]