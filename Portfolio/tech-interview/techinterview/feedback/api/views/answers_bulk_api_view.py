from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from feedback.serializers import AnswersSerializer
from feedback.models import Answers
from techinterview.logger import log


class AnswersBulkAPIView(CreateAPIView):
    """Serve saving for many answers by one request"""
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

    def create(self, request, *args, **kwargs):
        query_list = []
        for question in request.data:
            try:
                query_list.append(Answers(answer_like=question.get('answer_like'),
                                          f_grade_id=question.get('grades'),
                                          f_question_id=question.get('questions'),
                                          f_interview_id=question.get('interviews')))
            except Answers.DoesNotExist as error:
                log.error(error)
                return Response('Grades does not exist', status=status.HTTP_400_BAD_REQUEST)

        serializer = AnswersSerializer(data=Answers.objects.bulk_create(query_list), many=True)
        serializer.is_valid()
        log.info('{} answered for poll'.format(request.user.username))
        log.debug('{} answers was saved'.format(len(query_list)))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
