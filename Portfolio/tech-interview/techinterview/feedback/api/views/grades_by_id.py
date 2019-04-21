from rest_framework.generics import RetrieveUpdateDestroyAPIView
from feedback.serializers import GradesSerializer
from feedback.models import Grades
from techinterview.logger import log


class GradesByIdAPIView(RetrieveUpdateDestroyAPIView):
    """ GET request for grades """
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

    def update(self, request, *args, **kwargs):
        log.info('Grade with id: {} was updated by {}'.format(request.data.get('id'),
                                                              request.user.username))
        return super().update(request, *args, **kwargs)

