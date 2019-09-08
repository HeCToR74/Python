from django.urls import path
from .views import ListEnter, PostEnter, PostPermission, RemovePermission


urlpatterns = [
    path('enter/<str:key>/list/', ListEnter.as_view()),
    path('enter/<str:key>/<int:room_id>/', PostEnter.as_view()),
    path('permission/<str:key>/<str:user_key>/<int:room_id>/', PostPermission.as_view()),
    path('permission/<str:key>/<str:user_key>/<int:room_id>/remove/', RemovePermission.as_view()),

]