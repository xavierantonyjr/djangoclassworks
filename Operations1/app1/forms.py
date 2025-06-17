from django import forms

class AdditionForm(forms.Form):
    number1 = forms.IntegerField()
    number2 = forms.IntegerField()

class FactForm(forms.Form):
    number1=forms.IntegerField()

class BmiForm(forms.Form):
    weight=forms.IntegerField()
    height=forms.IntegerField()


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    email = forms.EmailField(max_length=50, widget=forms.EmailInput)

    gender_choices = [('male', 'Male'), ('female', 'Female'),('others','Others')]
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)

    role_choices = [('admin', 'Admin'), ('student', 'Student')]
    role = forms.ChoiceField(choices=role_choices)


class CalorieForm(forms.Form):

    weight = forms.IntegerField()
    height = forms.IntegerField()
    age = forms.IntegerField()

    gender_choices = [('male', 'Male'), ('female', 'Female'),('others','Others')]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)

    activity_choice = [(1.2,'sedentary'),(1.375,'light activity'),(1.55,'moderate'),(1.725,'hard'),(1.9,'very hard')]
    activity_level = forms.ChoiceField(choices=activity_choice)