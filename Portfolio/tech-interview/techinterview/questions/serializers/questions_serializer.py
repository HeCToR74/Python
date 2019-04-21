from rest_framework import serializers
from questions.models import Stages, Questions
from .stages_serializer import StagesSerializer


class QuestionsSerializer(serializers.ModelSerializer):
    """Serializer for Questions model"""
    stage = StagesSerializer(source='f_stage')

    class Meta:
        model = Questions
        # without id because id specified in URL
        fields = ('id', 'name', 'hint', 'stage')

    def create(self, validated_data):
        """Correct save data from serializer to DB"""
        # validated_data['f_stage'] = dict(validated_data['f_stage'])
        stage = Stages.objects.get(name=validated_data.pop('f_stage').get('name'))
        instance = Questions.objects.create(name=validated_data.get('name'),
                                            hint=validated_data.get('hint'),
                                            f_stage=stage)
        return instance

    def update(self, instance, validated_data):
        stage = Stages.objects.get(name=validated_data.pop('f_stage').get('name'))

        instance.name = validated_data.get('name', instance.name)
        instance.hint = validated_data.get('hint', instance.hint)
        instance.f_stage = validated_data.get('stage', stage)
        instance.save()
        return instance
