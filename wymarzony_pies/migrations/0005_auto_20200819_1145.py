# Generated by Django 3.1 on 2020-08-19 09:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wymarzony_pies', '0004_auto_20200817_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='training',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(default=1, max_length=128, verbose_name='Twoje imię'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='date_of_reservation',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='reservation',
            name='res_from',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='res_to',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='training',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wymarzony_pies.training'),
            preserve_default=False,
        ),
    ]
