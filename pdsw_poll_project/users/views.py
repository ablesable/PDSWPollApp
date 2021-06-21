from django.shortcuts import render, redirect
from users.forms import UserForm, ExtendedUserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form = ExtendedUserForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserForm()
        profile_form = ExtendedUserForm()
    return render(request, 'users/register.html', {'form': form, 'profile_form' : profile_form})