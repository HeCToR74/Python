from rest_framework.generics import RetrieveUpdateDestroyAPIView
from authorization.models import Permissions
from authorization.serializers import PermissionsSerializer


class PermissionsByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
