from rest_framework.generics import ListCreateAPIView

from questions.models import Sections
from questions.serializers import SectionsSerializer
from techinterview.logger import log


class SectionsListAPIView(ListCreateAPIView):
    """handler for POST request"""
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer

    def create(self, request, *args, **kwargs):
        log.info('Section {} was created by {}'.format(request.data['name'], request.user.username))
        return super().create(request, *args, **kwargs)
