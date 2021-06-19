from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    first_option = models.CharField(max_length=40)
    second_option = models.CharField(max_length=40)
    third_option  = models.CharField(max_length=40)
    first_option_count = models.IntegerField(default = 0)
    second_option_count = models.IntegerField(default = 0)
    third_option_count = models.IntegerField(default = 0)