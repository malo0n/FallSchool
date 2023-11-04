from django import forms
from .models import *
GENDERS = [('Парень','Парень'),('Девушка','Девушка')]
class UserInfo(forms.ModelForm):
    gender = forms.ChoiceField(
        widget = forms.RadioSelect(attrs={'class': 'custom-radio', 'id': 'gender'}),
        choices=GENDERS,
    )
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'inputAvatar', 'id': 'file'}),
            'name': forms.TextInput(attrs={'class': 'name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'date'}),
            'telegram': forms.TextInput(attrs={'class': 'telegram', 'id': 'telegram'}),
            'phone_number': forms.TextInput(attrs={'class': 'phone', 'id': 'phone'}),
            'description': forms.Textarea(attrs={'class': 'info', 'id': 'about_me'}),
        }
        