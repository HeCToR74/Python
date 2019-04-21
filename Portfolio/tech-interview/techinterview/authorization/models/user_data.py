from django.db import models
from .roles import Roles
from django.contrib.auth.models import User

class UserData(models.Model):
    class Meta:
        db_table = 'user_data'
        ordering = ['id']

    f_auth = models.OneToOneField(User, on_delete=models.CASCADE)
    f_role = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)

    avatar = models.URLField(max_length=150,
                             default='/static/images/avatar/default-avatar.jpg')

    def __str__(self):
        return self.f_auth.username
