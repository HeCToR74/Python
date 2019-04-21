from django.db import models
from .interviews import Interviews


class InterviewsRes(models.Model):

    class Meta:
        db_table = 'interviewsRes'
        ordering = ['id']

    summary_of_qualification = models.TextField()
    years_of_experience = models.IntegerField()
    level = models.CharField(max_length=45)
    level_com = models.TextField()
    gaps = models.TextField()
    gaps_com = models.TextField()
    technical_english = models.CharField(max_length=45)
    technical_english_com = models.TextField()
    high_potential = models.CharField(max_length=45)
    high_potential_com = models.TextField()
    potentially_hire = models.CharField(max_length=45)
    potentially_hire_com = models.TextField()
    f_interview_id = models.OneToOneField(Interviews, related_name='f_interview_res_id', on_delete=models.CASCADE)