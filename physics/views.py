from django.shortcuts import render

def home(request):
    return render(request,"physics/home.html")

def home_a_matter_and_radiation(request):
    return render(request, "physics/home_a_matter_and_radiation.html")

def home_d_electricity(request):
    return render(request, "physics/home_d_electricity.html")

def home_e_further_mechanics_and_thermal_physics(request):
    return render(request, "physics/home_e_further_mechanics_and_thermal_physics.html")

