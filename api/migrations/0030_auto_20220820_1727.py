# Generated by Django 3.1 on 2022-08-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20220820_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='content_en',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='docs',
            name='description_ja',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='docs',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
