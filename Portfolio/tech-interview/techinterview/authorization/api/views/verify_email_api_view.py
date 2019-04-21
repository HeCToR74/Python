import jwt
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import status
from rest_auth.registration.urls import VerifyEmailView
from django.contrib.auth import login as auth_login
from rest_framework.response import Response
from authorization.helper import *
from techinterview.logger import log


class VerifyEmailAPIView(VerifyEmailView):
    """VerifyEmailAPIView"""

    def get(self, request, token, *args, **kwargs):

        if token:
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

                user = User.objects.get(id=decoded['id'])
                user.is_active = True
                user.save()
                log.info('Email {} verified!'.format(user.email))
                auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')

                return redirect('/home/')

            except Exception as exp:
                log.error(exp)
                raise exp
            except jwt.ExpiredSignatureError:
                return Response('User was NOT confirm, because time went out ',
                                status=status.HTTP_409_CONFLICT)
