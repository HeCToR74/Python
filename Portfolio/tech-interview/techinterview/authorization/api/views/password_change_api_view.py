from rest_auth.views import PasswordChangeView
from techinterview.logger import log


class PasswordChangeAPIView(PasswordChangeView):
    """PasswordChangeAPIView"""
    def post(self, request, *args, **kwargs):
        thread = super().post(request, *args, **kwargs)
        log.info('User {} changed the password'.format(request.user.username))
        return thread
