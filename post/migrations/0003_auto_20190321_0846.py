# Generated by Django 2.1.7 on 2019-03-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190321_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thum_image',
            field=models.ImageField(blank=True, default='post/posts/default-thumbnail.jpg', upload_to='post/posts/', verbose_name='Thumb image'),
        ),
    ]