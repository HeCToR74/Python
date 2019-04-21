# Generated by Django 2.1.7 on 2019-03-04 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_passwordreset', '0002_pk_migration'),
        ('authorization', '0002_auto_20190220_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetAPIView',
            fields=[
                ('resetpasswordtoken_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_rest_passwordreset.ResetPasswordToken')),
            ],
            bases=('django_rest_passwordreset.resetpasswordtoken',),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='f_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authorization.Roles'),
        ),
    ]
