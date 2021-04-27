from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout

from .forms import UserRegisterForm, UserAuthenticationForm

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'registration error')
    else:
        form = UserRegisterForm()
    return render(request, 'UserApp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'registration error')
    else:
        form = UserAuthenticationForm()
    return render(request, 'UserApp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')