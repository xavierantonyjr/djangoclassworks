from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
def student_list(request):
    student = Student.objects.all()
    return render(request,'student_list.html',{'student':student})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    else:
        form = StudentForm(instance=student)
    return render(request,'student_form.html',{'form':form})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method =='POST':
        student.delete()
        return redirect('student:student_list')
    return render(request,'student_delete.html',{'student':student})