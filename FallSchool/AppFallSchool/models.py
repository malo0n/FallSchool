from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, telegram, password, **extra_fields):
        # password=None
        user = self.model(telegram=telegram, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
    def create_superuser(self, telegram, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(telegram, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(null=True)
    name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)
    telegram = models.CharField(max_length=50, unique = True)
    phone_number = models.CharField(max_length=11, unique = True, null=True)
    description = models.TextField(null=True)
    
    is_superuser = models.BooleanField(default=False)
    
    grade = models.CharField(max_length=10, null=True)
    course = models.CharField(max_length=15, null=True)
    degree = models.CharField(max_length=10, null=True)
    faculty = models.CharField(max_length=20, null=True)
    program = models.CharField(max_length=20, null=True)
    job = models.CharField(max_length=25, null=True)
    job_date_of_start = models.DateField(null=True)
    
    USERNAME_FIELD = 'telegram'
    EMAIL_FILED = 'phone_number'
    REQUIRED_FIELDS=[]
    objects = UserManager()




