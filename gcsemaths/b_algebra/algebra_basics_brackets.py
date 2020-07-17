from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal
from .  import algebra_logic
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

def basics_negative_numbers(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = algebra_logic.basics_negative_numbers()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def basics_multiplying_letters(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = algebra_logic.basics_multiplying_letters()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def basics_collecting_like_terms(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = algebra_logic.basics_collecting_like_terms()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def expand_brackets_three_letters(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = algebra_logic.expand_brackets_three_letters()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def expand_brackets_numbers_letters(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = algebra_logic.expand_brackets_numbers_letters()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def expand_brackets_double(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, a, b, c, d, e, f, g, h, i, j, k, l, pre, preans = algebra_logic.expand_brackets_double()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

