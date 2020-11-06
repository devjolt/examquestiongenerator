from django.shortcuts import render
from random import randint, randrange
from testapp import testapp_classes_functions as cf
#from testapp import variety_lists as vl

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
    return cf.moduleListGen(list_callable_functions(), 'd', 0, 1)

def module_path():
    return '/testapp/physics_dev/'

#def (printable)(interactive)(section a)(section b)(marks)

def d_type_piax1():#printable
    q = cf.Question(cf.currentFuncName())
    q.questionBase = 'printable interactive typed question: 3 onkeys -2'
    q.qtype = 'type'
    q.answerUnits = 'onkies'
    q.answerBase = 1
    return q.returnAll()
'''
def d_type_piab1():#printable
    q = cf.Question(cf.currentFuncName())
    q.questionBase = 'printable interactive typed or multi choice question: 3-2'
    q.answerBase = 1
    return q.returnAll()
'''
def d_type_parts_pxax3():
    q = cf.Question(cf.currentFuncName())
    q.questionBase = 'printable non-interactive typed question: Mary had a...'
    q.questionPartList = (
        {'sub_number': 1, 'sub_question':'3+2', 'sub_answer':5, 'sub_mark': 1},
        {'sub_number': 2, 'sub_question':'little', 'sub_answer':'lamb', 'sub_mark': 2},
    )
    q.marksBase = 3
    return q.returnAll()

def d_multi_pixb1():
    correct = ['correct']
    incorrect = ['incorrect1', 'incorrect2', 'incorrect3', 'incorrect4']
    #func_name, qtype = multi|select|drag,  correct = [], incorrect = [], pairs = [[]], fillers = [], marks, correctRequired, numOptions
    q = cf.SelectMcDrag(cf.currentFuncName(), 'multi', correct, incorrect,None, (), 1, 1, 4)
    q.questionBase = f"What do you think?"
    return q.returnAll()

def d_multi2_pixb1():
    correct = ['right']
    incorrect = ['wrong1', 'wrong2', 'wrong3', 'wrong4']
    q = cf.SelectMcDrag(cf.currentFuncName(), 'multi', correct, incorrect,None, (), 1, 1, 4)
    q.questionBase = f"What do you think?"
    return q.returnAll()


#def piab