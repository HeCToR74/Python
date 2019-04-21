import datetime
from rest_framework import status
from rest_framework.generics import CreateAPIView

from feedback.serializers import CommentsSerializer

from feedback.models import Answers, Comments
from interviews.models import Interviews

from rest_framework.response import Response
from techinterview.logger import log


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

            except Answers.DoesNotExist as error:
                log.error(error)
                return Response('Grades does not exist', status=status.HTTP_400_BAD_REQUEST)

        serializer = CommentsSerializer(data=Comments.objects.bulk_create(query_list), many=True)
        serializer.is_valid()
        log.info('{} was validate candidate\'s answers'.format(request.user.username))
        log.debug('{} comments was saved'.format(len(query_list)))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
