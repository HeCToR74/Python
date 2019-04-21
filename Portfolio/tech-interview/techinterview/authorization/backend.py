from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class CandidateAuthBackend(ModelBackend):
    """Allow candidates without password log in into system"""
    def authenticate(self, request, username=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if not user.has_usable_password():
                return user
            return super().authenticate(request=request, username=username, password=kwargs['password'])
        except User.DoesNotExist:
            return None
