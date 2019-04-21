from django.contrib.auth import authenticate, login as auth_login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from techinterview.logger import log


@csrf_protect
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        log.debug('username or password is none')
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(request, username=username, password=password)
    if not user:
        log.debug('Server refused credentials')
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    if user.is_active:
        log.info('User {} sign in'. format(user.get_username()))
        auth_login(request, user)

    return Response(status=HTTP_200_OK)
