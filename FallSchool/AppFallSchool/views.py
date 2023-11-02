from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def first__screen(request):
    return render(request, 'AppFallSchool/first__screen.html')
def second__screen(request):
    return render(request, 'AppFallSchool/second__screen.html')