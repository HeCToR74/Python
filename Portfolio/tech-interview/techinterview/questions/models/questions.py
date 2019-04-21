from django.db import models
from .stages import Stages


# Create your models here.

class Questions(models.Model):
    class Meta:
        db_table = "questions"
        ordering = ['f_stage']

    name = models.TextField(max_length=255, null=False)
    hint = models.TextField(max_length=300, default=None, null=True)
    f_stage = models.ForeignKey(Stages, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
