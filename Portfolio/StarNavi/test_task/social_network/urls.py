from django.urls import path
from .views import PostView, UserView

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('users/', UserView.as_view()),
]