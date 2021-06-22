from django.shortcuts import render, redirect
from django.http import HttpResponse
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
                messages.info(request, "Your poll has been created!")
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
        poll = Poll.objects.get(pk=poll_id)
        context = {
            'poll' : poll
        }
        return render(request, 'poll/results.html', context)
    else:
        messages.warning(request, "Unfoturnately - this feature is only for admin!")
        return redirect('home') 

def vote(request, poll_id):
    if request.user.is_superuser:
        messages.info(request, "Not this time - This feature is only for users. Please register first as one!")
        return redirect('home') 
    else:
        poll = Poll.objects.get(pk=poll_id)
        if request.method == 'POST':
            selected_option = request.POST['poll']
            print(request.POST['poll'])
            
            if selected_option == 'option1':
                poll.first_option_count += 1
            
            elif selected_option == 'option2':
                poll.second_option_count += 1 

            elif selected_option == 'option3':
                poll.third_option_count += 1
            
            else:
                return HttpResponse(400)

            poll.save()
            return redirect('results', poll.id)

            
        context = {
            'poll': poll
        }
        return render(request, 'poll/vote.html', context)