from django.db import models
from .sections import Sections


# Create your models here.

class Stages(models.Model):
    class Meta:
        db_table = "stages"
        ordering = ['f_section']

    name = models.CharField(max_length=60, null=False)
    f_section = models.ForeignKey(Sections, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
