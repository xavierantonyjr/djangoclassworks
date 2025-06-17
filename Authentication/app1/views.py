from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from app1.forms import SignUpForm, SignInForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.set_password(form.cleaned_data['password'])
            form.save()
            return redirect('signin')

class SigninView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'login.html',{'form': form})
    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'login.html', {'form': form})

class  SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')