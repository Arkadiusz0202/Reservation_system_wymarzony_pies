# Generated by Django 3.1 on 2020-08-20 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wymarzony_pies', '0009_auto_20200820_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='customer',
        ),
    ]
