# Generated by Django 2.1.5 on 2019-01-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20190125_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepsmodel',
            name='group_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stepsmodel',
            name='step_name',
            field=models.CharField(max_length=50),
        ),
    ]
