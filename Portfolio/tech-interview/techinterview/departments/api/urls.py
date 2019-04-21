from django.urls import re_path
from .views import DepartmentsByIdAPIView, DepartmentsListAPIView


urlpatterns = [
    re_path(r'(?P<pk>[\w\-]+)/?$', DepartmentsByIdAPIView.as_view(), name='departments-ById-API'),
    re_path(r'$', DepartmentsListAPIView.as_view(), name='departments-POST-API'),
]
