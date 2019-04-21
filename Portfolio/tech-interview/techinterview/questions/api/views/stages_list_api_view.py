from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from questions.models import Sections, Stages
from questions.serializers import SectionsSerializer, StagesSerializer
from rest_framework.response import Response
from techinterview.logger import log


class StagesListAPIView(ListCreateAPIView):
    """handler for POST request"""

    queryset = Stages.objects.all()
    serializer_class = StagesSerializer

    def create(self, request, *args, **kwargs):
        """Get name from 'section', serialize it and get full JSON"""

        try:
            ser = SectionsSerializer(Sections.objects.get(id=request.data['section']))
        except Sections.DoesNotExist as error:
            log.error(error)
            return Response('Section does not exist',
                            status=status.HTTP_400_BAD_REQUEST)

        request.data['section'] = ser.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        log.info('Stage {} was created by {}'.format(serializer.data['name'], request.user.username))
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
