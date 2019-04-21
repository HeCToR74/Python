from rest_framework import serializers
from django.contrib.auth.models import User
from authorization.models import UserData, Roles


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
