from rest_framework import serializers
from authorization.models import Permissions


class PermissionsSerializer(serializers.ModelSerializer):
    """PermissionsSerializer"""

    class Meta:
        """Meta"""
        model = Permissions
        fields = ('name', 'code_name')
