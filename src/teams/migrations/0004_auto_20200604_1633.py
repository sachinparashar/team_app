# Generated by Django 3.0.6 on 2020-06-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20200530_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
