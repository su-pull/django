# Generated by Django 3.1 on 2022-07-29 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20220729_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.jaen'),
        ),
    ]