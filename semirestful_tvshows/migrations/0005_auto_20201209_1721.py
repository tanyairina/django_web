# Generated by Django 2.2 on 2020-12-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semirestful_tvshows', '0004_auto_20201209_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]
