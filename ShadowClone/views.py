from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Forest(request):
    return HttpResponse("This is my Ninja Way")
