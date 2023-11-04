from django.shortcuts import render, redirect
from .models import User
from .forms import UserInfo

# Create your views here.

def first__screen(request):
    form = UserInfo()
    if request.method == 'POST' and form.is_valid():
        form = UserInfo(request.POST)
        return redirect(second__screen)
    return render(request, 'AppFallSchool/first__screen.html', {'form' : form})
def second__screen(request):
    form = UserInfo()
    if request.method == 'POST' and form.is_valid():
        form = UserInfo(request.POST)
        form.save()
    return render(request, 'AppFallSchool/second__screen.html', {'form' : form})