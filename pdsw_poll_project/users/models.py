from django.db.models import IntegerField, Model
from django.core.exceptions import ValidationError

# for another way of gender validation #

# def validate_capitalized(value):
#     if value != value.capitalize():
#         raise ValidationError('Invalid (not capitalized) value: %(value)s',
#                               code='invalid',
#                               params={'value': value})

# def validate_genders(value):
#     if (value != 'Male' or value != 'Female' or value!= 'Other'):
#         raise ValidationError('Please enter your proper gender (Male, Female, Other)',
#                               code='invalid',
#                               params={'value': value})

DROPDOWN_GENDERS =[('female', 'Female'),
                    ('male', 'Male'),
                    ('other', 'Other')
                    ]




