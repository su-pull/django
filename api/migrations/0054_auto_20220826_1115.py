# Generated by Django 3.1 on 2022-08-26 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20220826_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
