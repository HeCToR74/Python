# Generated by Django 2.1.7 on 2019-04-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0010_auto_20190411_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='name',
            field=models.CharField(default='null', max_length=60),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='avatar',
            field=models.URLField(default='https://techintbaseforavatar.s3.amazonaws.com/user.jpg', max_length=150),
        ),
    ]
