from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import *

class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserExtended 
        fields = ('username', 'age', 'gender', 'email', 'password')