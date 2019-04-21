from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from interviews.models import Interviews
from interviews.pagination import InterviewsPagination
from interviews.serializers import InterviewsSerializer
from departments.models.departments import Departments
from authorization.models import UserData
from authorization.serializers import UserDataSerializer
from departments.serializers import DepartmentsSerializer
from interviews.api.interview_email import *
import datetime
from techinterview.logger import log


class InterviewsListAPIViews(ListCreateAPIView):
    """handler for POST request"""

    queryset = Interviews.objects.all()
    serializer_class = InterviewsSerializer
    pagination_class = InterviewsPagination

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)

        if self.request.query_params.get('list', False):
            for element in res.data.get('results'):
                def get_username(obj):
                    return obj['auth']['first_name'] + ' ' + obj['auth']['last_name'] + ' '

                element['candidate_email'] = element['candidate']['auth']['email']
                element['expert_email'] = element['expert']['auth']['email']
                element['candidate'] = get_username(element['candidate'])
                element['expert'] = get_username(element['expert'])
                del element['recruiter']
                del element['department']
                del element['created_date']
                del element['completion_date']
        return res

    def create(self, request, *args, **kwargs):
        try:
            recruiter = UserDataSerializer(UserData.objects.get(f_auth_id=self.request.user.id))
            candidate = UserDataSerializer(UserData.objects.get(f_auth_id=request.data['candidate']))
            expert = UserDataSerializer(UserData.objects.get(f_auth_id=request.data['expert']))
            department = DepartmentsSerializer(Departments.objects
                                               .get(id=request.data['department']))
            department.to_representation = department.original_representation

            if recruiter.data['auth']['id'] == candidate.data['auth']['id'] or \
                    recruiter.data['auth']['id'] == expert.data['auth']['id'] or \
                    candidate.data['auth']['id'] == expert.data['auth']['id']:
                return Response('Users can not be the same!', status=status.HTTP_400_BAD_REQUEST)

            if recruiter.data['role']['name'] != 'recruiter':
                log.error('User {} with role {} tries to create interview'
                          .format(request.user.username, recruiter.data['role']['name']))
                return Response('You aren\'t recruiter!', status=status.HTTP_400_BAD_REQUEST)

        except UserData.DoesNotExist as error:
            log.error(error)
            return Response('User does not exist!', status=status.HTTP_400_BAD_REQUEST)
        except Departments.DoesNotExist as error:
            log.error(error)
            return Response('Department does not exist!', status=status.HTTP_400_BAD_REQUEST)

        request.data['recruiter'] = recruiter.data
        request.data['candidate'] = candidate.data
        request.data['expert'] = expert.data
        request.data['department'] = department.data
        request.data['created_date'] = datetime.date.today()
        request.data['status'] = 'scheduled'

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        log.info(self.perform_create(serializer))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        instance = serializer.save()
        if serializer:
            token = anc(serializer.data['id'])
            send_email_cand(token, serializer.data)
            token = create_token(serializer.data['id'])
            send_email_expert(token, serializer.data)
        return instance
