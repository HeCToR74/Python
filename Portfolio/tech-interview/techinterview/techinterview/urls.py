"""techinterview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/feedback/', include('feedback.api.urls')),
    path('api/departments/', include('departments.api.urls')),
    path('api/interviews/', include('interviews.api.urls')),
    path('api/questions/', include('questions.api.urls')),
    path('api/user/', include('authorization.api.urls')),

    # Should be at the bottom of urlpatterns
    re_path(r'.*', include('home.urls')),
]