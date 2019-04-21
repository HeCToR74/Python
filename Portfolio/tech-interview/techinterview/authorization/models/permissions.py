from django.db import models


class Permissions(models.Model):
    class Meta:
        db_table = "permissions"
        ordering = ['id']

    name = models.CharField(max_length=255, default='No name')
    code_name = models.CharField(max_length=100, default='No codename')

    def __str__(self):
        return self.name