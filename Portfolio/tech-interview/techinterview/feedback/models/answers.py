from django.db import models


class Answers(models.Model):
    class Meta:
        db_table = "answers"
        ordering = ['id']

    answer_like = models.NullBooleanField(default=None, null=True)
    f_grade = models.ForeignKey('feedback.Grades', on_delete=models.SET_NULL, default=None, null=True)
    f_question = models.ForeignKey('questions.Questions', on_delete=models.CASCADE)
    f_interview = models.ForeignKey('interviews.Interviews', on_delete=models.CASCADE)

    def answer_to_bool(self, string):
        self.answer_like = True if string.lower() == 'yes' else False
