from django.conf import settings
import jwt

import datetime


class TokenMixin:
    def get_token(self, user):
        return jwt.encode(self.__generate_payload(user), settings.SECRET_KEY, algorithm='HS256')

    def __generate_payload(self, user):
        return {'id': user.id,
                'exp': datetime.datetime.now() + datetime.timedelta(days=3)}
