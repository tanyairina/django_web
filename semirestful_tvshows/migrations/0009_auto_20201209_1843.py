# Generated by Django 2.2 on 2020-12-09 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semirestful_tvshows', '0008_auto_20201209_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(default=None, validators=[datetime.datetime]),
        ),
    ]
