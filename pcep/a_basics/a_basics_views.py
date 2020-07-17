from django.shortcuts import render
from random import randint
from . import a_basics_logic
import sys
from pcep import pcep_helper_functions as phf


def view_builder(name): #Essential for all other view modules
    passed = eval(f"a_basics_logic.{name}()")
    return phf.allArguments2(passed)

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

'''
#generates a whole section of 15-16 marks
def section_generator(request):
    return render(request, "physics_section.html", view_builder(currentFuncName()))

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
#selects a function at random from moduleList generated list and returns everything needed to generate a view
'''

def e1qa_test(request):
    return render(request, "pcep/pcep_multi_choice.html", view_builder(currentFuncName()))

def a1qa_interpreting_the_interpreter(request):
    return render(request, "pcep/pcep_multi_choice_dynamic.html", view_builder(currentFuncName()))
def a1qb_compilation_and_the_compiler(request):
    return render(request, "pcep/pcep_multi_choice.html", view_builder(currentFuncName()))
def a1qc_machine_higher_level_natural_languages(request):
    return render(request, "pcep/pcep_multi_choice.html", view_builder(currentFuncName()))
def a1qd_language_elements(request):
    return render(request, "pcep/pcep_multi_choice.html", view_builder(currentFuncName()))
def a1qe_python(request):
    return render(request, "pcep/pcep_multi_choice.html", view_builder(currentFuncName()))
def a1qf_python_keywords(request):
    return render(request, "pcep/pcep_multi_choice.html", view_builder(currentFuncName()))
def a1qg_indentation_and_spacing(request):
    return render(request, "pcep/pcep_multi_choice.html", view_builder(currentFuncName()))
