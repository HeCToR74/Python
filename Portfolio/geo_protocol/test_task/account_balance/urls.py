from django.urls import path
from .views import CustomerView

app_name = "customeres"

customeres = [
    path('customeres/', CustomerView.as_view()),
]