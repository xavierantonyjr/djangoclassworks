from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def register(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    return render(request, 'signout.html')
