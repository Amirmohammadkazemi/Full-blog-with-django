# Generated by Django 4.0.1 on 2022-02-04 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_category_parentcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='CategoryStatus',
        ),
    ]
