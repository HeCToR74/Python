from django.db import models
from django.db.models.query import QuerySet


class Grades(models.Model):
    class Meta:
        db_table = "grades"
        ordering = ['id']

    name = models.CharField(max_length=30, null=False, unique=True)
    weight = models.SmallIntegerField(null=False, unique=True)

    def __str__(self):
        return self.name.title()
