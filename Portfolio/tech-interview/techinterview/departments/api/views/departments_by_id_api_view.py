from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, serializers
from techinterview.logger import log

from departments.models import Departments
from departments.serializers import DepartmentsSerializer


class DepartmentsByIdAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()

    def get_serializer_class(self):
        raw = self.request.query_params.get('raw')
        if not raw:
            DepartmentsSerializer.to_representation = DepartmentsSerializer.custom_representation
        else:
            DepartmentsSerializer.to_representation = serializers.ModelSerializer.to_representation
        return DepartmentsSerializer

    def update(self, request, *args, **kwargs):
        department_data = Departments.objects.get(id=int(request.data.get('id')))
        department_data.name = request.data['name']
        department_data.questions.set(request.data['questions'])
        department_data.save()
        serializer = DepartmentsSerializer(department_data)
        log.info('Department {} was updated by {}'.format(serializer.data['name'],
                                                          request.user.username))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
