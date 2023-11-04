from django.shortcuts import render, HttpResponse
from .models import User
from .forms import UserInfo

# Create your views here.

def first__screen(request):
    form = UserInfo()
    return render(request, 'AppFallSchool/first__screen.html', {'form' : form})
def second__screen(request):
    return render(request, 'AppFallSchool/second__screen.html')