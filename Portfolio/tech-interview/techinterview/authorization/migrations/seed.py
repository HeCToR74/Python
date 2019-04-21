# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Roles = apps.get_model("authorization", "Roles")
    db_alias = schema_editor.connection.alias
    print("Creating roles...")
    Roles.objects.using(db_alias).bulk_create([
        Roles(name="candidate"),
        Roles(name="recruiter"),
        Roles(name="expert"),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates three Roles instances,
    # so reverse_func() should delete them.
    Roles = apps.get_model("authorization", "Roles")
    db_alias = schema_editor.connection.alias
    print("Deleting roles...")
    Roles.objects.using(db_alias).filter(name="candidate").delete()
    Roles.objects.using(db_alias).filter(name="recruiter").delete()
    Roles.objects.using(db_alias).filter(name="expert").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_auto_20190312_1603'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
