from django.shortcuts import render
from random import randint
from . import e4_co_arc_logic
import sys
from alevelmaths import alevelmaths_classes_functions as cf

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

def modulesList():#used by urls to generate paths for funcs in this file
    return cf.moduleListGen(list_callable_functions(), 'e', 0, 1)

def current_module():
    return "e_trigonometry"


for module in e4_co_arc_logic.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f'''def {module}(request):\n\treturn render(
                request,     
                'alevelmaths/alevelmathsPaperMSReveal.html', 
                cf.view_builder('e4_co_arc_logic', cf.currentFuncName()))''')

#for module in e1b_simple_harmonic_motion_logic.modulesList(): #generates every logic function as a view, depending on their required template
#    exec(f"def {module}(request):\n\treturn render(request, 'physics/physicsSectionABReveal.html', cf.view_builder2('e1b_simple_harmonic_motion_logic', cf.currentFuncName()))")
