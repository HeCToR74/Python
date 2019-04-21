from rest_framework.generics import RetrieveUpdateDestroyAPIView

from questions.models import Sections
from questions.serializers import SectionsSerializer
from techinterview.logger import log


class SectionsByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer

    def update(self, request, *args, **kwargs):
        log.info('Section {} was updated by {}'.format(request.data['name'], request.user.username))
        return super().update(request, *args, **kwargs)