from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('home2', views.home_page2, name='home2'),
]
