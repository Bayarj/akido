# example/views.py
from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
