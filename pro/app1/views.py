from django.shortcuts import render
from django.http import HttpResponse

# Blank View
def blank(request):
    return HttpResponse("Hello")
# Home View
def home(request):
    return HttpResponse("Django")
# Index View
def index(request):
    return HttpResponse("Welcome Welcome")
