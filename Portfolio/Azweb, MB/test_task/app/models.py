from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

