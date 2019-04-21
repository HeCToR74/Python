"""AUTH serialiters"""

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import UserData, Permissions, Roles


class PermissionsSerializer(serializers.ModelSerializer):
    """PermissionsSerializer"""

    class Meta:
        """Meta"""
        model = Permissions
        fields = ('name', 'code_name')


class RolesSerializer(serializers.ModelSerializer):
    """RolesSerializer"""

    permissions = PermissionsSerializer(many=True)

    class Meta:
        """Meta"""
        model = Roles
        fields = ('name', 'permissions')

    def create(self, validated_data):
        instance = Roles.objects.create(name=validated_data.get('name'))

        for permission in validated_data['permissions']:
            permission = dict(permission)

            permission_name = Permissions.objects.get(name=permission['name'])
            instance.permissions.add(permission_name)
            instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    """UserSerializer"""

    id = serializers.ReadOnlyField()

    class Meta:
        """Meta"""
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


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
        instance = UserData.objects.create(f_auth=User.objects.get(id=auth['id']),
                                           f_role=Roles.objects.get(id=role['id']))
        return instance


class PasswordlessRegistration(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.CharField()

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise Exception('Email already exists')
        return email

    def validate_role(self, role):
        if not Roles.objects.filter(name=role).exists():
            raise Exception('Role doen\'t exist!')
        return role

    def create(self, validated_data):
        username = validated_data['first_name'][:1].lower() + validated_data['last_name'][:4].lower()
        if User.objects.filter(username=username).exists():
            username += str(len(User.objects.filter(username__contains=username).all()))

        user = User(username=username,
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    email=validated_data['email'])
        user.is_active = False
        user.set_unusable_password()
        user.save()
        UserData.objects.create(f_auth=user, f_role=Roles.objects.get(name=validated_data['role']))
        return user


class GoogleRegistration(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise Exception('Email already exists')
        return email

    def create(self, validated_data):
        user = User(username=validated_data['email'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    email=validated_data['email'])
        user.is_active = True
        user.set_unusable_password()
        user.save()
        UserData.objects.create(f_auth=user, f_role=Roles.objects.get(name='recruiter'))
        return user
