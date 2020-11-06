from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.
#def home(request):
#    return HttpResponse("<h1>look</h1>")

def home(request):
    return render(request,"home.html")

def work_on(request):
    return render(request, "work_on.html")