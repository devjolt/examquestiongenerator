from django.shortcuts import render
from random import randint
from . import e_further_mechanics_thermal_physics_logic
import sys
from physics import physics_helper_functions as phf


def view_builder(name): #Essential for all other view modules
    passed = eval(f"e_further_mechanics_thermal_physics_logic.{name}()")
    return phf.allArguments2(passed)

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

#generates a whole section of 15-16 marks
def section_generator(request):
    return render(request, "physics_section.html", view_builder(currentFuncName()))

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
#selects a function at random from moduleList generated list and returns everything needed to generate a view
def e1_uniform_circular_motion_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e2_centripetal_acceleration_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e3_on_the_road_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e4_at_the_fairground_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
#Individual question views start here
def e1qa_minute_hand_of_clock(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e1qb_time_pweriod_angle_electric_motor(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e1qc_planet_rotation(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e1qd_satalite_orbit(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e2qa_the_wheel_of(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e2qb_object_circular_path(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e2qc_earth_around_sun(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e2qd_hammer_thrower(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e3qa_bridge(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e3qb_roundabout(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e3qc_racingtrack(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e4qa_rollercoaster(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e4qb_swing(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def e4qc_wheel(request):
    return render(request, "questionAnswerPrintable.html", view_builder(currentFuncName()))