# Generated by Django 2.2.5 on 2019-09-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_Image/', verbose_name='Product'),
        ),
    ]
