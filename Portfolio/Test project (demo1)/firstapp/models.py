from django.db import models

class RolesModel(models.Model):
	class Meta:
		db_table = "Roles"
	name = models.CharField(max_length=25)

class UserdataModel(models.Model):
	class Meta:
		db_table = "Userdata"
	name = models.CharField(max_length=25)
	surname = models.CharField(max_length=25)

class CourstitlesModel(models.Model):
	class Meta:
		db_table = "Courstitles"
	cours_name = models.CharField(max_length=50)

class StepsModel(models.Model):
	class Meta:
		db_table = "Steps"
	step_name = models.CharField(max_length=50)
	cours_id = models.ForeignKey(CourstitlesModel, on_delete=models.DO_NOTHING)

class GradesModel(models.Model):
	class Meta:
		db_table = "Grades"
	grade_name = models.CharField(max_length=25)
	grade_value = models.IntegerField()

class QuestionsModel(models.Model):
	class Meta:
		db_table = "Questions"
	step_id = models.ForeignKey(StepsModel, on_delete=models.DO_NOTHING)
	question_name = models.CharField(max_length=50)
	cours_id = models.ForeignKey(CourstitlesModel, on_delete=models.DO_NOTHING)
	description = models.CharField(max_length=500)

class UsersModel(models.Model):
	class Meta:
		db_table = "Users"
	login = models.CharField(max_length=25)
	password = models.CharField(max_length=25)
	role_id = models.ForeignKey(RolesModel, on_delete=models.DO_NOTHING)
	data_id = models.ForeignKey(UserdataModel, on_delete=models.DO_NOTHING)

class AnswersModel(models.Model):
	class Meta:
		db_table = "Answers"
	user_id = models.ForeignKey(UsersModel, on_delete=models.DO_NOTHING)
	question_id = models.ForeignKey(QuestionsModel, on_delete=models.DO_NOTHING)
	answer_like =  models.BooleanField()
	grade_id = models.ForeignKey(GradesModel, on_delete=models.DO_NOTHING)
	reg_date =  models.DateTimeField()

class ExpertusersModel(models.Model):
	class Meta:
		db_table = "Expertusers"
	user_id_ex = models.ForeignKey(UserdataModel, on_delete=models.DO_NOTHING)
	answer_id = models.ForeignKey(AnswersModel, on_delete=models.DO_NOTHING)
	grade_id = models.ForeignKey(GradesModel, on_delete=models.DO_NOTHING)
	comment = models.CharField(max_length=100)




