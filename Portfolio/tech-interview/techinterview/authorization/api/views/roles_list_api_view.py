from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from authorization.models import Permissions
from authorization.serializers import PermissionsSerializer, RolesSerializer
from rest_framework.response import Response
from authorization.helper import *


class RolesListAPIView(ListCreateAPIView):
    """handler for POST request"""

    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

    def create(self, request, *args, **kwargs):
        """Get name from 'roles', serialize it and get full JSON"""

        list_permissions = []
        for permission in request.data['permissions']:
            try:
                permission_ser = PermissionsSerializer(Permissions.objects.get(name=permission))
                list_permissions.append(permission_ser.data)

                request.data['permissions'] = list_permissions
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)

                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

            except Permissions.DoesNotExist:
                return Response('Permission does not exist', status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RolesSerializer(queryset, many=True)
        return Response(serializer.data)
