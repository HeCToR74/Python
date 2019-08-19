from django.db import models
from datetime import datetime

class Customer(models.Model):
    name = models.CharField(max_length=255)
    balance = models.IntegerField()

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.ForeignKey('Customer', related_name='customeres', on_delete=models.CASCADE)
    point = models.IntegerField()
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return Customer.objects.get(id=self.name.id).name + ' (' + str(self.date) +')'

class Balance(models.Model):
    date = models.DateTimeField(default=datetime.now(), blank=True)
    balance = models.IntegerField()
