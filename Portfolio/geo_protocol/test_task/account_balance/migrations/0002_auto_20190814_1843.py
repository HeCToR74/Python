# Generated by Django 2.1.5 on 2019-08-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
