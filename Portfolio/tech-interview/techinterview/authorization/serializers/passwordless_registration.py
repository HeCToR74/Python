from rest_framework import serializers
from django.contrib.auth.models import User

from authorization.models import UserData, Roles


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
