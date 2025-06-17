from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Home View
def home(request):
    """return HttpResponse("Welcome to Home")"""
    context={'name':'Arun','age':25,'place':'ekm'}
    return render(request,'index.html',context)

# First View
def first(request):
    """return HttpResponse("First Page")"""
    return render(request, 'first.html')
# Second View
def second(request):
    """return HttpResponse("Second Page")"""
    return render(request, 'second.html')