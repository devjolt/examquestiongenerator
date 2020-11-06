from os.path import join
from django.shortcuts import render
from random import randint, randrange
from physics import universal_classes_functions as ucf
from physics import variety_lists as vl

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
    return ucf.moduleListGen(list_callable_functions(), 'd', 0, 1)

def module_path():
    return '/physics/electricity/'

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def emfIntResSetup():
    emf = randint(6,18)
    intRes = randint(5,25)/10
    resistor =randint(2,9)
    totalRes = resistor + intRes
    current = emf/(totalRes)
    terminalPd = current*resistor
    wastedPd = current*intRes
    powerSupplied = current*emf
    powerDelivered = current * current * resistor
    powerWasted = current * current * intRes
    current2 = randint(1,100)/10
    terminalPd2 = current2*resistor
    resistor2 = emf/current2 - intRes

    return emf, intRes, resistor, totalRes, round(current, 3), round(terminalPd,3), round(wastedPd, 3), round(powerSupplied, 3), round(powerDelivered,3), round(powerWasted, 3), round(current2, 3), round(terminalPd2, 3), round(resistor2, 2)

def dbc1_resistance_current_lostpxax8():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    emf, intRes, resistor, totalRes, current, terminalPd, wastedPd, powerSupplied, powerDelivered, powerWasted, current2, terminalPd2, resistor2 = emfIntResSetup()
    q.questionBase = f"A battery of emf {emf}v and internal resistance of {intRes} \u03A9 is connected to a {resistor} \u03A9 resistor. Calculate:"
    question1 = "the total resistance of the circuit"
    question2 = "the current through the battery"
    question3 = "the lost pd"
    question4 = "the pd across the cell terminals."
    marks1, marks2, marks3, marks4= 2, 2, 2, 2
    answer1 = f"{totalRes} \u03A9"
    answer2 = f"{current} A"
    answer3 = f"{wastedPd} v"
    answer4 = f"{terminalPd} v"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': marks1}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': marks2}, 
       {'sub_number': 3, 'sub_question': question3, 'sub_answer': answer3, 'sub_mark': marks3}, 
       {'sub_number': 4, 'sub_question': question4, 'sub_answer': answer4, 'sub_mark': marks4}, 
    ]
    return q.returnAll()

def dbc2_resistance_and_power_lost_pdpxax8():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    emf, intRes, resistor, totalRes, current, terminalPd, wastedPd, powerSupplied, powerDelivered, powerWasted, current2, terminalPd2, resistor2 = emfIntResSetup()
    q.questionBase = f"A battery of emf {emf}v and internal resistance of {intRes} \u03A9 is connected to a {resistor} \u03A9 resistor. Calculate:"
    question1 = "the current"
    question2 = "the terminal pd"
    question3 = f"the power delivered to the {resistor} \u03A9 resistor"
    question4 = "the power wasted in the cell."
    marks1, marks2, marks3, marks4= 2, 2, 2, 2
    answer1 = f"{current} A"
    answer2 = f"{terminalPd} v"
    answer3 = f"{powerDelivered} w"
    answer4 = f"{powerWasted} w"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': marks1}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': marks2}, 
       {'sub_number': 3, 'sub_question': question3, 'sub_answer': answer3, 'sub_mark': marks3}, 
       {'sub_number': 4, 'sub_question': question4, 'sub_answer': answer4, 'sub_mark': marks4}, 
    ]
    return q.returnAll()

def dbc3_changing_current_impact_on_emfpxax5():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    emf, intRes, resistor, totalRes, current, terminalPd, wastedPd, powerSupplied, powerDelivered, powerWasted, current2, terminalPd2, resistor2 = emfIntResSetup()
    q.questionBase = f"The pd acrpss the terminals of a cell was {terminalPd} v when the current from the cell was {current} A, and {terminalPd2} v when the current was {current2} A. Calculate:"
    question1 = "the internal resistance of the cell"
    question2 = "the cell's emf"
    marks1, marks2 = 2, 3
    answer1 = f"{intRes} \u03A9"
    answer2 = f"{emf} v"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': marks1}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': marks2}, 
    ]
    return q.returnAll()
    
def dbc4_changing_current_effect_on_resistorpxax5():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    emf, intRes, resistor, totalRes, current, terminalPd, wastedPd, powerSupplied, powerDelivered, powerWasted, current2, terminalPd2, resistor2 = emfIntResSetup()
    q.questionBase = f"A battery of unknown emf and internal resistance is connected in series with an ammeter and a resistance box. The current was {current} A when the box was set at {resistor} \u03A9 and {current2} A at {resistor2} \u03A9. Calculate:"
    question1 = "the cell's emf"
    question2 = "the cell's internal resistance"
    marks1, marks2 = 2, 3
    answer1 = f"{emf} v"
    answer2 = f"{intRes} \u03A9"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': marks1}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': marks2}, 
    ]
    return q.returnAll()
