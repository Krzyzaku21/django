# Generated by Django 3.1.4 on 2021-01-28 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20210127_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 14, 30, 53, 26490), verbose_name='Date'),
        ),
    ]