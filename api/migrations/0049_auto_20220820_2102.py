# Generated by Django 3.1 on 2022-08-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_auto_20220820_2102'),
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
            field=models.TextField(max_length=300),
        ),
    ]
