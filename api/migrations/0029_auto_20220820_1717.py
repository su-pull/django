# Generated by Django 3.1 on 2022-08-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20220820_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='content_en',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='docs',
            name='description_ja',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='docs',
            name='slug',
            field=models.SlugField(),
        ),
    ]
