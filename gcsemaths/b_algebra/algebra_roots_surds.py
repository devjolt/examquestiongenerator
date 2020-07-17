from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal
from . import algebra_logic
import sys

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

#allArguments makes it less messy to return dictionary values to templates
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None, question4=None, answer4=None, marks4=None, pre=None, preans = None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            'question4':question4, 'answer4': answer4, 'marks4':marks4,
            'pre':pre, 'preans':preans
            }

def power_of_zero(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_of_one(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_one_to_the_power_of(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_multiplying_powers(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_dividing(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_raising_to(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_raising_two_powers_to(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_with_fractions(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_with_fractions_letters(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_negative(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_negative_letters(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def power_fractional(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_17(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_2a7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans= eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, None, None, None, None, None, None,None, None, None,None, None, None, pre, None))

def surd_rule_3a7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_3b7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_3c7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_4a7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_4b7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_5a7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_5b7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_rule_6a7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, None, None, None, None, None, None,None, None, None,None, None, None, pre, Nones))

def surd_rule_6b7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, pre, preans))

def surd_simplify_addition_a8(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_simplify_addition_b8(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_simplify_addition_c8(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_simplify_area8(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def surd_in_the_form9(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks,a,b,c,d,e,f,g,h,i,j,k,l,pre,preans = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 3, None, None, None, None, None, None,None, None, None,None, None, None, pre, None ))




'''unicode small slash = \u2e0d
unicode fraction slash = \u2044
multiplication: \u00D7
root: \u221A
power of 2: \u00b2
'''
