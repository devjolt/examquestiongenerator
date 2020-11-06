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

def pdPowerSetup():
    complist = ["hairdryer", "buzzer", "klaxon warning of immenent alien invasion", "disco light", "subwoofer", "warning becon", "pair of hair straighteners", "robotic monkey", "electric pencil sharpener"]
    component = complist[randint(0, len(complist)-1)]
    option = randint(1,4)
    time = randint(10,2000)
    current = randint(5, 500)/100
    pd = randint(5,20)
    work = round(time * current * pd, 2)
    power = current * pd
    constant = ''
    return component, option, time, current, pd, work, power, constant,



def dab1_work_pd_currentpiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, time, current, pd, work, power, q.constant = pdPowerSetup()
    if option == 1:
        q.questionBase = f"Calculate the energy transfered in {time}s in a {component} where the the potential difference is {pd}v and current is {current}A."
        q.answerBase = f"{work}"
        q.answerUnits = 'J'
    if option == 2:
        q.questionBase = f"Calculate the time taken to transfer {work}J of energy where the the potential difference accross a {component} is {pd}v and the current is {current}A."
        q.answerBase = f"{time}"
        q.answerUnits = 's'
    if option == 3:
        q.questionBase = f"Calculate the average potential difference accross a {component} where a current of {current}A does {work}J of work over {time}s."
        q.answerBase = f"{pd}"
        q.answerUnits = 'v'
    if option == 4:
        q.questionBase = f"Calculate the average current drawn by a {component} where the average potential difference accross the component is {pd}v over {time} seconds and {work}J of work is done."
        q.answerBase = f"{current}A"
        q.answerUnits = 'A'
    qtype = 'type'
    return q.returnAll()

def dab2_power_pd_current4pxax():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, time, current, pd, work, power, q.constant = pdPowerSetup()
    q.questionBase = f"A {pd}V, {round(power,2)}W {component} is connected to a {pd}V battery. Work out:"
    question1= f"the current through the {component}"
    answer1 = f"{current}A"
    question2= f"the energy transfered to the {component} in {time}s."
    answer2 = f"{work}J"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
    ]
    return q.returnAll()

def dab3_pd_charge_energy_power_timepxax6():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, time, current, pd, work, power, q.constant = pdPowerSetup()
    bat = ["large potato battery", "lithium-ion battery", "curiously powerful watch battery", "NiMh battery", "battery made of lemons"]
    battery = bat[randint(0,len(bat)-1)]
    charge = round(current * time, 2)
    q.questionBase = f"A {battery} has an emf of {pd}V. It stores a total charge of {charge}C and has negligible internal resistance. Calculate:"
    question1= f"the maximum energy the {battery} could deliver"
    answer1 = f"{work}J"
    question2= f"the power it would deliver to a {component} drawing {current}A"
    answer2 = f"{power}W"
    question3= f"how long the {battery} would last in seconds if it supplied power at the rate calculated above."
    answer3 = f"{time}s"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
       {'sub_number': 3, 'sub_question': question3, 'sub_answer': answer3, 'sub_mark': 2}, 
    ]
    return q.returnAll()


