"""AUTH Views"""

import jwt
import datetime
from django.contrib.auth.models import User, AnonymousUser
from django.dispatch import receiver
from django.shortcuts import redirect
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_auth.views import LogoutView, PasswordChangeView, APIView
from rest_auth.registration.urls import RegisterView, VerifyEmailView
from rest_auth.registration.app_settings import RegisterSerializer, register_permission_classes
from rest_auth.models import TokenModel
from authorization.models import Roles, Permissions, UserData
from authorization.serializers import PermissionsSerializer, \
    RolesSerializer, UserSerializer, UserDataSerializer, PasswordlessRegistration, GoogleRegistration
from interviews.models import Interviews
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .helper import *
from authorization.token_mixin import TokenMixin
from google.oauth2 import id_token
from google.auth.transport import requests
from authorization.csrf_exempt_authentication import CsrfExemptAuthentication
from rest_framework.authentication import BasicAuthentication


@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    """password_reset_token_created function"""

    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url':
            "http://127.0.0.1:8000/password_reset/confirm/{}".format(reset_password_token.key)
    }

    subject = 'Contact Form Received'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [reset_password_token.user.email]

    email_html_message = get_template('mail_send.html').render(context)
    return send_mail(subject, email_html_message, from_email, to_email)


@csrf_protect
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)

    if user.is_active:
        auth_login(request, user)

    return Response(status=HTTP_200_OK)


class LogoutAPIView(LogoutView):
    pass


class UserDetailsAPIView(ListAPIView):
    """UserDetailsAPIView"""

    serializer_class = UserDataSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        role = self.request.query_params.get('role')
        queryset = self.model.objects.filter(f_role__name=role) \
            if role else self.model.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):

        auth = UserData.objects.get(f_auth_id=request.user.id)
        role = Roles.objects.get(id=auth.f_role_id)

        if self.request.query_params.get('role'):
            return super().get(request, *args, **kwargs)

        try:
            interviews_recruiter = \
                len(Interviews.objects.filter(status='scheduled', f_recruiter_id=auth.id))
        except Interviews.DoesNotExist:
            interviews_recruiter = False

        try:
            interviews_candidate = \
                Interviews.objects.filter(status='scheduled', f_candidate_id=auth.id)
            if len(interviews_candidate):
                interviews_candidate = interviews_candidate[0].id
        except Interviews.DoesNotExist:
            interviews_candidate = False

        try:
            interviews_expert = Interviews.objects.filter(status='scheduled', f_expert_id=auth.id)
            if len(interviews_expert):
                interviews_expert = interviews_expert[0].id
        except Interviews.DoesNotExist:
            interviews_expert = False

        user = {
            'id': request.user.id,
            'login': request.user.username,
            'first': request.user.first_name,
            'last': request.user.last_name,
            'email': request.user.email,
            'role': role.name,
            'avatar': auth.avatar,
            'interviews_recruiter': interviews_recruiter,
            'interviews_candidate': interviews_candidate,
            'interviews_expert': interviews_expert,
        }
        return Response({'user': user}, status=status.HTTP_200_OK)


class PasswordChangeAPIView(PasswordChangeView):
    """PasswordChangeAPIView"""
    pass


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
        # headers = self.get_success_headers(serializer.data)

        email_confirm_token_send(user, self.get_token(user=user))
        request.session.flush()
        return Response(status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """rewrite method perform_create"""

        user = serializer.save(self.request)
        # if user:
        #     try:
        #         payload = {}
        #         payload['id'] = user.id
        #         payload['exp'] = datetime.datetime.now() + datetime.timedelta(days=3)
        #         self.token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        #     except Exception as exp:
        #         raise exp

        # complete_signup(self.request._request, user, None, None)
        user = set_first_last_role(user, self.request)
        return user


class VerifyEmailAPIView(VerifyEmailView):
    """VerifyEmailAPIView"""

    def get(self, request, token, *args, **kwargs):

        if token:
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

                user = User.objects.get(id=decoded['id'])
                user.is_active = True
                user.save()

                if user.is_active:
                    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')

                return redirect('/home/')

            except Exception as exp:
                raise exp
            except jwt.ExpiredSignatureError:
                return Response('User was NOT confirm, because time went out ',
                                status=status.HTTP_409_CONFLICT)


class UserDataByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def put(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        a = request.data
        print(a.keys())
        if request.data['avatar'] != 'None':
            userData = UserData.objects.get(f_auth_id=user.id)
            userData.avatar = request.data['avatar']
            userData.save()
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.save()
        return Response(status=HTTP_200_OK)


class UserDataListAPIView(ListCreateAPIView):
    """handler for POST request"""

    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def create(self, request, *args, **kwargs):

        try:
            auth = UserSerializer(User.objects.get(username=request.data['auth']))
            role = RolesSerializer(Roles.objects.get(id=request.data['role']))

            request.data['auth'] = auth.data
            request.data['role'] = role.data
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except User.DoesNotExist:
            return Response('User does not exist!', status=status.HTTP_400_BAD_REQUEST)
        except Roles.DoesNotExist:
            return Response('Roles does not exist!', status=status.HTTP_400_BAD_REQUEST)


class RolesByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


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


class PermissionsByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer


class PermissionsListAPIView(ListCreateAPIView):
    """handler for POST request"""

    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer


class PaswordlessRegistrationView(APIView, TokenMixin):
    def post(self, request, role):
        request.data['role'] = role
        candidate = PasswordlessRegistration(data=request.data)
        candidate.is_valid(raise_exception=True)
        registered = candidate.create(candidate.validated_data)

        email_confirm_token_send(registered, self.get_token(user=registered))

        return Response(registered.id, status=status.HTTP_201_CREATED)


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
