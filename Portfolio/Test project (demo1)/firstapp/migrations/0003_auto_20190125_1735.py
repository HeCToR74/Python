# Generated by Django 2.1.5 on 2019-01-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20190125_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepsmodel',
            name='group_name',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='stepsmodel',
            name='step_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
