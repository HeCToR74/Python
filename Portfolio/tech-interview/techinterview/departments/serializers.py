from rest_framework import serializers, permissions
from questions.models import Questions
from questions.serializers import QuestionsSerializer

from .models import Departments


class DepartmentsSerializer(serializers.ModelSerializer):
    """Serializer for Departments model"""
    permission_classes = [permissions.IsAuthenticated, ]
    # Get questions data using QuestionsSerializer in Questions app
    questions = QuestionsSerializer(many=True)
    original_representation = serializers.ModelSerializer.to_representation

    class Meta:
        model = Departments
        # without id because id specified in URL
        fields = ('id', 'name', 'questions')

    def custom_representation(self, instance):
        data = dict(super().to_representation(instance))
        new_data = {
            'id': data['id'],
            'name': data['name'],
            'sections': dict()
        }
        for question in data['questions']:
            serialized_question = {
                'id': question['id'],
                'name': question['name'],
                'hint': question['hint']
            }
            if new_data['sections'].get(question['stage']['section']['name'], False):
                if new_data['sections'][question['stage']['section']['name']].get(question['stage']['name'], False):
                    new_data['sections'][question['stage']['section']['name']][question['stage']['name']] += [serialized_question]
                else:
                    new_data['sections'][question['stage']['section']['name']][question['stage']['name']] = [serialized_question]
            else:
                new_data['sections'][question['stage']['section']['name']] = dict()
                new_data['sections'][question['stage']['section']['name']][question['stage']['name']] = [serialized_question]
        return new_data

    def create(self, validated_data):
        """Correct save data from serializer to DB"""
        instance = Departments.objects.create(name=validated_data.get('name'))
        for dict_questions in validated_data['questions']:
            dict_questions = dict(dict_questions)
            question = Questions.objects.get(name=dict_questions['name'])

            instance.questions.add(question)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        name = Departments.objects.get(name=validated_data.get('name'))
        for dict_questions in validated_data['questions']:
            dict_questions = dict(dict_questions)
            question = Questions.objects.get(name=dict_questions['name'])
            instance.questions.add(question)

            instance.save()
            name.save()
        return instance
