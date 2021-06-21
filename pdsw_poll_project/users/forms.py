from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import *

class UserForm(UserCreationForm):
    username = forms.CharField()
    age = forms.IntegerField(validators = [MinValueValidator(15), MaxValueValidator(100)])#ValidateAge() #specific model needed
    gender = forms.CharField(label='What is your gender?', widget = forms.Select(choices=DROPDOWN_GENDERS))

    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ('username', 'age', 'gender', 'email')