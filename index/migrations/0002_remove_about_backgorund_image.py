# Generated by Django 5.0.1 on 2024-06-11 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='backgorund_image',
        ),
    ]
