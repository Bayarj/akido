# example/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('trainer.html', views.trainer, name="trainer"),
    path('signup.html', views.signup, name="signup"),
    path('why.html', views.why, name="why"),
    path('contact.html', views.contact, name="signup"),
]
