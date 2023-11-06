from django.shortcuts import render, redirect
from .models import User
from .forms import UserInfo

# Create your views here.

def first__screen(request):
  print(request, request.method)
  if request.method == "POST":
    # print(request.POST)
    form = UserInfo(request.POST, request.FILES)
    if form.is_valid():
      form.save(commit=True)  
    return redirect('second__screen')
  else:
      form = UserInfo()
      
  return render(request, 'AppFallSchool/first__screen.html', {'form': form})



def second__screen(request):
    form = UserInfo()
    if request.method == 'POST' and form.is_valid():
        form = UserInfo(request.POST)
        if form.is_valid():
          form.save(commit=False)
          second_page = form.cleaned_data()
          last_person = User.objects.last()
          last_person.degree = second_page.degree
          last_person.save()
    return render(request, 'AppFallSchool/second__screen.html', {'form' : form})