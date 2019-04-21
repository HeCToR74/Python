from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from feedback.serializers import GradesSerializer
from feedback.models import Grades
from techinterview.logger import log


class GradesListAPIView(ListCreateAPIView):
    """ POST request for grades """

    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

    def list(self, request, *args, **kwargs):
        original_list = super().list(request, *args, **kwargs)
        if self.request.query_params.get('dict', False):
            grades_dict = {grade['id']: grade['name'] for grade in original_list.data}
            return Response(grades_dict, status=status.HTTP_200_OK)
        return original_list

    def create(self, request, *args, **kwargs):
        log.info('New grade was created by {}'.format(request.user.username))
        return super().create(request, *args, **kwargs)
