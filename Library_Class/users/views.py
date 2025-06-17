from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import SignUpForm, SignInForm


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:signin')
        return render(request, 'signup.html', {'form': form})


class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('books:home')
        return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})


class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('books:home')
