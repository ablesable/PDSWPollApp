from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
# from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreatePollForm(request.POST)
            if form.is_valid():
                
                form.save()
                return redirect('home')
        else:
            form = CreatePollForm()
        context = {
            'form' : form
        }
        return render(request, 'poll/create.html', context)
    else:
        messages.warning(request, "Unfoturnately - this feature is only for admin!")
        return redirect('home') 

def results(request, poll_id):
    if request.user.is_superuser:
        context = {}
        return render(request, 'poll/results.html', context)
    else:
        messages.warning(request, "Unfoturnately - this feature is only for admin!")
        return redirect('home') 

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        print(request.POST[''])
    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)