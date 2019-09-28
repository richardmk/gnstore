# Generated by Django 2.2.5 on 2019-09-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190924_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default=1, max_length=250, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=150, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='author',
            name='facebook',
            field=models.URLField(max_length=150, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='author',
            name='instagram',
            field=models.URLField(max_length=150, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.URLField(max_length=300, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, verbose_name='title'),
        ),
    ]
