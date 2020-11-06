from django.shortcuts import render
from random import randint
from . import aa_mobile_devices_logic
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

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_callable_functions(), 'e', 0, 1)

def test(request):
    return render(request, "comptia_a_plus/comptiaSelectMultiDrag.html", cf.view_builder('aa_mobile_devices_logic', cf.currentFuncName()))

def type_test(request):
    return render(request, "comptia_a_plus/type.html", cf.view_builder('aa_mobile_devices_logic', cf.currentFuncName()))


for module in aa_mobile_devices_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'comptia_a_plus/comptiaSelectMultiDrag.html', cf.view_builder('aa_mobile_devices_logic', cf.currentFuncName()))")



'''
What the old views looked like, just in case you ever need them, you silly goose!
def a1qa_what_is_sql(request):
    return render(request, template(), view_builder(cf.currentFuncName()))

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
'''