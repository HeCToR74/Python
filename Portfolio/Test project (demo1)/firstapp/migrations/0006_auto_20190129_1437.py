# Generated by Django 2.1.5 on 2019-01-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_remove_stepsmodel_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courstitlesmodel',
            name='cours_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='question_name',
            field=models.CharField(max_length=50),
        ),
    ]
