# example/views.py
from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    # now = datetime.now()
    # html = f'''
    # <html>
    #     <body>
    #         <h1>Сайн уу хонгор минь</h1>
    #         <p>The current time is { now }.</p>
    #     </body>
    # </html>
    # '''
    return render(request, 'index.html')
