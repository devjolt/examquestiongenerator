from django.shortcuts import render
from random import randint
from . import a_basics_logic
import sys
from sql import sql_helper_functions as hf


def view_builder(name): #Essential for all other view modules
    passed = eval(f"a_basics_logic.{name}()")
    return hf.allArguments2(passed)

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

def template():
    return "sql/sql_multi_choice_dynamic.html"

def test(request):
    print("Here is ip: " + request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    return render(request, template(), view_builder(currentFuncName()))

def a1qa_what_is_sql(request):
    return render(request, template(), view_builder(currentFuncName()))
def a1qb_what_sql_does(request):
    return render(request, template(), view_builder(currentFuncName()))
def a1qc_database_brands(request):
    return render(request, template(), view_builder(currentFuncName()))
def a1qd_database_entities(request):
    return render(request, template(), view_builder(currentFuncName()))
def a2qa_statements(request):
    return render(request, template(), view_builder(currentFuncName()))
def a2qb_commands_starting_statements(request):
    return render(request, template(), view_builder(currentFuncName()))
def a2qc_create_statements(request):
    return render(request, template(), view_builder(currentFuncName()))