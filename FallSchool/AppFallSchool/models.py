from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, telegram, password=None, **extra_fields):
        user = self.model(telegram=telegram, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, telegram, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(telegram, password, **extra_fields)
        # user.save(using=self._db)
        # return 
    
class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    telegram = models.CharField(max_length=50, unique = True, blank=True)
    phone_number = models.CharField(max_length=11, unique = True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    
    grade = models.CharField(max_length=40, null=True, blank=True)
    course = models.CharField(max_length=40, null=True, blank=True)
    degree = models.CharField(max_length=40, null=True, blank=True)
    faculty = models.CharField(max_length=40, null=True, blank=True)
    program = models.CharField(max_length=40, null=True, blank=True)
    job = models.CharField(max_length=25, null=True, blank=True)
    job_date_of_start = models.DateField(null=True, blank=True)
    
    USERNAME_FIELD = 'telegram'
    # EMAIL_FILED = 'phone_number'
    REQUIRED_FIELDS=[]
    objects = UserManager()




