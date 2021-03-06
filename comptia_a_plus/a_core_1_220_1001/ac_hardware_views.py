from django.shortcuts import render
from random import randint
from . import ac_hardware_logic
import sys
from comptia_a_plus import comptia_classes_functions as cf

def list_callable_functions():
    """returns list of all modules in this file
    This function MUST remain in this file to work correctly!
    Used by:
    modulesList
    previousNext
    """
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    return entireModuleList

def modulesList():#this list is used by urls to automatically generate paths based on what's in this file
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

#return templates for use by different types of view functions, depending on question type
def mcRevealTemplate():
    return "comptia_a_plus/mcReveal.html"
def dragRevealTemplate():
    return "comptia_a_plus/dragReveal.html"
def dragDoubleRevealTemplate():
    return "comptia_a_plus/dragDoubleReveal.html"
def module_name():
    return 'ac_hardware_logic'

for module in ac_hardware_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'comptia_a_plus/comptiaSelectMultiDrag.html', cf.view_builder('ac_hardware_logic', cf.currentFuncName()))")
    


'''
What the old views looked like, just in case you ever need them, you silly goose!
def a1qa_what_is_sql(request):
    return render(request, template(), view_builder(cf.currentFuncName()))

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
'''