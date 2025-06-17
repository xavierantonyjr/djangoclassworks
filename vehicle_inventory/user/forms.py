from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
from django.contrib.auth import password_validation

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'address')


class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'address')


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput, required=True)
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput, required=True)
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError("The new passwords do not match.")

            password_validation.validate_password(new_password1)

        return cleaned_data


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True, max_length=254)


class ResetPasswordForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    new_password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("new_password1") != cleaned_data.get("new_password2"):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class DeleteAccountForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="I confirm that I want to delete my account")


class DeactivateAccountForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="I confirm that I want to deactivate my account")


class ReactivateAccountForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="I confirm that I want to reactivate my account")
