# Generated by Django 2.1.5 on 2019-08-15 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0004_auto_20190814_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 15, 11, 39, 24, 448821)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='epitome',
            field=models.TextField(default=''),
        ),
    ]
