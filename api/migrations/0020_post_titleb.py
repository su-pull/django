# Generated by Django 3.1 on 2022-07-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20220729_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titleB',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
