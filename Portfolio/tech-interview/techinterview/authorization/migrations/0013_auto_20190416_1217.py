# Generated by Django 2.1.7 on 2019-04-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0012_merge_20190415_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='avatar',
            field=models.URLField(default='https://techintbaseforavatar.s3.amazonaws.com/default-avatar.jpg', max_length=150),
        ),
    ]
