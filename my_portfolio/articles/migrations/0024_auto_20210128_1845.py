# Generated by Django 3.1.4 on 2021-01-28 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_auto_20210128_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 18, 45, 12, 98225), verbose_name='Date'),
        ),
    ]