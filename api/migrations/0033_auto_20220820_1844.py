# Generated by Django 3.1 on 2022-08-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20220820_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='description_ja',
            field=models.TextField(blank=True, null=True),
        ),
    ]