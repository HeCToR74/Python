from django.urls import re_path
from .views import \
    GradesByIdAPIView, \
    GradesListAPIView, \
    AnswersByIdAPIView,\
    AnswersListAPIView, \
    CommentsByIdAPIView, \
    CommentsListAPIView, \
    AnswersBulkAPIView, \
    CommentsBulkAPIView, \
    InterviewResultsView

urlpatterns = [
    re_path(r'grades/(?P<pk>[\w\-]+)/?$',
            GradesByIdAPIView.as_view(),
            name='grades-ById-api'),
    re_path(r'grades/?$',
            GradesListAPIView.as_view(),
            name='grades-list-api'),
    re_path(r'answers/bulk?$',
            AnswersBulkAPIView.as_view(),
            name='answers-bulk-api'),
    re_path(r'answers/(?P<pk>[\w\-]+)/?$',
            AnswersByIdAPIView.as_view(),
            name='answers-ById-api'),
    re_path(r'answers/?$',
            AnswersListAPIView.as_view(),
            name='answers-list-api'),
    re_path(r'comments/bulk?$',
            CommentsBulkAPIView.as_view(),
            name='answers-bulk-api'),
    re_path(r'comments/?$',
            CommentsListAPIView.as_view(),
            name='comments-list-api'),
    re_path(r'comments/(?P<pk>[\w\-]+)/?$',
            CommentsByIdAPIView.as_view(),
            name='comments-ById-api'),
    re_path(r'results/(?P<pk>[\w\-]+)/?$',
            InterviewResultsView.as_view(),
            name='comments-api'),
]
