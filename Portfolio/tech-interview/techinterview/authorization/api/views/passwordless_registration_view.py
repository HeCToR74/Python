from rest_framework import status
from rest_auth.views import APIView
from authorization.serializers import PasswordlessRegistration
from rest_framework.response import Response
from authorization.helper import *
from authorization.token_mixin import TokenMixin
from techinterview.logger import log


class PaswordlessRegistrationView(APIView, TokenMixin):
    def post(self, request, role):
        request.data['role'] = role
        candidate = PasswordlessRegistration(data=request.data)
        candidate.is_valid(raise_exception=True)
        registered = candidate.create(candidate.validated_data)
        log.info('New {role} successfully registered as {username} by {recruiter}'
                 .format(role=role.title(),
                         username=registered.username,
                         recruiter=request.user.username))
        email_confirm_token_send(registered, self.get_token(user=registered))

        return Response(registered.id, status=status.HTTP_201_CREATED)