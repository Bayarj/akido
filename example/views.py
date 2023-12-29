# example/views.py
from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')
def trainer(request):
    return render(request, 'trainer.html')
def signup(request):
    return render(request, 'signup.html')
def why(request):
    return render(request, 'why.html')
def contact(request):
    return render(request, 'contact.html')