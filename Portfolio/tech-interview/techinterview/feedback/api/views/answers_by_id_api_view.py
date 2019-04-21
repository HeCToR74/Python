from rest_framework.generics import RetrieveUpdateDestroyAPIView
from feedback.serializers import AnswersSerializer
from feedback.models import Answers


class AnswersByIdAPIView(RetrieveUpdateDestroyAPIView):
    """ GET request for answers """

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
