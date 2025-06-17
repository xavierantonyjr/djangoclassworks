from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    role_choices = [('Student', 'Student'), ('Staff', 'Staff')]
    role = forms.ChoiceField(choices=role_choices, required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2','first_name', 'last_name','phone', 'address','role')


class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
