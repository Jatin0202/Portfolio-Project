from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home , name='project'),
    path('<int:project_id>/', views.detail ,name='detail'),
]
