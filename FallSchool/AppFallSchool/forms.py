from django import forms
# from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class UserInfo(forms.ModelForm):
    
    def is_valid(self) -> bool:
        asd = super().is_valid()
        if self.errors:
            print(self.errors)
        return asd
    
    class Meta:
        model = User
        fields = ['avatar', 'name', 'date_of_birth', 'telegram', 'phone_number', 'description', 'grade', 'course', 'degree', 'faculty', 'program', 'job', 'job_date_of_start', 'gender']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'inputAvatar', 'id': 'file'}),
            'name': forms.TextInput(attrs={'class': 'name'}),
            'gender': forms.TextInput(attrs={'class': 'genderInput'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'date'}),
            'telegram': forms.TextInput(attrs={'class': 'telegram', 'id': 'telegram'}),
            'phone_number': forms.TextInput(attrs={'class': 'phone', 'id': 'phone'}),
            'description': forms.Textarea(attrs={'class': 'info', 'id': 'about me'}),
            'grade': forms.TextInput(attrs={'class': 'gradeInput', 'value': 'value'}),
            'course': forms.TextInput(attrs={'class': 'courseInput'}),
            'degree': forms.TextInput(attrs={'class': 'degreeInput'}),
            'faculty': forms.TextInput(attrs={'class': 'facultyInput'}),
            'program': forms.TextInput(attrs={'class': 'programInput'}),
            'job': forms.TextInput(attrs={'class': 'job', 'id': 'job'}),
            'job_date_of_start': forms.DateInput(attrs={'class': 'jobTime'}),

        }
        