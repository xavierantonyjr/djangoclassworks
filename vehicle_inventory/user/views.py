from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, UpdateView, RedirectView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from .forms import SignInForm, SignUpForm, UpdateProfileForm
from .models import CustomUser
from django.contrib import messages

@method_decorator(sensitive_post_parameters('password'), name='dispatch')
class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = SignInForm
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f"Welcome back, {user.username}!")
            return redirect(self.get_success_url())
        form.add_error(None, 'Invalid credentials')
        return self.form_invalid(form)

class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)

class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Registration successful! Please login.")
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UpdateProfileForm
    template_name = 'user/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
