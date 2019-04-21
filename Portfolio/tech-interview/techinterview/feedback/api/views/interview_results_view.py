from rest_framework import status
from rest_framework.views import APIView

from feedback.serializers import InterviewResultsSerializer
from interviews.models import Interviews
from feedback.interview_results import InterviewResults

from rest_framework.response import Response


class InterviewResultsView(APIView):
    """ API for estimating candidate """

    def get(self, request, pk):
        """ Show validated grades information by id """
        try:
            int_res = InterviewResults(pk)
        except Interviews.DoesNotExist:
            return Response('Bad interview id', status=status.HTTP_400_BAD_REQUEST)
        serializer = InterviewResultsSerializer(int_res)
        return Response(serializer.data, status=status.HTTP_200_OK)
