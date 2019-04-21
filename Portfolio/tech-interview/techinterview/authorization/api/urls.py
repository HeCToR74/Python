from django.urls import re_path, include
import authorization.api.views as views
from django_rest_passwordreset.urls import *

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # URLs that do not require a session or valid token7
    re_path(r'^password_reset/', include('django_rest_passwordreset.urls',
                                         namespace='password_reset')),
    re_path(r'^login/$', views.login),

    re_path(r'^google/$', csrf_exempt(views.GoogleAuthorization.as_view())),
    # URLs that require a user to be logged in with a valid session / token.
    re_path(r'^verify_email/(?P<token>[\w\.\-\%_\&\;]+)', views.VerifyEmailAPIView.as_view()),
    re_path(r'^logout/$', views.LogoutAPIView.as_view(), name='rest_logout'),

    re_path(r'^user/$', views.UserDetailsAPIView.as_view(),
            name='rest_user_details'),
    re_path(r'^password/change/$', views.PasswordChangeAPIView.as_view(),
            name='rest_password_change'),
    re_path(r'^registration/(?P<role>[\w\-]+)/?$', views.PaswordlessRegistrationView.as_view(),
            name='rest_register_2'),
    re_path(r'^registration/$', views.RegistrationAPIView.as_view(),
            name='rest_register'),
    re_path(r'^profile/$', views.UserDataByIdAPIView.as_view()),

]


