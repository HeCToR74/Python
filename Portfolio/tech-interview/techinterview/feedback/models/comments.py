from django.db import models


class Comments(models.Model):
    class Meta:
        db_table = "comments"
        ordering = ['id']

    f_question = models.ForeignKey('questions.Questions', on_delete=models.CASCADE)
    f_grade = models.ForeignKey('feedback.Grades', on_delete=models.SET_NULL, null=True)
    comment = models.TextField(default=None, null=True)
    f_interview = models.ForeignKey('interviews.Interviews', on_delete=models.CASCADE)
