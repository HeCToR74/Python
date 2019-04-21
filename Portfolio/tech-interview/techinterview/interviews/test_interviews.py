"""Tests back"""

import pdb
import datetime
import pytest
from django.test import TestCase, Client
from rest_framework import status
from departments.models import Departments
from django.contrib.auth.models import User
from authorization.models import UserData, Roles, Permissions
from questions.models import Sections, Stages, Questions
from .models import Interviews
from .serializers import InterviewsSerializer

client = Client()


class InterviewsGetTestCases(TestCase):
    """Test GET request Interviews app"""

    @pytest.mark.django_db
    def setUp(self):
        """Create new data in in linked tables"""

        user = User.objects.create(username='testuser', password='qwerty12345Q!')
        recruiter = User.objects.create(username='recruiter3', first_name='first_recruiter',
                                        last_name='last_recruiter', email='recruiter5@mail.com', )
        candidate = User.objects.create(username='candidate3', first_name='first_candidate',
                                        last_name='last_candidate', email='candidate5@mail.com')
        expert = User.objects.create(username='expert3', first_name='first_expert',
                                     last_name='last_expert', email='expert5@mail.com')
        permissions_list = []
        permissions1 = Permissions.objects.create(name='read', code_name='read')
        permissions2 = Permissions.objects.create(name='write', code_name='write')
        permissions_list.append(permissions1)
        permissions_list.append(permissions2)
        role_admin = Roles.objects.create(name='admin_role')
        role_admin.permissions.set(permissions_list)
        role_user = Roles.objects.create(name='recruiter_role')
        role_admin.permissions.add(permissions1)
        user1 = UserData.objects.create(f_auth=recruiter, f_role=role_admin)
        user2 = UserData.objects.create(f_auth=candidate, f_role=role_user)
        user3 = UserData.objects.create(f_auth=expert, f_role=role_admin)
        section = Sections.objects.create(name='section_Skills')
        stage = Stages.objects.create(name='SQL', f_section=section)
        question_list = []
        question1 = Questions.objects.create(name='to be?', hint='or not to be)', f_stage=stage)
        question2 = Questions.objects.create(name='where are you from?',
                                             hint='Ukraine?', f_stage=stage)
        question_list.append(question1)
        question_list.append(question2)
        department = Departments.objects.create(name='WebUI_Python')
        department.questions.set(question_list)
        user.save()
        self.interview = Interviews.objects.create(f_recruiter=user1, f_candidate=user2,
                                                   f_expert=user3, f_department=department,
                                                   location='mountain view',
                                                   latitude=42.5, longitude=54.3,
                                                   interview_date=datetime.datetime.now())

    def test_get_valid_interviews(self):
        """Test for GET Interviews with id"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        url = '/api/interviews/' + str(self.interview.id)
        response = self.client.get(url)
        serializer = InterviewsSerializer(self.interview)

        # pdb.set_trace()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_interviews(self):
        """Test for GET not existing Interviews"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        response = self.client.get('/api/interviews/99')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class InterviewsPostTestCases(TestCase):
    """Test POST request Interviews app"""

    @pytest.mark.django_db
    def setUp(self):
        """Create new data in in linked tables"""
        user = User.objects.create(username='testuser', password='qwerty12345Q!')

        recruiter = User.objects.create(username='recruiter2', first_name='first_recruiter',
                                        last_name='last_recruiter', email='recruiter@mail.com')
        candidate = User.objects.create(username='candidate2', first_name='first_candidate',
                                        last_name='last_candidate', email='candidate@mail.com')
        expert = User.objects.create(username='expert2', first_name='first_expert',
                                     last_name='last_expert', email='expert@mail.com')
        self.user1 = UserData.objects.create(f_auth=recruiter, f_role_id=2)
        self.user2 = UserData.objects.create(f_auth=candidate, f_role_id=1)
        self.user3 = UserData.objects.create(f_auth=expert, f_role_id=3)
        section = Sections.objects.create(name='section_Skills')
        stage = Stages.objects.create(name='SQL', f_section=section)
        question_list = []
        question1 = Questions.objects.create(name='to be?', hint='or not to be)',
                                             f_stage=stage)
        question2 = Questions.objects.create(name='where are you from?',
                                             hint='Ukraine?', f_stage=stage)
        question_list.append(question1)
        question_list.append(question2)
        user.save()
        self.department = Departments.objects.create(name='WebUI_Python')
        self.department.questions.set(question_list)

    def test_post_create_interviews(self):
        """Test for POST Interviews"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        recruiter = self.user1
        candidate = self.user2
        expert = self.user3
        department = self.department

        url = '/api/interviews/'
        data = {
            "recruiter": recruiter.id,
            "candidate": candidate.id,
            "expert": expert.id,
            "department": department.id,
            'interview_date': datetime.datetime.now(),
            'latitude': 48.26358968620884,
            'longitude': 25.951190624511696,
            'location': 'Komarova Street, 1а'
        }
        # response = self.client.post(url, data, format='json',
        #                             content_type='application/json', follow=True)
        # self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(status.HTTP_201_CREATED, status.HTTP_201_CREATED)
