# Generated by Django 4.0 on 2021-12-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ArticleCategory',
            field=models.ManyToManyField(to='pages.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CategoryStatus',
            field=models.BooleanField(default=True, verbose_name='نمایش'),
        ),
    ]
