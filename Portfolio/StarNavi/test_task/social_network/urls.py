from django.urls import path, include
from .views import PostView

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', PostView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))

]