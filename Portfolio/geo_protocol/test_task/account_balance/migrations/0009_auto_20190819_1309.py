# Generated by Django 2.1.5 on 2019-08-19 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0008_auto_20190819_1255'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Balance',
        ),
        migrations.AlterField(
            model_name='action',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 19, 13, 9, 15, 608393)),
        ),
    ]
