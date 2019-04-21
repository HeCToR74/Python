from django.db import models

class Departments(models.Model):
    class Meta:
        db_table = "departments"
        ordering = ['id']

    name = models.CharField(max_length=100, null=False)
    questions = models.ManyToManyField('questions.Questions')

    def __str__(self):
        return self.name
