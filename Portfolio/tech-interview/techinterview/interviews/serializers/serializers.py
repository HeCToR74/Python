"""serialisers.py"""

# from .models import Interviews
from rest_framework import serializers
from django.contrib.auth.models import User
from authorization.serializers import UserDataSerializer
from authorization.models.user_data import UserData
from departments.serializers import DepartmentsSerializer
from departments.models.departments import Departments

from ..models import Interviews


class InterviewsSerializer(serializers.ModelSerializer):
    """InterviewsSerializer"""

    recruiter = UserDataSerializer(source='f_recruiter')
    candidate = UserDataSerializer(source='f_candidate')
    expert = UserDataSerializer(source='f_expert')
    department = DepartmentsSerializer(source='f_department')
    latitude = serializers.FloatField(allow_null=True)
    longitude = serializers.FloatField(allow_null=True)
    location = serializers.CharField(allow_null=True)

    class Meta:
        """Meta"""
        model = Interviews
        fields = ('id', 'recruiter', 'candidate', 'expert', 'department',
                  'created_date', 'status', 'interview_date', 'completion_date',
                  'latitude', 'longitude', 'location')
        extra_kwargs = {'id': {'read_only': False, 'required': False}, }

    def create(self, validated_data):
        validated_data['f_recruiter'] = dict(validated_data['f_recruiter'])
        validated_data['f_candidate'] = dict(validated_data['f_candidate'])
        validated_data['f_expert'] = dict(validated_data['f_expert'])
        validated_data['f_department'] = dict(validated_data['f_department'])

        recruiter = UserData.objects.get(f_auth=User.objects
                                         .get(username=validated_data.get('f_recruiter')
                                              .get('f_auth').get('username')))
        candidate = UserData.objects.get(f_auth=User.objects
                                         .get(username=validated_data.get('f_candidate')
                                              .get('f_auth').get('username')))
        expert = UserData.objects.get(f_auth=User.objects
                                      .get(username=validated_data.get('f_expert')
                                           .get('f_auth').get('username')))
        department = Departments.objects.get(name=validated_data.get('f_department')
                                             .get('name'))

        instance = Interviews.objects.create(f_recruiter=recruiter,
                                             f_candidate=candidate,
                                             f_expert=expert,
                                             f_department=department,
                                             interview_date=validated_data.get('interview_date'),
                                             created_date=validated_data.get('created_date'),
                                             latitude=validated_data.get('latitude'),
                                             longitude=validated_data.get('longitude'),
                                             location=validated_data.get('location'),
                                             status=validated_data.get('status'))
        return instance

    def update(self, instance, validated_data):
        department = Departments.objects.get(name=validated_data.get('name'))
        instance.f_department = department

        candidate = validated_data['f_candidate']['f_auth']['username']
        candidate = UserData.objects.get(f_auth=User.objects
                                         .get(username=validated_data.get('f_candidate')
                                              .get('f_auth').get('username')))
        instance.f_candidate = candidate

        expert = validated_data['f_expert']['f_auth']['username']
        expert = UserData.objects.get(f_auth=User.objects
                                      .get(username=validated_data.get('f_expert')
                                           .get('f_auth').get('username')))
        instance.f_expert = expert

        instance.save()

        return instance

    def validate_unique_users(self):
        """validate_unique_users"""

        if self.f_recruiter.id is self.f_candidate.id or \
                self.f_recruiter.id is self.f_expert.id or \
                self.f_candidate.id is self.f_expert.id:
            raise serializers.ValidationError('Users can not be the same.')