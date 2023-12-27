# example/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('login', views.login, name="home"),
    path('signup', views.signup, name="home"),
]
