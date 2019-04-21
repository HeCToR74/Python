from django.test import TestCase, Client
from rest_framework import status
import pytest
from questions.models import Sections, Stages, Questions
from .models import Departments
from departments.serializers import DepartmentsSerializer
from django.contrib.auth.models import User

client = Client()


class DepartmentGetTestCases(TestCase):
    """Test for GET department by id"""

    @pytest.mark.django_db
    def setUp(self):
        """Create new department and fill questions"""
        user = User.objects.create(username='testuser', password='qwerty12345Q!')
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
        user.save()

    def test_get_valid_department(self):
        """Test for GET Department with id '2' """

        # Note: PostGre server not working properly with setup
        # and give to new instance id=2
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        serializer = DepartmentsSerializer(Departments.objects.get(name='depart1'))

        response = self.client.get('/api/departments/' + str(serializer.data['id']))

        # Check status of response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check body of response
        self.assertEqual(serializer.data, response.data)

    def test_get_invalid_department(self):
        """Test for GET not existing Department """
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        response = self.client.get('api/departments/51000')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


@pytest.mark.django_db
class DepartmentPostTestCases(TestCase):
    """Test for POST department"""

    @pytest.fixture(autouse=True)
    def setup_stuff(self, db):
        user = User.objects.create(username='testuser', password='qwerty12345Q!')
        user.save()

    def test_post_create_department(self):
        """
        Ensure we can create a new department object.
        """
        url = '/api/departments/'
        data = {"name": "java", "questions": list()}

        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        expected = {'name': 'java', 'sections': {}}
        response = self.client.post(url, data, format='json', content_type='application/json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        print(dir(response))
        response.data.pop('id')
        self.assertEqual(response.data, expected)
