from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from authorization.serializers import RolesSerializer, UserSerializer, UserDataSerializer
from rest_framework.response import Response
from authorization.helper import *


class UserDataListAPIView(ListCreateAPIView):
    """handler for POST request"""

    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def create(self, request, *args, **kwargs):

        try:
            auth = UserSerializer(User.objects.get(username=request.data['auth']))
            role = RolesSerializer(Roles.objects.get(id=request.data['role']))

            request.data['auth'] = auth.data
            request.data['role'] = role.data
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except User.DoesNotExist:
            return Response('User does not exist!', status=status.HTTP_400_BAD_REQUEST)
        except Roles.DoesNotExist:
            return Response('Roles does not exist!', status=status.HTTP_400_BAD_REQUEST)