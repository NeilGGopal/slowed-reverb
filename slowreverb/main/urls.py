from django.urls import path

from . import views

urlpatterns = [
    path('convert', views.home, {'option': 'convert'}, name='home'),
    path('download', views.home, {'option': 'download'}, name='home'),
    path('', views.home, {'option': ''}, name='home'),
]
