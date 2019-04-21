from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


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
