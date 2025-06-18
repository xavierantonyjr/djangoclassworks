from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignupForm, SignInForm

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'register.html',{'form':form})
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signin')  # Redirect to sign-in page after successful registration
        return render(request, 'register.html', {'form': form})

class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'form': form})


class SignoutView(View):
    def get(self, request):
        logout(request)
        return render(request,'logout.html')
