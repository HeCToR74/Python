"""Interviews Views"""

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from interviews.models import Interviews
from interviews.serializers import InterviewsSerializer
from authorization.models import UserData
from authorization.serializers import UserSerializer, UserDataSerializer
from datetime import timedelta
import datetime
from django.contrib.auth.models import User


class InterviewsListForAnalytics(ListCreateAPIView):
    queryset = Interviews.objects.all()
    serializer_class = InterviewsSerializer

    def get(self, request, *args, **kwargs):
        def data_generation(dict1, dict2, dict3):
            data = [
                {
                    'label': 'somethingA',
                    'values': [{'x': key, 'y': dict1[key]} for key in dict1.keys()]
                },
                {
                    'label': 'somethingB',
                    'values': [{'x': key, 'y': dict2[key]} for key in dict2.keys()]
                },
                {
                    'label': 'somethingC',
                    'values': [{'x': key, 'y': dict3[key]} for key in dict3.keys()]
                }
            ]
            return data

        queryset = self.get_queryset()
        serializer_interwiew = InterviewsSerializer(queryset, many=True)
        recruiters = UserData.objects.filter(f_role_id=2)

        data = {}
        for recruiter in recruiters:
            list_created_date = []
            list_interview_date = []
            list_completion_date = []
            for item in serializer_interwiew.data:
                if item['recruiter']['auth']['id'] == recruiter.f_auth.id:
                    if item['created_date'] != None:
                        list_created_date.append(item['created_date'])
                    if item['interview_date'] != None:
                        list_interview_date.append(item['interview_date'])
                    if item['completion_date'] != None:
                        list_completion_date.append(item['completion_date'])

            now = datetime.datetime.now()
            list_created_date_7_days = {}
            list_interview_date_7_days = {}
            list_completion_date_7_days = {}
            for i in range(6,-1,-1):
                then = timedelta(days = i)
                list_created_date_7_days[(now - then).strftime("%d/%m/%Y")] = 0
                list_interview_date_7_days[(now - then).strftime("%d/%m/%Y")] = 0
                list_completion_date_7_days[(now - then).strftime("%d/%m/%Y")] = 0
                for item in list_created_date:
                    if (now-then).strftime("%Y-%m-%d") == item[0:10]:
                        list_created_date_7_days[(now - then).strftime("%d/%m/%Y")] += 1
                for item in list_interview_date:
                    if (now-then).strftime("%Y-%m-%d") == item[0:10]:
                        list_interview_date_7_days[(now - then).strftime("%d/%m/%Y")] += 1
                for item in list_completion_date:
                    if (now-then).strftime("%Y-%m-%d") == item[0:10]:
                        list_completion_date_7_days[(now - then).strftime("%d/%m/%Y")] += 1

            list_created_date_month = {}
            list_interview_date_month = {}
            list_completion_date_month = {}
            for i in range(4, -1, -1):
                then = timedelta(days=i * 7)

                list_then = [(now - timedelta(days=i*7-j)).strftime("%Y-%m-%d") for j in range(7)]
                str_date = (now - timedelta(days=i*7)).strftime("%d/%m/%Y") + "-" + (now - timedelta(days=i*7-6)).strftime("%d/%m/%Y")

                list_created_date_month[(now - then).strftime(str_date)] = 0
                list_interview_date_month[(now - then).strftime(str_date)] = 0
                list_completion_date_month[(now - then).strftime(str_date)] = 0
                for item in list_created_date:
                    if item[0:10] in list_then:
                        list_created_date_month[(now - then).strftime(str_date)] += 1
                for item in list_interview_date:
                    if item[0:10] in list_then:
                        list_interview_date_month[(now - then).strftime(str_date)] += 1
                for item in list_completion_date:
                    if item[0:10] in list_then:
                        list_completion_date_month[(now - then).strftime(str_date)] += 1

            list_created_date_year  = {}
            list_interview_date_year = {}
            list_completion_date_year = {}
            for i in range(12):
                then = now
                for j in range(12-i,1,-1):
                    then = (then.replace(day=1) - timedelta(days=1))
                list_created_date_year[then.strftime("%m/%Y")] = 0
                list_interview_date_year[then.strftime("%m/%Y")] = 0
                list_completion_date_year[then.strftime("%m/%Y")] = 0
                for item in list_created_date:
                    if then.strftime("%Y-%m") == item[0:7]:
                        list_created_date_year[then.strftime("%m/%Y")] += 1
                for item in list_interview_date:
                    if then.strftime("%Y-%m") == item[0:7]:
                        list_interview_date_year[then.strftime("%m/%Y")] += 1
                for item in list_completion_date:
                    if then.strftime("%Y-%m") == item[0:7]:
                        list_completion_date_year[then.strftime("%m/%Y")] += 1

            data[recruiter.f_auth.username] = {'day_data':
                                                   data_generation(list_created_date_7_days,
                                                                   list_interview_date_7_days,
                                                                   list_completion_date_7_days),
                                               'month_data':
                                                   data_generation(list_created_date_month,
                                                                   list_interview_date_month,
                                                                   list_completion_date_month),
                                               'year_data':
                                                   data_generation(list_created_date_year,
                                                                   list_interview_date_year,
                                                                   list_completion_date_year)}

        return Response({'all_data': data, 'username': request.user.username}, status=200)
