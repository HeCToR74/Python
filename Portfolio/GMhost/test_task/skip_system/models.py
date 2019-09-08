from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User


class Enter(models.Model):
	date = models.DateTimeField(default=datetime.now(), blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	room = models.ForeignKey('Room', related_name='enter_room', on_delete=models.CASCADE)

	def __str__(self):
		return "({} -> {})".format(self.user, self.room)

class Room(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Key(models.Model):
	key = models.CharField(max_length=255, db_index=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	expired = models.DateTimeField(default=datetime.now(), blank=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return "Key for {}".format(User.objects.get(id=self.user.id).username)

class Permission(models.Model):
	room = models.ForeignKey('Room', related_name='permission_room', on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('room', 'user')

	def __str__(self):
		return "({} <-> {})".format(Room.objects.get(id=self.room.id).name, User.objects.get(id=self.user.id).username)  

	
