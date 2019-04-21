from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from feedback.serializers import GradesSerializer, CommentsSerializer
from questions.serializers import QuestionsSerializer
from interviews.serializers import InterviewsSerializer

from feedback.models import Grades, Comments
from questions.models import Questions
from interviews.models import Interviews

from rest_framework.response import Response


class CommentsListAPIView(ListCreateAPIView):
    """ POST request for comments """

    serializer_class = CommentsSerializer

    def get_queryset(self):
        interview_id = self.request.query_params.get('interview_id')
        queryset = Comments.objects.filter(f_interview_id=interview_id) if interview_id else Comments.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        questions_list = super().list(request, *args, **kwargs)
        questions_dict = {
            question['questions']: {'validated_grade': question['validated_grade'], 'comment': question['comment']}
            for question in questions_list.data}
        return Response(questions_dict, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        try:
            ques = QuestionsSerializer(Questions.objects.get(id=request.data['questions']))
            grad = GradesSerializer(Grades.objects.get(id=request.data['grades']))
            inter = InterviewsSerializer(Interviews.objects.get(id=request.data['interviews']))
        except Grades.DoesNotExist:
            return Response('Status does not exist', status=status.HTTP_400_BAD_REQUEST)
        except Questions.DoesNotExist:
            return Response('Status does not exist', status=status.HTTP_400_BAD_REQUEST)
        except Interviews.DoesNotExist:
            return Response('Status does not exist', status=status.HTTP_400_BAD_REQUEST)

        request.data['questions'] = ques.data
        request.data['grades'] = grad.data
        request.data['interviews'] = inter.data

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
