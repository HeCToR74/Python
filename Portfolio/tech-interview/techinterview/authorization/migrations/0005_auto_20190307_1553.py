# Generated by Django 2.1.7 on 2019-03-07 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_merge_20190307_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordresetapiview',
            name='resetpasswordtoken_ptr',
        ),
        migrations.DeleteModel(
            name='PasswordResetAPIView',
        ),
    ]
