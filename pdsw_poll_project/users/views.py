from django.shortcuts import render, redirect
from users.forms import UserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})