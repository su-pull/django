# Generated by Django 3.1 on 2022-08-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20220820_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ja', models.CharField(max_length=100)),
                ('content_ja', models.TextField()),
                ('description_ja', models.TextField()),
                ('title_en', models.CharField(max_length=100)),
                ('content_en', models.TextField()),
                ('description_en', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
