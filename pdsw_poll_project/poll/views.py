from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm 
from users.forms import ExtendedUserForm
from .models import Poll, VoteModel
from django.contrib import messages

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

#################################

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


#################################

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


################################

def vote(request, poll_id):
    if request.user.is_superuser:
        messages.info(request, "Not this time - This feature is only for users. Please register first as one!")
        return redirect('home') 
    else:
        poll = Poll.objects.get(pk=poll_id)
        if request.method == 'POST':
            selected_option = request.POST['poll']
            current_user = request.user
            current_poll = Poll.objects.get(pk=poll_id)
            current_user_age = request.user.profile_user.age
            
            if VoteModel.objects.filter(which_user_voted = current_user, poll_voted=current_poll).exists():
                messages.info(request, "You've already voted!")
                return redirect('home')
            else: 
                voted = VoteModel.objects.create(which_user_voted = current_user, poll_voted=current_poll)
                voted.save()

                #youth counting
                if ((selected_option == 'option1') and (15 <= current_user_age <= 19)):
                    poll.first_option_count_youth += 1
                
                elif ((selected_option == 'option2') and (15 <= current_user_age <= 19)):
                    poll.second_option_count_youth += 1
                
                elif ((selected_option == 'option3') and (15 <= current_user_age <= 19)):
                    poll.third_option_count_youth += 1

                #young people counting
                elif ((selected_option == 'option1') and (20 <= current_user_age <= 39)):
                    poll.first_option_count_youngpeople += 1
                
                elif ((selected_option == 'option2') and (20 <= current_user_age <= 39)):
                    poll.second_option_count_youngpeople += 1

                elif ((selected_option == 'option3') and (20 <= current_user_age <= 39)):
                    poll.third_option_count_youngpeople += 1
                
                #middleage people counting
                elif ((selected_option == 'option1') and (40 <= current_user_age <= 59)):
                    poll.first_option_count_middleagepeople += 1
                
                elif ((selected_option == 'option2') and (40 <= current_user_age <= 59)):
                    poll.second_option_count_middleagepeople += 1 

                elif ((selected_option == 'option3') and (40 <= current_user_age <= 59)):
                    poll.third_option_count_middleagepeople += 1
                
                #old people counting
                elif ((selected_option == 'option1') and (current_user_age > 59)):
                    poll.first_option_count_oldpeople += 1
                
                elif ((selected_option == 'option2') and (current_user_age > 59)):
                    poll.second_option_count_oldpeople += 1 

                elif ((selected_option == 'option3') and (current_user_age > 59)):
                    poll.third_option_count_oldpeople += 1


                else:
                    return HttpResponse(400)

                poll.save()
                messages.info(request, "Thanks for your vote")
                return redirect('home')

            
        context = {
            'poll': poll
        }
        return render(request, 'poll/vote.html', context)