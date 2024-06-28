# Generated by Django 5.0.6 on 2024-06-10 06:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default=' ', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
