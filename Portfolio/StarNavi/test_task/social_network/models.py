from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    like = models.IntegerField(default=0, blank=True)
    unlike = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


    
