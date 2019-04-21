from ..models import InterviewsRes, Interviews
from rest_framework import serializers
from django.contrib.auth.models import User
from .serializers import InterviewsSerializer


class InterviewsResSerializer(serializers.ModelSerializer):
    """InterviewsResSerializer"""

    class Meta:
        model = InterviewsRes
        fields = ('summary_of_qualification', 'years_of_experience',
                  'level', 'level_com', 'gaps', 'gaps_com', 'technical_english',
                  'technical_english_com', 'high_potential',
                  'high_potential_com', 'potentially_hire',
                  'potentially_hire_com', 'f_interview_id')

        def create(self, validated_data):
            validated_data['summary_of_qualification'] = dict(validated_data['summary_of_qualification'])
            validated_data['years_of_experience'] = dict(validated_data['years_of_experience'])
            validated_data['level'] = dict(validated_data['level'])
            validated_data['level_com'] = dict(validated_data['level_com'])
            validated_data['gaps'] = dict(validated_data['gaps'])
            validated_data['gaps_com'] = dict(validated_data['gaps_com'])
            validated_data['technical_english'] = dict(validated_data['technical_english'])
            validated_data['technical_english_com'] = dict(validated_data['technical_english_com'])
            validated_data['high_potential'] = dict(validated_data['high_potential'])
            validated_data['high_potential_com'] = dict(validated_data['high_potential_com'])
            validated_data['potentially_hire'] = dict(validated_data['potentially_hire'])
            validated_data['potentially_hire_com'] = dict(validated_data['potentially_hire_com'])
            validated_data['f_interview_id'] = InterviewsSerializer(data=Interviews.objects.get(pk=validated_data['f_interview_id']))


            instance = InterviewsRes.objects.create(**validated_data)
            return instance