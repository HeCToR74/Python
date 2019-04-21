from rest_framework.generics import ListCreateAPIView

from questions.models import Questions
from questions.serializers import QuestionsSerializer
from techinterview.logger import log


class QuestionsListAPIView(ListCreateAPIView):
    """handler for POST request"""
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    def create(self, request, *args, **kwargs):
        log.info('Question {} was created by {}'.format(request.data['name'], request.user.username))
        return super().create(request, *args, **kwargs)
