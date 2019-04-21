from rest_framework.generics import RetrieveUpdateDestroyAPIView
from feedback.serializers import CommentsSerializer
from feedback.models import Comments


class CommentsByIdAPIView(RetrieveUpdateDestroyAPIView):
    """ GET request for comments """

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
