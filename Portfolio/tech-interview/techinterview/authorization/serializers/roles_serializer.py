from rest_framework import serializers
from authorization.models import Roles, Permissions
from authorization.serializers import PermissionsSerializer


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
