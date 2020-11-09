from django.shortcuts import render
from random import randint, randrange
from alevelmaths import alevelmaths_classes_functions as cf
#from physics import variety_lists as vl

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

def module_path():
    return '/alevelmaths/trigonometry/'


def x_short_long_display():
    q = cf.Question()
    q.questionNumber = 1
    q.questionBase = 'stuff'
    #list of dictionaries containing: sub_number, sub_question, sub_answer, sub_mark
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':'and another things', 'sub_answer':'is this', 'sub_mark':1},
        {'sub_number': 2, 'sub_question':'and another thingsadf', 'sub_answer':'is thisasdf', 'sub_mark':2},
        {'sub_number': 3, 'sub_question':'and another thingsgh', 'sub_answer':'is thisgh', 'sub_mark':3},
        {'sub_number': 4, 'sub_question':'and another thingfgh', 'sub_answer':'is thishgfhg', 'sub_mark':4},
    ]
    q.marksBase = 10
    q.answerBase = 'things'
    q.qtype = 'parts'
    return q.returnAll()


def x_multi_display():
    correct = ('correct1', 'correct2')
    incorrect = ('incorrect1', 'incorrect2', 'incorrect3', 'incorrect4')
    fillers = ('filler1', 'filler2')
    #qtype = multi|select|drag, correct = [], incorrect = [], pairs = [[]], fillers = [], marks, correctRequired, numOptions
    q = cf.SelectMcDrag('multi', correct, incorrect, None, fillers, 1, 1, 4)
    q.questionNumber = 1
    q.questionBase = 'Pick the right one or you will be silly!'
    #list of dictionaries containing: sub_number, sub_question, sub_answer, sub_mark
    return q.returnAll()

def e4a_dfinitions():
    q = cf.Question(cf.currentFuncName())
    pairs = (
        ('secant','	The straight line drawn from the center through one end of a circular arc and intersecting the tangent to the other end of the arc.')
        ('cosecant', ' length of the hypotenuse divided by the length of the opposite side.')
        ()
    )
    
    q.questionBase = f" {atom}"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 1}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 1}, 
    ]
    q.previousQ, q.nextQ = cf.previousNext(
                                list_callable_functions(),
                                cf.currentFuncName()[:2], 0, 2, 
                                cf.currentFuncName(), module_path())
    return q.returnAll()

def a1b_name_part_of_the_atom1():
    q = cf.Question(cf.currentFuncName())
    q.previousQ, q.nextQ = cf.previousNext2(list_callable_functions(),cf.currentFuncName()[:2], 0, 2, cf.currentFuncName(), module_path())
    answers = [["neutrons",["have zero charge", "have the largest mass", "when removed create a different isotope"]],
           ["protons", ["have positive charge", "have second to largest mass", " have the second to largest specific charge", "dictate what element an atom is"]],
           ["electrons", ["have negative charge", "have the highest specific charge", "dictate whether the atom is an ion"]]]
    nuclide = randint(0, len(answers)-1)
    qu = randint(0, len(answers[nuclide][1])-1)
    q.questionBase = f'Name the part of the atom which {answers[nuclide][1][qu]}.'
    q.answerBase= f'The {answers[nuclide][0]} {answers[nuclide][1][qu]}.'
    q.constant = None
    q.previousQ, q.nextQ = cf.previousNext(
                                list_callable_functions(),
                                cf.currentFuncName()[:2], 0, 2, 
                                cf.currentFuncName(), module_path())
    return q.returnAll()

def a1c_ionised6():
    q = cf.Question(cf.currentFuncName())
    q.previousQ, q.nextQ = cf.previousNext2(list_callable_functions(),cf.currentFuncName()[:2], 0, 2, cf.currentFuncName(), module_path())
    atom, mass, element, proton = atomGenerator()   
    losesGains = "loses" if randint(0,1)==0 else "gains"
    electrons = randint(1,4)
    electron = -electrons if losesGains == "loses" else electrons
    q.questionBase = f"An {atom} atom {losesGains} {electrons} electrons."
    question1 = "What is the charge of the atom in Coulombs?"
    answer1= f"{(-electron * electronCharge())} C"
    question2 = "State the number of nucleons the atom contains."
    answer2 = f"{mass}"
    question3 = "Calculate its specific charge in Ckg-1. "
    specificCharge = round((-electron * float(electronCharge())) / (mass * float(nucleonMass())), 2)
    if specificCharge < 0: specificCharge *= -1
    answer3 = f"{specificCharge}"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 1}, 
       {'sub_number': 3, 'sub_question': question3, 'sub_answer': answer3, 'sub_mark': 3}, 
    ]
    return q.returnAll()