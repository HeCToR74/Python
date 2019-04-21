from rest_framework.generics import RetrieveUpdateDestroyAPIView
from questions.models import Stages
from questions.serializers import StagesSerializer
from techinterview.logger import log


class StagesByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = Stages.objects.all()
    serializer_class = StagesSerializer

    def update(self, request, *args, **kwargs):
        log.info('Stage {} was updated by {}'.format(request.data['name'], request.user.username))
        return super().update(request, *args, **kwargs)
