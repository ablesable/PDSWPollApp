from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from users.forms import UserForm

# Create your views here.

# def register(request):
#     form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()


    return render(request, 'users/register.html', {'form': form})