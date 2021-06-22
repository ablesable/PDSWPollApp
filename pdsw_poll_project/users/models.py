from django.db.models import IntegerField, Model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

DROPDOWN_GENDERS =[('female', 'Female'),
                    ('male', 'Male'),
                    ('other', 'Other')
                    ]

class UserExtendedModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    gender = models.CharField(max_length = 30, choices=DROPDOWN_GENDERS)
    age = models.IntegerField(validators = [MinValueValidator(15), MaxValueValidator(100)])

    def __str__(self):
        return self.user.username