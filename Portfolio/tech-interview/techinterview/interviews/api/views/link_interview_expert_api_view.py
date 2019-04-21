from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from interviews.api.interview_email import *
from techinterview.logger import log


class LinkInterviewExpertAPIView(APIView):

    def get(self, request, token, *args, **kwargs):
        if token:
            try:
                decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                return redirect('/expert/{}'.format(decoded['id']))
            except Exception as e:
                log.error(e)
                raise e
            except jwt.ExpiredSignatureError:
                return Response('User was NOT confirm, because time went out ',
                                status=status.HTTP_409_CONFLICT)
