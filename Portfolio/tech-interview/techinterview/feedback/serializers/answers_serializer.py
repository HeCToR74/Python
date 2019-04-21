from rest_framework import serializers

from interviews.serializers import InterviewsSerializer
from questions.serializers import QuestionsSerializer

from feedback.models import Answers, Grades
from questions.models import Questions
from interviews.models import Interviews
from .grades_serializer import GradesSerializer


class AnswersSerializer(serializers.ModelSerializer):
    # Serializer for Answers model
    grades = GradesSerializer(source='f_grade')
    interviews = InterviewsSerializer(source='f_interview')
    questions = QuestionsSerializer(source='f_question')

    class Meta:
        model = Answers
        fields = ('id', 'answer_like', 'grades', 'questions', 'interviews')

    def to_representation(self, instance):
        return {'answer_like': instance.answer_like,
                'grades': instance.f_grade_id,
                'questions': instance.f_question_id}

    def create(self, validated_data):
        validated_data['f_grade'] = dict(validated_data['f_grade'])
        grade = Grades.objects.get(name=validated_data.pop('f_grade').get('name'))

        validated_data['f_question'] = dict(validated_data['f_question'])
        question = Questions.objects.get(name=validated_data.pop('f_question').get('name'))

        validated_data['f_interview'] = dict(validated_data['f_interview'])
        interview = Interviews.objects.get(id=validated_data.get('f_interview').get('id'))

        instance = Answers.objects.create(answer_like=validated_data.get('answer_like'),
                                          f_grade=grade,
                                          f_question=question,
                                          f_interview=interview)
        return instance
