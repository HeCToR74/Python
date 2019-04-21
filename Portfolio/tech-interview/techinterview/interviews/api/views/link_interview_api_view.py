from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from interviews.api.interview_email import *
from techinterview.logger import log


class LinkInterviewAPIView(APIView):

    def get(self, request, token, *args, **kwargs):
        if token:
            try:
                id = deanc(token)
                return redirect('/test/{}'.format(id))
            except Exception as error:
                log.error(error)
                raise error
            except jwt.ExpiredSignatureError:
                return Response('User was NOT confirm, because time went out ',
                                status=status.HTTP_409_CONFLICT)
