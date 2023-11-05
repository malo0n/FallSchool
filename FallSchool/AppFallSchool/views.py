from django.shortcuts import render, redirect
from .models import User
from .forms import UserInfo

# Create your views here.

def first__screen(request):
  print(request, request.method)
  if request.method == "POST":
    print(request.POST)
    form = UserInfo(request.POST)
    if form.is_valid():
      post = form.save(commit=True)
      post.save()
      print(request.POST, form)
      # my_form = form.save()
      # User.objects
    # return redirect('AppFallSchool/second__screen.html')
  else:
      form = UserInfo()
  return render(request, 'AppFallSchool/first__screen.html', {'form': form})



def second__screen(request):
    form = UserInfo()
    if request.method == 'POST' and form.is_valid():
        form = UserInfo(request.POST)
        form.save()
    return render(request, 'AppFallSchool/second__screen.html', {'form' : form})