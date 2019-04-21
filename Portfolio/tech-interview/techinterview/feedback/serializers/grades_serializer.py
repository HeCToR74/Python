from rest_framework import serializers
from feedback.models import Grades


class GradesSerializer(serializers.ModelSerializer):
    # Serializer for Grades model

    class Meta:
        model = Grades
        fields = ('id', 'name', 'weight')
