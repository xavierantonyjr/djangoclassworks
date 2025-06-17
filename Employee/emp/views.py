from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employee = Employee.objects.all()
    return render(request,'employee_list.html',{'employee':employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emp:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_details(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'employee_details.html',{'employee':employee})

def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('emp:employee_list')

def employee_update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,request.FILES,instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emp:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request,'employee_form.html',{'form':form})

