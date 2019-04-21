from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'sections/?$', views.SectionsListAPIView.as_view(), name='sections-list-API'),
    re_path(r'sections/(?P<pk>[\w\-]+)/?$', views.SectionsByIdAPIView.as_view(), name='sections-ById-API'),
    re_path(r'stages/?$', views.StagesListAPIView.as_view(), name='stages-list-API'),
    re_path(r'stages/(?P<pk>[\w\-]+)/?$', views.StagesByIdAPIView.as_view(), name='stages-ById-API'),
    re_path(r'questions/?$', views.QuestionsListAPIView.as_view(), name='questions-list-API'),
    re_path(r'questions/(?P<pk>[\w\-]+)/?$', views.QuestionsByIdAPIView.as_view(), name='questions-ById-API'),
]
