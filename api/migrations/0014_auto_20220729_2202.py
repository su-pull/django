# Generated by Django 3.1 on 2022-07-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20220729_2144'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostJaEn',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]