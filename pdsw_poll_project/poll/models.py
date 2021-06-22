from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    first_option = models.CharField(max_length=40)
    second_option = models.CharField(max_length=40)
    third_option  = models.CharField(max_length=40)
    
    #youth
    first_option_count_youth = models.IntegerField(default = 0)
    second_option_count_youth = models.IntegerField(default = 0)
    third_option_count_youth = models.IntegerField(default = 0)

    #young
    first_option_count_youngpeople = models.IntegerField(default = 0)
    second_option_count_youngpeople = models.IntegerField(default = 0)
    third_option_count_youngpeople = models.IntegerField(default = 0)

    #middleage
    first_option_count_middleagepeople = models.IntegerField(default = 0)
    second_option_count_middleagepeople = models.IntegerField(default = 0)
    third_option_count_middleagepeople = models.IntegerField(default = 0)

    #old
    first_option_count_oldpeople = models.IntegerField(default = 0)
    second_option_count_oldpeople = models.IntegerField(default = 0)
    third_option_count_oldpeople = models.IntegerField(default = 0)

    def first_option_result(self):
        return self.first_option_count_youth + self.first_option_count_youngpeople + self.first_option_count_middleagepeople + self.first_option_count_oldpeople

    def second_option_result(self):
        return self.second_option_count_youth + self.second_option_count_youngpeople + self.second_option_count_middleagepeople + self.second_option_count_oldpeople

    def third_option_result(self):
        return self.third_option_count_youth + self.third_option_count_youngpeople + self.third_option_count_middleagepeople + self.third_option_count_oldpeople

    def total(self):
        return self.first_option_count_youth + self.second_option_count_youth + self.third_option_count_youth + self.first_option_count_youngpeople + self.second_option_count_youngpeople + self.third_option_count_youngpeople + self.first_option_count_middleagepeople + self.second_option_count_middleagepeople + self.third_option_count_middleagepeople + self.first_option_count_oldpeople + self.second_option_count_oldpeople + self.third_option_count_oldpeople

class VoteModel(models.Model):
    which_user_voted = models.ForeignKey(User, on_delete=models.CASCADE)
    poll_voted = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)