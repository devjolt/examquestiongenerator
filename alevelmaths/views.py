from django.shortcuts import render

def home(request):
    return render(request,"alevelmaths/alevelmaths_home.html")

def trigonometry_home(request):
    return render(request,"alevelmaths/trigonometry_home.html")
