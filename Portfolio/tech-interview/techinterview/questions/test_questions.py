from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework import status
import pytest
from .models import Sections, Stages, Questions


class SectionsPostTestCases(TestCase):
    """Test for POST section"""

    def setUp(self):
        user = User.objects.create(username='testuser', password='qwerty12345Q!')
        user.save()

    def test_post_create_section(self):
        """
        Ensure we can create a new section object.
        """
        url = '/api/questions/sections/'
        data = {"name": "Activities"}
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        response = self.client.post(url, data, format='json', content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        del response.data['id']
        self.assertEqual(response.data, data)


class StagesPostTestCases(TestCase):
    """Test for POST stage"""

    def setUp(self):
        Sections.objects.create(name='section1')
        user = User.objects.create(username='testuser', password='qwerty12345Q!')
        user.save()

    def test_post_create_stage(self):
        """
        Ensure we can create a new stage object.
        """
        url = '/api/questions/stages/'
        data = {'name': 'stage1', 'section': Sections.objects.get(name='section1').id}
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        response = self.client.post(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Stages.objects.filter(name='stage1').exists(), True)

    def test_post_create_stage_with_non_exisitend_section(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        url = '/api/questions/stages/'
        data = {'name': 'stage1', 'section': 56}
        response = self.client.post(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Stages.objects.filter(name='not_exist').exists(), False)


class QuestionsPostTestCases(TestCase):
    """Test for POST question"""

    def setUp(self):
        user = User.objects.create(username='testuser', password='qwerty12345Q!')
        section = Sections.objects.create(name='section1')
        Stages.objects.create(name='stage2', f_section=section)
        user.save()

    def test_post_create_question(self):
        """
        Ensure we can create a new question object.
        """
        section1 = Sections.objects.create(name='section1')
        stage2 = Stages.objects.get(name='stage2')
        url = '/api/questions/questions/'
        data = {'name': 'question1', 'hint': 'hint1', 'stage': {'id': stage2.id, 'name': "stage2", 'section':\
            {'id': section1.id, 'name': 'section1'}}}
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        response = self.client.post(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Questions.objects.filter(name='question1').exists(), True)

    #
    def test_post_create_question_without_hint(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

        """
        Ensure we can create a new question object without hint
        """
        section1 = Sections.objects.create(name='section1')
        stage2 = Stages.objects.get(name='stage2')
        url = '/api/questions/questions/'
        data = {'name': 'question1', 'stage': {'id': stage2.id, 'name': "stage2", 'section': \
            {'id': section1.id, 'name': 'section1'}}}
        response = self.client.post(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Questions.objects.filter(name='question1').exists(), True)

    def test_post_create_question_with_non_exisitend_stage(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        url = '/api/questions/questions/'
        data = {'name': 'question1', 'hint': 'hint1', 'stage': 'not'}
        response = self.client.post(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
