# Generated by Django 3.1.4 on 2021-01-19 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20210119_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 14, 9, 15, 855936), verbose_name='Date'),
        ),
    ]