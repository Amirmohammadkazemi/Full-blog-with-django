# Generated by Django 4.0 on 2021-12-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LinkName', models.CharField(max_length=100)),
                ('LinkAddress', models.CharField(max_length=500, verbose_name='آدرس لینک')),
            ],
        ),
    ]
