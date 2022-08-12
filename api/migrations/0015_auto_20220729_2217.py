# Generated by Django 3.1 on 2022-07-29 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20220729_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='JaEn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ja', models.CharField(max_length=100)),
                ('en', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jaen'),
        ),
    ]
