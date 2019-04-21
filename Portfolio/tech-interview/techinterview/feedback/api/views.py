import datetime
from rest_framework import status, serializers
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView

from feedback.serializers import \
    GradesSerializer, \
    AnswersSerializer, \
    CommentsSerializer, \
    InterviewResultsSerializer
from questions.serializers import QuestionsSerializer
from interviews.serializers import InterviewsSerializer
from feedback.models import Grades, Answers, Comments
from questions.models import Questions
from interviews.models import Interviews
from feedback.interview_results import InterviewResults

from rest_framework.response import Response


class GradesByIdAPIView(RetrieveUpdateDestroyAPIView):
    """ GET request for grades """
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer



class GradesListAPIView(ListCreateAPIView):
    """ POST request for grades """

    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

    def list(self, request, *args, **kwargs):
        original_list = super().list(request, *args, **kwargs)
        if self.request.query_params.get('dict', False):
            grades_dict = {grade['id']: grade['name'] for grade in original_list.data}
            return Response(grades_dict, status=status.HTTP_200_OK)
        return original_list


class AnswersByIdAPIView(RetrieveUpdateDestroyAPIView):
    """ GET request for answers """

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class AnswersListAPIView(ListCreateAPIView):
    """ POST request for answers """

    serializer_class = AnswersSerializer

    def get_queryset(self):
        interview_id = self.request.query_params.get('interview_id')
        queryset = Answers.objects.filter(f_interview_id=interview_id) \
            if interview_id else Answers.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        questions_list = super().list(request, *args, **kwargs)
        questions_dict = {question['questions']: {
            'answer_like': question['answer_like'],
            'grade': question['grades']}
            for question in questions_list.data}
        return Response(questions_dict, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        try:
            grad = GradesSerializer(Grades.objects.get(id=request.data['grades']))
            ques = QuestionsSerializer(Questions.objects.get(id=request.data['questions']))
            inter = InterviewsSerializer(Interviews.objects.get(id=request.data['interviews']))
        except Grades.DoesNotExist:
            return Response('Grades does not exist', status=status.HTTP_400_BAD_REQUEST)
        except Questions.DoesNotExist:
            return Response('Questions does not exist', status=status.HTTP_400_BAD_REQUEST)
        except Interviews.DoesNotExist:
            return Response('Interviews does not exist', status=status.HTTP_400_BAD_REQUEST)

        request.data['grades'] = grad.data
        request.data['questions'] = ques.data
        request.data['interviews'] = inter.data

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AnswersBulkAPIView(CreateAPIView):
    """Serve saving for many answers by one request"""
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

    def create(self, request, *args, **kwargs):
        query_list = []
        for question in request.data:
            try:
                query_list.append(Answers(answer_like=question.get('answer_like'),
                                          f_grade_id=question.get('grades'),
                                          f_question_id=question.get('questions'),
                                          f_interview_id=question.get('interviews')))
            except Answers.DoesNotExist:
                return Response('Grades does not exist', status=status.HTTP_400_BAD_REQUEST)

        serializer = AnswersSerializer(data=Answers.objects.bulk_create(query_list), many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentsByIdAPIView(RetrieveUpdateDestroyAPIView):
    """ GET request for comments """

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentsBulkAPIView(CreateAPIView):
    """Serve saving for many comments by one request"""
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        try:
            if len(Answers.objects.filter(f_interview_id=request.data[0].get('interview'))) == len(request.data):
                current_interview = Interviews.objects.get(id=request.data[0].get('interview'))
                current_interview.status = 'completed'
                current_interview.completion_date = datetime.date.today()
                current_interview.save()
        except IndexError:
            return response
        except Interviews.DoesNotExist:
            return response
        return response

    def create(self, request, *args, **kwargs):
        query_list = []
        for comment in request.data:
            try:
                query_list.append(Comments(comment=comment.get('comment') if comment.get('comment') != '' else None,
                                           f_grade_id=comment.get('grade'),
                                           f_interview_id=comment.get('interview'),
                                           f_question_id=comment.get('question')))

            except Answers.DoesNotExist:
                return Response('Grades does not exist', status=status.HTTP_400_BAD_REQUEST)

        serializer = CommentsSerializer(data=Comments.objects.bulk_create(query_list), many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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


class InterviewResultsView(APIView):
    """ API for estimating candidate """

    def get(self, request, pk):
        """ Show validated grades information by id """
        try:
            int_res = InterviewResults(pk)
        except Interviews.DoesNotExist:
            return Response('Bad interview id', status=status.HTTP_400_BAD_REQUEST)
        serializer = InterviewResultsSerializer(int_res)
        return Response(serializer.data, status=status.HTTP_200_OK)
