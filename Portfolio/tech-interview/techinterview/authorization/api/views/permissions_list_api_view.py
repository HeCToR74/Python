from rest_framework.generics import ListCreateAPIView
from authorization.models import Permissions
from authorization.serializers import PermissionsSerializer


class PermissionsListAPIView(ListCreateAPIView):
    """handler for POST request"""

    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
