from rest_framework import serializers
from questions.models import Sections, Stages
from .sections_serializer import SectionsSerializer


class StagesSerializer(serializers.ModelSerializer):
    """Serializer for Stages model"""
    section = SectionsSerializer(source='f_section')

    class Meta:
        model = Stages
        # without id because id specified in URL
        fields = ('id', 'name', 'section')

    def create(self, validated_data):
        """Correct save data from serializer to DB"""
        validated_data['f_section'] = dict(validated_data['f_section'])
        section = Sections.objects.get(name=validated_data.pop('f_section').get('name'))
        instance = Stages.objects.create(name=validated_data.get('name'),
                                         f_section=section)
        return instance
