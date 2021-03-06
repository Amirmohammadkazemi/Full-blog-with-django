# Generated by Django 4.0 on 2021-12-18 11:34

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_article_articlestatus_projects_projectstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ArticleDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='support',
            name='SupportDescription',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='توضیحات '),
        ),
        migrations.AlterField(
            model_name='support',
            name='SupportImage',
            field=models.ImageField(null=True, upload_to='', verbose_name='تصویر'),
        ),
    ]
