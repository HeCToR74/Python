from rest_auth.views import APIView
from rest_auth.registration.app_settings import register_permission_classes
from authorization.serializers import GoogleRegistration
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.status import *
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests
from authorization.csrf_exempt_authentication import CsrfExemptAuthentication
from rest_framework.authentication import BasicAuthentication


class GoogleAuthorization(APIView):
    authentication_classes = (CsrfExemptAuthentication, BasicAuthentication)
    permission_classes = register_permission_classes()

    def post(self, request):
        token = request.POST.get('idtoken')
        id_info = id_token.verify_oauth2_token(token, requests.Request())
        user = authenticate(username=id_info.get('email'))
        if not user:
            google_user = GoogleRegistration(data={'first_name': id_info.get('given_name'),
                                                   'last_name': id_info.get('family_name'),
                                                   'email': id_info.get('email')})
            google_user.is_valid()
            user = google_user.create(google_user.validated_data)

        auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return Response('Success', status=HTTP_200_OK)
