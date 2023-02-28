from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    if request.method == 'GET':
        return HttpResponse('Hello')