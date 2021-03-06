# Generated by Django 4.0 on 2021-12-18 12:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_alter_links_linkaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HeaderDescription', ckeditor.fields.RichTextField()),
                ('HeaderStatus', models.CharField(choices=[('Publish', 'انتشار'), ('Draft', 'پیش نویس')], max_length=10, null=True, verbose_name='وضعیت')),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubDescription', ckeditor.fields.RichTextField()),
                ('SubStatus', models.CharField(choices=[('Publish', 'انتشار'), ('Draft', 'پیش نویس')], max_length=10, null=True, verbose_name='وضعیت')),
            ],
        ),
        migrations.AddField(
            model_name='links',
            name='LinkStatus',
            field=models.CharField(choices=[('Publish', 'انتشار'), ('Draft', 'پیش نویس')], max_length=10, null=True, verbose_name='وضعیت'),
        ),
    ]
