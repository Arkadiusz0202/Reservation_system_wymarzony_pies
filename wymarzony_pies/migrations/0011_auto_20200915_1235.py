# Generated by Django 3.1.1 on 2020-09-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wymarzony_pies', '0010_remove_reservation_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='open_form',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='location',
            name='open_to',
            field=models.CharField(max_length=128),
        ),
    ]