# Generated by Django 2.1.7 on 2019-04-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_auto_20190404_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='active',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]