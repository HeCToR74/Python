from rest_framework.generics import RetrieveUpdateDestroyAPIView
from authorization.serializers import RolesSerializer
from authorization.models import Roles


class RolesByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
