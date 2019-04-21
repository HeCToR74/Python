from django.contrib.auth.models import User
from rest_framework import status
from rest_auth.registration.urls import RegisterView
from rest_auth.registration.app_settings import RegisterSerializer, register_permission_classes
from rest_auth.models import TokenModel
from rest_framework.response import Response
from authorization.helper import *
from authorization.token_mixin import TokenMixin
from techinterview.logger import log


class RegistrationAPIView(RegisterView, TokenMixin):
    """RegistrationAPIView"""

    serializer_class = RegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel

    def create(self, request, *args, **kwargs):
        """rewrite method create"""

        if User.objects.filter(username=request.data['username']).exists():
            return Response({
                'error': 'LOGIN',
                'message': 'User was NOT created, because LOGIN is exists'
            }, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=request.data['email']).exists():
            return Response({
                'error': 'EMAIL',
                'message': 'User was NOT created, because EMAIL is exists',
            }, status=status.HTTP_409_CONFLICT)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        email_confirm_token_send(user, self.get_token(user=user))
        log.info(msg='User {} was registered'.format(user.username))
        request.session.flush()

        return Response(status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """rewrite method perform_create"""

        user = serializer.save(self.request)
        user = set_first_last_role(user, self.request)
        return user
