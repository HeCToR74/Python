from django.urls import path
from .views import UserView

urlpatterns = [
    path('v1/users/', UserView.as_view()),
    path('v1/users/<int:pk>', UserView.as_view())
]