from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail

from .forms import SignUpForm, SignInForm
from .models import CustomUser


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
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.generate_otp()

            send_mail(
                'Django OTP Verification',
                f'Your OTP is: {user.otp}',
                'noreply@example.com',
                [user.email],
                fail_silently=False,
            )

            messages.success(request, "OTP sent to your email.")
            return redirect('verify')

        return render(request, 'signup.html', {'form': form})


class SigninView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if not user.is_active:
                    form.add_error(None, 'Account is not active. Please verify your email.')
                else:
                    login(request, user)
                    if user.is_superuser:
                        return redirect('admin_home')
                    elif user.role == 'Student':
                        return redirect('student_home')
                    elif user.role == 'Staff':
                        return redirect('staff_home')
            else:
                form.add_error(None, 'Invalid username or password.')

        return render(request, 'registration/login.html', {'form': form})


class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class VerifyView(View):
    def get(self, request):
        return render(request, 'verify.html')

    def post(self, request):
        otp = request.POST.get('otp')
        try:
            user = CustomUser.objects.get(otp=otp)
            user.is_active = True
            user.is_verified = True
            user.otp = None
            user.save()
            messages.success(request, 'Email verified. You can now log in.')
            return redirect('signin')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid OTP')
            return redirect('verify')


class AdminHomeView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'admin_home.html')
        else:
            return redirect('signin')


class StudentHomeView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'Student':
            return render(request, 'student_home.html')
        else:
            return redirect('signin')


class StaffHomeView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'Staff':
            return render(request, 'staff_home.html')
        else:
            return redirect('signin')
