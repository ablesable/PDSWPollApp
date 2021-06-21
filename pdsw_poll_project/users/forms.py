from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import *

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ExtendedUserForm(forms.ModelForm):
    
    class Meta:
        model = UserExtendedModel
        fields = ('age', 'gender')