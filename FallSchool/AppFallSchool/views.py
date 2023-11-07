from django.shortcuts import render, redirect
from .models import User
from .forms import UserInfo

# Create your views here.

def first__screen(request):
  print(request, request.method)
  if request.method == "POST":
    print(request.POST)
    form = UserInfo(request.POST, request.FILES)
    if form.is_valid():
      form.save(commit=True)  
    return redirect('second__screen')
  else:
      form = UserInfo()
      
  return render(request, 'AppFallSchool/first__screen.html', {'form': form})


def second__screen(request):
  print(request, request.method)
  if request.method == 'POST':
    form = UserInfo(request.POST, request.FILES)
    try:
      print(5)
      if form.is_valid():
        print(5)
        form.save(commit=False) 
        second_page = form.cleaned_data
        last_person = User.objects.last()
        print(second_page)
        last_person.grade = second_page.grade
        last_person.course = second_page.course
        last_person.degree = second_page.degree
        last_person.faculty = second_page.faculty
        last_person.program = second_page.program
        last_person.job = second_page.job
        last_person.job_date_of_start = second_page.job_date_of_start
        last_person.save()
    except Exception as e:
      print(str(e)) 
  else:
    form = UserInfo()
  return render(request, 'AppFallSchool/second__screen.html', {'form' : form})