# Generated by Django 2.1.7 on 2019-03-19 06:09

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('pub_posts', django.db.models.manager.Manager()),
            ],
        ),
    ]
