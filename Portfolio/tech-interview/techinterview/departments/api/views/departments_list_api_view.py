from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from departments.models import Departments
from departments.serializers import DepartmentsSerializer
from questions.serializers import QuestionsSerializer
from questions.models import Questions
from techinterview.logger import log


class DepartmentsListAPIView(ListCreateAPIView):
    """handler for POST request"""
    DepartmentsSerializer.to_representation = DepartmentsSerializer.custom_representation
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

    def create(self, request, *args, **kwargs):
        """Get name from 'departments', serialize it and get full JSON"""
        list_questions = []
        for i in request.data['questions']:
            try:
                ser = QuestionsSerializer(Questions.objects.get(id=i))
                list_questions.append(ser.data)

            except Questions.DoesNotExist:
                log.error('Question with id={} doesn\'t exist'.format(i))
                return Response('question does not exist',
                                status=status.HTTP_400_BAD_REQUEST)

        request.data['questions'] = list_questions
        serializer = DepartmentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        log.info('Department {} was created by {}'.format(serializer.data.get('name'),
                                                          request.user.username))
        log.debug('Department was created with {} questions'.format(len(list_questions)))
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
