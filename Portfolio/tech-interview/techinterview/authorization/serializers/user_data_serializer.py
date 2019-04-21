from rest_framework import serializers
from django.contrib.auth.models import User
from authorization.models import UserData, Roles
from .user_serializer import UserSerializer
from .roles_serializer import RolesSerializer


class UserDataSerializer(serializers.ModelSerializer):
    """UserDataSerializer"""

    auth = UserSerializer(source='f_auth')
    role = RolesSerializer(source='f_role', read_only=True)

    class Meta:
        """Meta"""
        model = UserData
        fields = ('auth', 'role')

    def create(self, validated_data):
        validated_data['f_auth'] = dict(validated_data['f_auth'])
        validated_data['f_role'] = dict(validated_data['f_role'])
        auth = User.objects.get(id=validated_data.get('id'))
        role = Roles.objects.get(id=validated_data.get('id'))
        avatar = validated_data['avatar']
        instance = UserData.objects.create(f_auth=User.objects.get(id=auth['id']),
                                           f_role=Roles.objects.get(id=role['id']))
        return instance
