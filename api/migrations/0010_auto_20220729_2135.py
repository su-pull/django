# Generated by Django 3.1 on 2022-07-29 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220727_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostJaEn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ja', models.CharField(max_length=100)),
                ('en', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.postjaen'),
        ),
    ]