from os.path import join
from random import randint
from django.shortcuts import render

'''
POINTERS:
Add select_random_view url to urls.py file
Add a link to appropriate HTML page
Test all questions
Feel great if it all works according to plan!
'''

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[5:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
    return usableModuleList

def previousNext(place): #generates url segments for previous/next buttons.
    myList = moduleList()
    current = myList[place]
    try:
        next_q = myList[place+1]
    except IndexError:
        next_q = myList[0]
    try:
        previous_q = myList[place-1]
    except IndexError:
        previous_q = myList[-1]
    return f"/physics/electricity/{previous_q}", f"/physics/electricity/{next_q}"

#allArguments makes it less messy to return dictionary values to templates
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None, question4=None, answer4=None, marks4=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            'question4':question4, 'answer4': answer4, 'marks4':marks4
            }

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    modList = moduleList()
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4  = eval(f"{modList[randint(0,len(modList)-1)]}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4 ))

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

def rand_resistance_current_lost_pd():
    previousQ, nextQ, diagram, constant = None, None, None, None
    emf, intRes, resistor, totalRes, current, terminalPd, wastedPd, powerSupplied, powerDelivered, powerWasted, current2, terminalPd2, resistor2 = emfIntResSetup()
    questionBase = f"A battery of emf {emf}v and internal resistance of {intRes} \u03A9 is connected to a {resistor} \u03A9 resistor. Calculate:"
    question1 = "the total resistance of the circuit"
    question2 = "the current through the battery"
    question3 = "the lost pd"
    question4 = "the pd across the cell terminals."
    marks1, marks2, marks3, marks4= 2, 2, 2, 2
    answer1 = f"{totalRes} \u03A9"
    answer2 = f"{current} A"
    answer3 = f"{wastedPd} v"
    answer4 = f"{terminalPd} v"
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4 

def rand_resistance_power_lost_pd():
    previousQ, nextQ, diagram, constant = None, None, None, None
    emf, intRes, resistor, totalRes, current, terminalPd, wastedPd, powerSupplied, powerDelivered, powerWasted, current2, terminalPd2, resistor2 = emfIntResSetup()
    questionBase = f"A battery of emf {emf}v and internal resistance of {intRes} \u03A9 is connected to a {resistor} \u03A9 resistor. Calculate:"
    question1 = "the current"
    question2 = "the terminal pd"
    question3 = f"the power delivered to the {resistor} \u03A9 resistor"
    question4 = "the power wasted in the cell."
    marks1, marks2, marks3, marks4= 2, 2, 2, 2
    answer1 = f"{current} A"
    answer2 = f"{terminalPd} v"
    answer3 = f"{powerDelivered} w"
    answer4 = f"{powerWasted} w"
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4 

def rand_changing_current_emf():
    previousQ, nextQ, diagram, constant = None, None, None, None
    emf, intRes, resistor, totalRes, current, terminalPd, wastedPd, powerSupplied, powerDelivered, powerWasted, current2, terminalPd2, resistor2 = emfIntResSetup()
    questionBase = f"The pd acrpss the terminals of a cell was {terminalPd} v when the current from the cell was {current} A, and {terminalPd2} v when the current was {current2} A. Calculate:"
    question1 = "the internal resistance of the cell"
    question2 = "the cell's emf"
    marks1, marks2 = 2, 3
    answer1 = f"{intRes} \u03A9"
    answer2 = f"{emf} v"
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, marks1,  question2, answer2, marks2, None, None, None, None, None, None
    
def rand_changing_current_resistor():
    previousQ, nextQ, diagram, constant = None, None, None, None
    emf, intRes, resistor, totalRes, current, terminalPd, wastedPd, powerSupplied, powerDelivered, powerWasted, current2, terminalPd2, resistor2 = emfIntResSetup()
    questionBase = f"A battery of unknown emf and internal resistance is connected in series iwth an ammeter and a resistance box. The current was {current} A when the box was set at {resistor} \u03A9 and {current2} A at {resistor2} \u03A9. Calculate:"
    question1 = "the cell's emf"
    question2 = "the cell's internal resistance"
    marks1, marks2 = 2, 3
    answer1 = f"{emf} v"
    answer2 = f"{intRes} \u03A9"
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, marks1,  question2, answer2, marks2, None, None, None, None, None, None
