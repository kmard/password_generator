from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello there friend")

def eggs(request):
    return HttpResponse("this page eggs")