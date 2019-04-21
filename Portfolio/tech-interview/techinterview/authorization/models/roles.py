from django.db import models


class Roles(models.Model):
    class Meta:
        db_table = "roles"
        ordering = ['id']

    name = models.CharField(max_length=60, default="null")
    permissions = models.ManyToManyField('Permissions')

    def __str__(self):
        return self.name
