from django.http import HttpResponseRedirect


class AuthCheckMiddleware:

    open_api = ['/api/user/password_reset/', '/api/user/registration/', '/api/user/login/',
                '/api/user/password_reset/confirm/', '/password_reset/', '/password_reset/confirm/',
                '/login/', '/register/', '/api/user/login/', '/favicon.ico', '/api/user/google/']

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        if (request.user.is_authenticated is False and request.path in self.open_api) \
                or request.path.__contains__('api/user/password_reset/confirm') \
                or request.path.__contains__('api/user/verify_email/') \
                or request.path.__contains__('/password_reset/confirm/') \
                or request.path.__contains__('/api/user/google/'):
                return response

        elif request.user.is_authenticated and request.user.is_active and request.path not in self.open_api:
            return response

        elif request.user.is_authenticated and request.user.is_active and request.path in self.open_api:

            return HttpResponseRedirect('/home/')

        else:
            return HttpResponseRedirect('/login/')
