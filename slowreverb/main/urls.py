from django.urls import path

from . import views

urlpatterns = [
    path('convert', views.home, name='home'),
    path('download', views.home, name='home'),
    path('', views.home, name='home'),
]