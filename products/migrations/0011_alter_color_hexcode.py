# Generated by Django 4.1.5 on 2023-02-17 11:09

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_colors_product_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='hexCode',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None, verbose_name='hex kod'),
        ),
    ]