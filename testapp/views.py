from django.shortcuts import render

def home(request):
    return render(request,"testapp/dev_home.html")