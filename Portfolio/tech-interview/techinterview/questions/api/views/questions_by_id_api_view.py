from rest_framework.generics import RetrieveUpdateDestroyAPIView

from questions.models import Questions
from questions.serializers import QuestionsSerializer
from techinterview.logger import log


class QuestionsByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    def update(self, request, *args, **kwargs):
        log.info('Question {} was updated by {}'.format(request.data['name'], request.user.username))
        return super().update(request, *args, **kwargs)
