# Generated by Django 2.2.4 on 2020-09-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
        ('projects', '0003_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(related_name='teams', to='subscribers.Subscriber')),
            ],
        ),
    ]
