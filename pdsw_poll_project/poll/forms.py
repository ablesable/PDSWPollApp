from django.forms import ModelForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'first_option', 'second_option', 'third_option']