# Generated by Django 3.1.4 on 2021-01-14 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210114_1229'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
    ]
