from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from app1.models import School

# Signup Form
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Signin Form
class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

# School Form
class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'principal', 'location']
