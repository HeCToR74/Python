from django.db import models

class Text(models.Model):
    text = models.TextField()

class Keyphrase(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=200)
    exist = models.BooleanField()
    disambiguation = models.BooleanField()

