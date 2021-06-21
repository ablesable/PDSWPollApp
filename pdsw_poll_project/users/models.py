from django.db.models import IntegerField, Model
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
DROPDOWN_GENDERS =[('female', 'Female'),
                    ('male', 'Male'),
                    ('other', 'Other')
                    ]

class UserExtended(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField(validators = [MinValueValidator(15), MaxValueValidator(100)])
    gender = models.CharField(max_length=50, choices = DROPDOWN_GENDERS)

    email = models.EmailField()






