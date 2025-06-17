from django import forms
from .models import Vehicle
from user.models import CustomUser


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model_name', 'year', 'price', 'image', 'is_available']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']
