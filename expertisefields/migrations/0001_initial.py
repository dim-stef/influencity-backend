# Generated by Django 2.2.4 on 2020-08-17 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertiseField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertiseFieldAvatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('image', models.ImageField(blank=True, height_field='height', null=True, upload_to='static/images', width_field='width')),
                ('expertise_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expertisefields.ExpertiseField')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]