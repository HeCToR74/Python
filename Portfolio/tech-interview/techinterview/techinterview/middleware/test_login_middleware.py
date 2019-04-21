from django.test import TestCase, Client
from rest_framework import status
import pytest

from departments.models import Departments
from departments.serializers import DepartmentsSerializer
from questions.models import Sections, Stages, Questions
from django.contrib.auth.models import User


client = Client()


class DepartmentMiddlewareTestCases(TestCase):
    """Test for GET department with unlogin user by id"""

    @pytest.mark.django_db
    def setUp(self):
        """Create new department and fill questions"""
        section1 = Sections.objects.create(name='section1')
        stages = Stages.objects.bulk_create([
            Stages(name='stage1', f_section=section1),
            Stages(name='stage2', f_section=section1),
        ])
        Questions.objects.bulk_create([
            Questions(name='question1', f_stage=stages[0]),
            Questions(name='question2', f_stage=stages[0]),
            Questions(name='question3', f_stage=stages[1]),
            Questions(name='question4', f_stage=stages[1]),
        ])

        dep1 = Departments.objects.create(name='depart1')
        dep1.questions.add(*Questions.objects.all())
        dep1.save()

    def test_get_valid_department_no_login_user(self):
        """Test for GET Department with id '2' with unlogin user and get error """

        serializer = DepartmentsSerializer(Departments.objects.get(name='depart1'))

        response = self.client.get('/api/departments/' + str(serializer.data['id']))

        # Check status of response
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
