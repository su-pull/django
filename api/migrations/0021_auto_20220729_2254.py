# Generated by Django 3.1 on 2022-07-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_post_titleb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titleB',
            field=models.CharField(max_length=100),
        ),
    ]
