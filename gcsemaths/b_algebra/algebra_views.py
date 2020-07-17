from django.shortcuts import render
from random import randint
from . import algebra_logic
import sys
from gcsemaths import gcsemaths_helper_functions as phf

def view_builder(name):
    passed = eval(f"algebra_logic.{name}()")
    return phf.allArguments2(passed)
    
currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

#selects a random selection module (as below) at random from algebra_logic.py 
def select_random(request):
    passed = algebra_logic.select_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

#selects a random module from one of the categories in title
def algebra_basics_random(request):
    passed = algebra_logic.algebra_basics_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

def algebra_brackets_random(request):
    passed = algebra_logic.algebra_brackets_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

def algebra_powers_random(request):
    passed = algebra_logic.algebra_powers_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

def algebra_surds_random(request):
    passed = algebra_logic.algebra_surds_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

def algebra_solve_random(request):
    passed = algebra_logic.algebra_solve_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

def algebra_factorising_random(request):
    passed = algebra_logic.algebra_factorising_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

#Basics

def basics_negative_numbers(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def basics_multiplying_letters(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def basics_collecting_like_terms(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

#Expanding brackets
def expand_brackets_three_letters(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def expand_brackets_numbers_letters(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def expand_brackets_double(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

#Powers
def power_of_zero(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_of_one(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_one_to_the_power_of(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_multiplying_powers(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_dividing(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_raising_to(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_raising_two_powers_to(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_with_fractions(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_with_fractions_letters(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_negative(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_negative_letters(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def power_fractional(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

#Surds
def surd_rule_17(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_2a7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_3a7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_3b7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_3c7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_4a7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_4b7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_5a7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_5b7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_6a7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_rule_6b7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_simplify_addition_a8(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_simplify_addition_b8(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_simplify_addition_c8(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_simplify_area8(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def surd_in_the_form9(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

#factorising
def factorising_two_letters(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def factorising_more_letters(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

#solving x
def solve_divide(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def solve_collectint_divide(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def solve_collectx_collectint_divide(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def solve_collectx_collectint_divide_brackets(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def solve_collectx_collectint_divide_brackets_double(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def solve_posneg_collectx_collectint_divide_brackets(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def solve_posneg_collectx_collectint_divide_brackets_fractions(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def solve_posneg_collectx_collectint_divide_brackets_first_fraction(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def solve_posneg_collectx_collectint_divide_brackets_second_fraction(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

['def moduleListGen(request):', 'def select_random(request):', 'def algebra_basics_random(request):', 'def algebra_brackets_random(request):', 'def algebra_powers_random(request):', 'def algebra_surds_random(request):', 'def algebra_solve_random(request):', 'def basics_negative_numbers(request):', 'def basics_multiplying_letters(request):', 'def basics_collecting_like_terms(request):', 'def expand_brackets_three_letters(request):', 'def expand_brackets_numbers_letters(request):', 'def expand_brackets_double(request):', 'def power_of_zero(request):', 'def power_of_one(request):', 'def power_one_to_the_power_of(request):', 'def power_multiplying_powers(request):', 'def power_dividing(request):', 'def power_raising_to(request):', 'def power_raising_two_powers_to(request):', 'def power_with_fractions(request):', 'def power_with_fractions_letters(request):', 'def power_negative(request):', 'def power_negative_letters(request):', 'def power_fractional(request):', 'def surd_rule_17(request):', 'def surd_rule_3a7(request):', 'def surd_rule_3b7(request):', 'def surd_rule_3c7(request):', 'def surd_rule_4a7(request):', 'def surd_rule_4b7(request):', 'def surd_rule_5a7(request):', 'def surd_rule_5b7(request):', 'def surd_rule_6a7(request):', 'def surd_rule_6b7(request):', 'def surd_simplify_addition_a8(request):', 'def surd_simplify_addition_b8(request):', 'def surd_simplify_addition_c8(request):', 'def surd_simplify_area8(request):', 'def surd_in_the_form9(request):', 'def factorising_two_letters(request):', 'def factorising_more_letters(request):', 'def solve_divide(request):', 'def solve_collectint_divide(request):', 'def solve_collectx_collectint_divide(request):', 'def solve_collectx_collectint_divide_brackets(request):', 'def solve_collectx_collectint_divide_brackets_double(request):', 'def solve_negative_collectx_collectint_divide_brackets(request):', 'def solve_posneg_collectx_collectint_divide_brackets(request):', 'def solve_posneg_collectx_collectint_divide_brackets_fractions(request):', 'def solve_posneg_collectx_collectint_divide_brackets_first_fraction(request):', 'def solve_posneg_collectx_collectint_divide_brackets_second_fraction(request):']