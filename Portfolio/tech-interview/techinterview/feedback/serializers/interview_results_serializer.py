from rest_framework import serializers


class InterviewResultsSerializer(serializers.Serializer):
    interview_id = serializers.IntegerField()
    total = serializers.CharField()
    levels = serializers.DictField()
