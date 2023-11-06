from django import forms
# from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

GENDERS = [('Парень','Парень'),('Девушка','Девушка')]
GRADES = [('Студент', 'Выпускник'), ('Работник','Работник')]
class UserInfo(forms.ModelForm):
    
    def is_valid(self) -> bool:
        asd = super().is_valid()
        if self.errors:
            print(self.errors)
        return asd
    
    gender = forms.ChoiceField(
        widget = forms.RadioSelect(attrs={'class': 'custom-radio', 'id': 'gender'}),
        choices=GENDERS,
    )
    grade = forms.ChoiceField(
        widget= forms.RadioSelect(attrs={'class': 'radio-custom', 'id': 'grade'}),
        choices= GRADES,
    )  
    class Meta:
        model = User
        fields = ['avatar', 'name', 'date_of_birth', 'telegram', 'phone_number', 'description', 'gender']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'inputAvatar', 'id': 'file'}),
            'name': forms.TextInput(attrs={'class': 'name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'date'}),
            'telegram': forms.TextInput(attrs={'class': 'telegram', 'id': 'telegram'}),
            'phone_number': forms.TextInput(attrs={'class': 'phone', 'id': 'phone'}),
            'description': forms.Textarea(attrs={'class': 'info', 'id': 'about_me'}),
            'course': forms.TextInput(attrs={'class': 'd'})
        }
        