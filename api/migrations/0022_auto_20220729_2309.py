# Generated by Django 3.1 on 2022-07-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20220729_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='titleB',
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ja',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ja',
            field=models.CharField(default='', max_length=100),
        ),
    ]
