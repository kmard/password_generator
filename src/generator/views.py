from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def eggs(request):
    return HttpResponse("<h1>this page eggs</h1>")