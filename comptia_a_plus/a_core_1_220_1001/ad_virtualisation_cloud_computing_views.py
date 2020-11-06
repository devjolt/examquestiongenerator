from django.shortcuts import render
from random import randint
from . import ad_virtualisation_cloud_computing_logic
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

for module in ad_virtualisation_cloud_computing_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'comptia_a_plus/comptiaSelectMultiDrag.html', cf.view_builder('ad_virtualisation_cloud_computing_logic', cf.currentFuncName()))")
