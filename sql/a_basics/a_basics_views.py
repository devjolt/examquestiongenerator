from django.shortcuts import render
from random import randint
from . import a_basics_logic
import sys
from sql import sql_classes_and_functions as cf

'''
#generates a whole section of 15-16 marks
def section_generator(request):
    return render(request, "physics_section.html", view_builder(currentFuncName()))

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
#selects a function at random from moduleList generated list and returns everything needed to generate a view
'''
def moduleListGen(qtype = None, low = 0, high = None): #generates a list of all functions with a certain pattern in their name
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    if qtype == None: # use qtype = None to use low high to select slice of list returned in relation to total modules in THIS file, low = -1 for last module only
        count = -1
        poop = []
        for thing in entireModuleList[low:high]:
            count += 1
            poop.append(thing)
    else:
        count = -1
        poop = []
        for thing in entireModuleList:
            if str(thing)[low:high] == qtype: # use qtype ='anystring', low = int representing start of string, high = int representing end of string for modules selected by name
                count += 1
                poop.append(thing)
    print(poop)
    return poop

def modulesList():#this is used by urls to automatically generate all urls for this module
    return moduleListGen('a', 0, 1)

def view_builder(name): #returns template dictionary
    passed = eval(f"a_basics_logic.{name}()")
    return cf.allArguments2(passed)

def template():
    return "sql/sql_multi_choice_dynamic.html"

def test(request):
    print("Here is ip: " + request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    return render(request, template(), cf.view_builder(hf.currentFuncName()))

for module in a_basics_logic.modulesList():
    exec(f"def {module}(request):\n\treturn render(request, template(), view_builder(cf.currentFuncName()))")

"""
def a1qa_what_is_sql(request):
    return render(request, template(), view_builder(cf.currentFuncName()))
def a1qb_what_sql_does(request):
    return render(request, template(), view_builder(cf.currentFuncName()))
def a1qc_database_brands(request):
    return render(request, template(), view_builder(cf.currentFuncName()))
def a1qd_database_entities(request):
    return render(request, template(), view_builder(cf.currentFuncName()))
def a2qa_statements(request):
    return render(request, template(), view_builder(cf.currentFuncName()))
def a2qb_commands_starting_statements(request):
    return render(request, template(), view_builder(cf.currentFuncName()))
def a2qc_create_statements(request):
    return render(request, template(), view_builder(cf.currentFuncName()))
"""