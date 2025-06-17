from django.shortcuts import render
from app1.forms import AdditionForm
# from app2.forms import FactForm
# form app2.forms import BmiForm
from app1.forms import SignupForm
from app1.forms import CalorieForm

def addition(request):
    result = None

    if request.method == 'POST':
        form_instance = AdditionForm(request.POST)
        if form_instance.is_valid():
            n1 = form_instance.cleaned_data['number1']
            n2 = form_instance.cleaned_data['number2']
            result = n1 + n2
    else:
        form_instance = AdditionForm()

    return render(request, 'addition.html', {'form': form_instance, 'result': result})

# Factorial View
def factorial(request):

    return render(request, 'factorial.html')

# BMI Calculator View
def bmi_calculator(request):

    return render(request, 'bmi.html')

def signup(request):
    if request.method == 'GET':
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})

def calorie(request):
    if request.method == 'POST':
        print(request.POST)
        form_instance = CalorieForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            weight = float(data['weight'])
            height = float(data['height'])
            age = int(data['age'])
            gender = data['gender']
            activity = float(data['activity_level'])  # Make sure this is numeric (e.g., 1.2, 1.375, etc.)

            if gender == 'male':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            print("BMR:", bmr)

            calorie_required = bmr * activity
            print("Calorie required:", calorie_required)

            return render(request, 'calorie.html', {'form': form_instance,'result':calorie_required})

    form_instance = CalorieForm()
    return render(request, 'calorie.html', {'form': form_instance})
