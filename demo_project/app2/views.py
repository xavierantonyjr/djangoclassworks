from django.shortcuts import render

# First View
def third(request):
    """return HttpResponse("First Page")"""
    return render(request, 'third.html')
# Second View
def fourth(request):
    """return HttpResponse("Second Page")"""
    return render(request, 'fourth.html')