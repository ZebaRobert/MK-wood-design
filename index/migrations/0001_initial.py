# Generated by Django 5.0.1 on 2024-03-27 14:58

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('backgorund_image', cloudinary.models.CloudinaryField(default='bgPH', max_length=255, verbose_name='bgIMG')),
                ('content', models.TextField()),
            ],
        ),
    ]
