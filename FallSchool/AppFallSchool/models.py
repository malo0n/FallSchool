from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    
    avatar = models.ImageField()
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    telegram = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    description = models.TextField()
    
    grade = models.CharField(max_length=10)
    course = models.CharField(max_length=15)
    degree = models.CharField(max_length=10)
    faculty = models.CharField(max_length=20)
    program = models.CharField(max_length=20)
    job = models.CharField(max_length=25)
    job_date_of_start = models.DateField()
    

