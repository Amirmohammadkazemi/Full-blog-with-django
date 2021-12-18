# Generated by Django 4.0 on 2021-12-18 11:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_article_articleslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ArticleBody',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Body', null=True, verbose_name='بدنه'),
        ),
        migrations.AddField(
            model_name='article',
            name='ArticleDate',
            field=models.DateField(null=True, verbose_name='تاریخ'),
        ),
        migrations.AddField(
            model_name='article',
            name='ArtileThumbnail',
            field=models.ImageField(null=True, upload_to='', verbose_name='تصویر مقاله'),
        ),
    ]
