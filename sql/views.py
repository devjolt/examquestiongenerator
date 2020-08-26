from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    response = HttpResponse('aaaaaa')
    response.set_cookie('aaaaab', 'aaaaac')
    print("yep")
    return render(request,"sql/home.html")

def work_on(request):
    return render(request, "sql/work_on.html")

def home_a_basics(request):
    return render(request,"sql/home_a_basics.html")