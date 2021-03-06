# Generated by Django 3.1.7 on 2021-07-19 09:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0002_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
