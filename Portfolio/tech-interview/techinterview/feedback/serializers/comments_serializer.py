from rest_framework import serializers

from interviews.serializers import InterviewsSerializer
from questions.serializers import QuestionsSerializer

from feedback.models import Comments, Grades
from questions.models import Questions
from interviews.models import Interviews
from .grades_serializer import GradesSerializer


class CommentsSerializer(serializers.ModelSerializer):
    # Serializer for Comments model

    # Get questions, grades, interviews data using QuestionsSerializer, GradesSerializer and InterviewsSerializer
    questions = QuestionsSerializer(source='f_question')
    grades = GradesSerializer(source='f_grade')
    interviews = InterviewsSerializer(source='f_interview')

    class Meta:
        model = Comments
        fields = ('id', 'questions', 'grades', 'comment', 'interviews')

    def to_representation(self, instance):
        return {'validated_grade': instance.f_grade_id,
                'comment': instance.comment,
                'questions': instance.f_question_id}

    def create(self, validated_data):
        validated_data['f_question'] = dict(validated_data['f_question'])
        questions = Questions.objects.get(name=validated_data.pop('f_question').get('name'))
        validated_data['f_grade'] = dict(validated_data['f_grade'])
        grades = Grades.objects.get(name=validated_data.pop('f_grade').get('name'))
        validated_data['f_interview'] = dict(validated_data['f_interview'])
        interview = Interviews.objects.get(id=validated_data.pop('f_interview').get('id'))
        instance = Comments.objects.create(f_question=questions,
                                           f_grade=grades,
                                           comment=validated_data.get('comment'),
                                           f_interview=interview
                                           )
        return instance
