from django.db import models

# Create your models here.

class UsersModel(models.Model):
	class Meta:
		db_table = "Users"
	name = models.CharField(max_length=25)
	password = models.CharField(max_length=25)

class MessagesModel(models.Model):
	class Meta:
		db_table = "Messages"
	user = models.ForeignKey(UsersModel, on_delete=models.DO_NOTHING)
	text = models.TextField()
	date = models.DateTimeField()

