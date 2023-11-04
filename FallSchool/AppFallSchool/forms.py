from django import forms
from .models import *
class UserInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'inputAvatar', 'id': 'file'}),
            'name': forms.TextInput(attrs={'class': 'name'}),
            'gender': forms.RadioSelect(attrs={'class': 'custom_radio', 'id': 'male', 'name': 'gender'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'date'})

        }
