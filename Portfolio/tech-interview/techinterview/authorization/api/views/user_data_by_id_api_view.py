from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from authorization.serializers import UserDataSerializer
from rest_framework.status import *
from rest_framework.response import Response
from authorization.helper import *
from authorization.models import UserData


class UserDataByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def put(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if 'first_name' in request.data:
            user.first_name = request.data['first_name']
        if 'last_name' in request.data:
            user.last_name = request.data['last_name']
        if 'avatar' in request.data:
            user_data = UserData.objects.get(f_auth_id=user.id)
            user_data.avatar = request.data['avatar']
            user_data.save()
        user.save()
        return Response(status=HTTP_200_OK)
