from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('User', related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    like = models.IntegerField(default=0, blank=True)
    unlike = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


    
