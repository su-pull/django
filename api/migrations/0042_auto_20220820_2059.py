# Generated by Django 3.1 on 2022-08-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_auto_20220820_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True),
        ),
    ]
