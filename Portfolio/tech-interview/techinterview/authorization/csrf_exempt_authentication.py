from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
