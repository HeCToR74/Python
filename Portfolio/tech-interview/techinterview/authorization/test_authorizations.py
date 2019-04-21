from django.test import TestCase, Client
from rest_framework import status
from .models import UserData
from .serializers import UserSerializer

client = Client()


class UserGetTestCases(TestCase):
    """Test for GET User by id"""

    def setUp(self):
        """Create new User"""
        self.adminuser = UserData.objects.create(username='admin', email='example@mail.com',  password="password",  first_name="Name", last_name="Surname")
        # self.adminuser.save()
        # self.adminuser.is_staff = True
        # self.adminuser.save()

    # def test_get_valid_user(self):
    #     """Test for GET User with id '1' """
    #
    #     serializer = UserSerializer(UserData.objects.get(username='admin'))
    #     response = self.client.get('/api/users/' + str(serializer.data['id']))
    #
    #     # Check status of response
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     # Check body of response
    #     self.assertEqual(serializer.data, response.data)
    #
    # def test_get_invalid_user(self):
    #     """Test for GET not existing User """
    #     response = self.client.get('/api/users/99')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
