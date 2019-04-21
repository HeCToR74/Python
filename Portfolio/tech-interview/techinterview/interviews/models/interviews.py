from django.db import models
from authorization.models.user_data import UserData
from departments.models.departments import Departments
from model_utils import Choices


class Interviews(models.Model):
    """Interviews Model"""

    class Meta:
        db_table = 'interviews'
        ordering = ['id']

    f_recruiter = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='f_recruiter_id')
    f_candidate = models.ForeignKey(UserData, on_delete=models.SET_NULL, related_name='f_candidate_id', null=True)
    f_expert = models.ForeignKey(UserData, on_delete=models.SET_NULL, related_name='f_expert_id', null=True)
    f_department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    interview_date = models.DateTimeField()
    completion_date = models.DateTimeField(default=None, null=True, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    location = models.CharField(max_length=200, null=True)
    STATUS = Choices('scheduled', 'completed', 'canceled')
    status = models.CharField(max_length=35, choices=STATUS, default=STATUS.scheduled)

    def __str__(self):
        return 'Interview with {candidate}. Expert - {expert}. Recruiter - {recruiter}. Date: {date}'.format(
            candidate=self.f_candidate.__str__(),
            expert=self.f_expert.__str__(),
            recruiter=self.f_recruiter.__str__(),
            date=self.created_date)
