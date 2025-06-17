from django import forms
# from django.contrib.auth.forms import User
#
# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username', 'email', 'password']
#
# class SignInForm(forms.Form):
#     username = forms.CharField(max_length=150, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)
#
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name', 'last_name')

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
