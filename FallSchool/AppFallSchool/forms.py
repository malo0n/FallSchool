from django import forms
from django import models


class UserInfo(forms.Models):
    name = forms.CharField(attrs={'class':'name'})