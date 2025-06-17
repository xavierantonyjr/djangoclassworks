from django.shortcuts import render

# Welcome View
def welcome(request):
    return render(request,'welcome.html')

# Addition View
def addition(request):
    context = {}
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        result = num1 + num2
        context = {'result': result}
    return render(request, 'addition.html', context)

# Factorial View
def factorial(request):
    context = {'fact': None}  # Default context

    if request.method == 'POST':
        num = int(request.POST.get('num1'))

        fact = 1
        for i in range(1, num + 1):
            fact *= i

        context['fact'] = fact

        return render(request, 'factorial.html', context)
    return render(request, 'factorial.html')

# BMI Calculator View
def bmi_calculator(request):
    context = {'bmi': None, 'category': None}

    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height_cm = float(request.POST.get('height'))
        height_m = height_cm / 100  # Convert to meters

        if height_m > 0:
            bmi = round(weight / (height_m ** 2), 2)
            context['bmi'] = bmi
            if bmi < 18.5:
                category = 'Underweight'
            elif bmi < 25:
                category = 'Normal weight'
            elif bmi < 30:
                category = 'Overweight'
            else:
                category = 'Obese'

            context['category'] = category

    return render(request, 'bmi.html', context)
