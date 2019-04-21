from rest_auth.views import LogoutView
from techinterview.logger import log


class LogoutAPIView(LogoutView):
    def post(self, request, *args, **kwargs):
        log.info('User {} sign out'.format(request.user.username))
        return super().post(request, *args, **kwargs)
