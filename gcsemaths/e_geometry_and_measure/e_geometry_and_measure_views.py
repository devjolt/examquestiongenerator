from django.shortcuts import render
from random import randint
from . import e_geometry_and_measure_logic
import sys
from gcsemaths import gcsemaths_classes_functions as cf

def module_path():
    return '/gcsemaths/e_geometry_and_measure/'

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

for module in e_geometry_and_measure_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'gcsemaths/gcsemathsPaperMarkschemeReveal.html', cf.view_builder('e_geometry_and_measure_logic', cf.currentFuncName()))")
    
