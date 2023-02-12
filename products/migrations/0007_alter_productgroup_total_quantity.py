# Generated by Django 4.1.5 on 2023-02-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productgroup_total_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='total_quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='gelen sany'),
            preserve_default=False,
        ),
    ]