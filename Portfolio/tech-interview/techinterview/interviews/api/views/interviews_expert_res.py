from rest_framework import status
from rest_framework.generics import CreateAPIView
from interviews.models import InterviewsRes, Interviews
from techinterview.logger import log
from interviews.serializers import InterviewsSerializer, InterviewsResSerializer
from rest_framework.response import Response


class InterviewsExpertRes(CreateAPIView):
    """handler for Post request"""
    serializer_class = InterviewsResSerializer
    queryset = InterviewsRes.objects.all()