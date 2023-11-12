from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        fields = ('avatar', 'name', 'date_of_birth', 'telegram', 'phone_number', 'description', 'grade', 'course', 'degree', 'faculty', 'program', 'job', 'job_date_of_start', 'gender')

    