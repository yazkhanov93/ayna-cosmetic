# Generated by Django 4.1.5 on 2023-02-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_banner_blurhash_productimage_blurhash_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='blurhash',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='blurhash'),
        ),
    ]
