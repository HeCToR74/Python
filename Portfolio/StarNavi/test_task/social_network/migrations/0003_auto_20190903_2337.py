# Generated by Django 2.0.10 on 2019-09-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0002_auto_20190903_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
