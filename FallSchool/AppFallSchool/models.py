from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class User(AbstractBaseUser):
    
    avatar = models.ImageField()
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    telegram = models.CharField(max_length=50, unique = True)
    phone_number = models.CharField(max_length=11)
    description = models.TextField()
    
    grade = models.CharField(max_length=10)
    course = models.CharField(max_length=15)
    degree = models.CharField(max_length=10)
    faculty = models.CharField(max_length=20)
    program = models.CharField(max_length=20)
    job = models.CharField(max_length=25)
    job_date_of_start = models.DateField()
    
    USERNAME_FIELD = 'telegram'
    REQUIRED_FIELDS=[]

class UserManager(BaseUserManager):
    # use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        password=None
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)