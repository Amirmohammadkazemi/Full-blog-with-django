# Generated by Django 4.0 on 2021-12-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='LinkAddress',
            field=models.CharField(max_length=1000, verbose_name='آدرس لینک'),
        ),
    ]
