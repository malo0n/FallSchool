from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    telegram = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    description = models.TextField()
    avatar = models.ImageField()
    

