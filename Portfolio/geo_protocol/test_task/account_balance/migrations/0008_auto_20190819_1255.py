# Generated by Django 2.1.5 on 2019-08-19 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0007_auto_20190815_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 19, 12, 55, 5, 346761))),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='action',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 19, 12, 55, 5, 345760)),
        ),
    ]
