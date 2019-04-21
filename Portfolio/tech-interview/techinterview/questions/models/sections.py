from django.db import models


class Sections(models.Model):
    class Meta:
        db_table = "sections"
        ordering = ['id']

    name = models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.name
