# Generated by Django 2.1.7 on 2019-02-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('questions', models.ManyToManyField(to='questions.Questions')),
            ],
            options={
                'db_table': 'departments',
                'ordering': ['id'],
            },
        ),
    ]
