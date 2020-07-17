from django.shortcuts import render

def home(request):
    return render(request,"pcep/home.html")

def home_basics(request):
    return render(request,"pcep/a_basics.html")
