# Generated by Django 2.1.7 on 2019-04-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_auto_20190404_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
