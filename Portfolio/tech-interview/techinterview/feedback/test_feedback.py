from django.test import TestCase, Client
from rest_framework import status
from .models import Grades, Answers, Comments
from django.contrib.auth.models import User
from departments.models import Departments
from authorization.models import UserData, Roles, Permissions
from questions.models import Questions, Stages, Sections
from interviews.models import Interviews
from .serializers import GradesSerializer, AnswersSerializer, CommentsSerializer
import pytest
import datetime

import pdb

client = Client()


class AnswersGetTestCases(TestCase):
    """Test GET request Answers app"""

    @pytest.mark.django_db
    def setUp(self):
        """Create new data in in linked tables"""
        user = User.objects.create(username='testuser', password='qwerty12345Q!')

        recruiter = User.objects.create(username='recruiter3', first_name='first_recruiter',
                                        last_name='last_recruiter', email='recruiter@mail.com',)
        candidate = User.objects.create(username='candidate3', first_name='first_candidate',
                                        last_name='last_candidate', email='candidate@mail.com')
        expert = User.objects.create(username='expert3', first_name='first_expert',
                                     last_name='last_expert', email='expert@mail.com')
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
        department = Departments.objects.create(name='WebUI_Python')
        interview = Interviews.objects.create(f_recruiter=user1, f_candidate=user2,
                                              f_expert=user3, f_department=department,
                                              interview_date=datetime.datetime.now())
        grade = Grades.objects.create(name='grade1', weight=1)
        stage = Stages.objects.create(name='stage1')
        question = Questions.objects.create(name='ques1', hint='question1 is important', f_stage=stage)
        self.answers = Answers.objects.create(f_grade=grade, f_question=question, f_interview=interview)

    def test_get_valid_answers(self):
        """Test for GET Answers with id"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        url = '/api/feedback/answers/' + str(self.answers.id)
        response = self.client.get(url)
        serializer = AnswersSerializer(self.answers)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_answers(self):
        """Test for GET not existing Answers"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        response = self.client.get('/api/feedback/answers/99')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class AnswersPostTestCases(TestCase):
    """Test POST request Answers app"""

    @pytest.mark.django_db
    def setUp(self):
        """Create new data in in linked tables"""
        user = User.objects.create(username='testuser', password='qwerty12345Q!')

        recruiter = User.objects.create(username='recruiter3', first_name='first_recruiter',
                                        last_name='last_recruiter', email='recruiter@mail.com', )
        candidate = User.objects.create(username='candidate3', first_name='first_candidate',
                                        last_name='last_candidate', email='candidate@mail.com')
        expert = User.objects.create(username='expert3', first_name='first_expert',
                                     last_name='last_expert', email='expert@mail.com')
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
        department = Departments.objects.create(name='WebUI_Python')
        self.interview = Interviews.objects.create(f_recruiter=user1, f_candidate=user2, f_expert=user3,
                                                   f_department=department,
                                                   interview_date=datetime.datetime.now())
        self.grade = Grades.objects.create(name="grade1", weight=1)
        section = Sections.objects.create(name='section')
        stage = Stages.objects.create(name='stage1', f_section=section)
        self.question = Questions.objects.create(name='ques1', hint='question1 is important', f_stage=stage)

    def test_post_create_answers(self):
        """Test for POST Answers"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        url = '/api/feedback/answers/bulk'
        response = self.client.post(url, [], format='json', content_type='application/json', follow=True)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


class CommentsGetTestCases(TestCase):
    """Test GET request Comments app"""

    def setUp(self):
        """Create new data in in linked tables"""
        user = User.objects.create(username='testuser', password='qwerty12345Q!')

        recruiter = User.objects.create(username='recruiter4', first_name='first4_recruiter',
                                        last_name='last_recruiter', email='recruiter4@mail.com', )
        candidate = User.objects.create(username='candidate4', first_name='first_candidate',
                                        last_name='last_candidate', email='candidate4@mail.com')
        expert = User.objects.create(username='expert4', first_name='first_expert',
                                     last_name='last_expert', email='expert4@mail.com')
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
        department = Departments.objects.create(name='WebUI_Python')
        interview = Interviews.objects.create(f_recruiter=user1, f_candidate=user2,
                                              f_expert=user3, f_department=department,
                                              interview_date=datetime.datetime.now())
        grade = Grades.objects.create(name='grade1', weight=1)
        stage = Stages.objects.create(name='stage2')
        question = Questions.objects.create(name='ques2', hint='question2 is important', f_stage=stage)
        self.comment = Comments.objects.create(comment='comment for comment1', f_question=question,
                                               f_grade=grade, f_interview=interview)

    def test_get_valid_comments(self):
        """Test for GET Comments with id"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        url = '/api/feedback/comments/' + str(self.comment.id)
        response = self.client.get(url)
        serializer = CommentsSerializer(self.comment)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_comments(self):
        """Test for GET not existing Comments"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        response = self.client.get('/api/feedback/comments/99')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class CommentsPostTestCases(TestCase):
    """Test POST request Comments app"""

    @pytest.mark.django_db
    def setUp(self):
        """Create new data in in linked tables"""
        user = User.objects.create(username='testuser', password='qwerty12345Q!')

        recruiter = User.objects.create(username='recruiter3', first_name='first_recruiter',
                                        last_name='last_recruiter', email='recruiter@mail.com', )
        candidate = User.objects.create(username='candidate3', first_name='first_candidate',
                                        last_name='last_candidate', email='candidate@mail.com')
        expert = User.objects.create(username='expert3', first_name='first_expert',
                                     last_name='last_expert', email='expert@mail.com')
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
        department = Departments.objects.create(name='WebUI_Python')
        self.interview = Interviews.objects.create(f_recruiter=user1, f_candidate=user2, f_expert=user3,
                                                   f_department=department, interview_date=datetime.datetime.now())
        section = Sections.objects.create(name='section1')
        stage = Stages.objects.create(name='stage1', f_section=section)
        self.question = Questions.objects.create(name='question1', hint='question1 is special', f_stage=stage)
        self.grade = Grades.objects.create(name='grade3', weight=3)

    def test_post_create_comments(self):
        """Test for POST Comments"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        url = '/api/feedback/comments/bulk'
        response = self.client.post(url, [], format='json', content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


class GradesGetTestCases(TestCase):
    """Test POST request Grades app"""

    @pytest.mark.django_db
    def setUp(self):
        """Create new data in linked tables"""
        user = User.objects.create(username='testuser', password='qwerty12345Q!')

        # grade1 = Grades.objects.create(name='grades1', weight=1)
        self.grades = Grades.objects.create(name='grades1', weight=1)

    def test_get_valid_grades(self):
        """Test for GET Grades with id"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        url = '/api/feedback/grades/' + str(self.grades.id)
        response = self.client.get(url)
        serializer = GradesSerializer(self.grades)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_grades(self):
        """Test for GET not existing Grades"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        response = self.client.get('/api/feedback/grades/99')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class GradesPostTestCases(TestCase):
    """Test POST request Grades app"""

    def test_post_create_grades(self):
        """Test for POST Grades"""
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        url = '/api/feedback/grades/'
        data = {'name': 'grades33', 'weight': 1}
        response = self.client.post(url, data, format='json', content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
