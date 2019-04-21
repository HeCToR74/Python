"""Interviews URLs"""

from django.urls import re_path
from .views import *


urlpatterns = [
    re_path(r'^link_interview/(?P<token>[\w\.\-\%_\&\;]+)', LinkInterviewAPIView.as_view(), name='interview-candidate-letter'),
    re_path(r'^link_interview_exp/(?P<token>[\w\.\-\%_\&\;]+)', LinkInterviewExpertAPIView.as_view(), name='interview-expert-letter'),
    re_path(r'^analytics/$', InterviewsListForAnalytics.as_view(), name='interviews-analytics-API'),
    re_path(r'^res/(?P<pk>[\w\-]+)/?$', InterviewsExpertRes.as_view(), name='Interviews-Exert-Res-API'),
    re_path(r'(?P<pk>[\w\-]+)/?$', InterviewsByIdAPIView.as_view(), name='interviews-ById-API'),
    re_path(r'$', InterviewsListAPIViews.as_view(), name='interviews-list-API'),
]
