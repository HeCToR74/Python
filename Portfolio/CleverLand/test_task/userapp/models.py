from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    about_myself = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return "{} {}".format(self.name, self.lastname)
