from django.shortcuts import render

def home(request):
    return render(request,"gcsemaths/home.html")

def home_number(request):
    return render(request,"gcsemaths/number_home.html")

def home_algebra(request):
    return render(request,"gcsemaths/algebra_home.html")

def home_geometry(request):
    return render(request,"gcsemaths/e_geometry_home.html")

def home_exam_non_calc(request):
    return render(request, "gcsemaths/home.html")