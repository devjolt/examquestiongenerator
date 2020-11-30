from django.shortcuts import render
from random import randint, randrange
from physics import variety_lists as vl
from physics import universal_classes_functions as ucf

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

def electronCharge():
    return 1.6E-19

def setup():
    option = randint(1,3)
    current = randint(10, 100)/100
    minSecs = ''
    minSecs = "minutes" if randint(0,1) == 1 else "seconds"
    statedTime = randint(5, 15)
    time = statedTime if minSecs == "seconds" else statedTime*60
    charge = round((current * time), 2)
    return option, current, minSecs, statedTime, time, charge

def daa1_charge_current_timepiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    option, current, minSecs, statedTime, time, charge = setup()
    q.constant = None
    if option == 1:
        q.questionBase = f"The current in a certain wire is {current}A.\nCalculate the charge passing a point in the wire during {statedTime} {minSecs}."
        q.answerBase = f"{charge}"
        q.answerUnits = 'C'
    if option == 2:
        q.questionBase = f"{charge} coulombs pass a point in a wire in {statedTime} {minSecs}. What is the average current at this point during this time?"
        q.answerBase = f"{current}"
        q.answerUnits = 'A'
    if option == 3:
        q.questionBase = f"{charge} coulombs pass a point in a wire at a current of {current} Amps. How long does this take?"
        q.answerBase = f"{time}"
        q.answerUnits = 's'
    q.qtype = 'type'
    return q.returnAll()

def daa2_electrons_current_timepiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    option, current, minSecs, statedTime, time, charge = setup()
    eCharge = electronCharge()
    charge = (current * time) / eCharge
    charge = ("{:.2e}".format(charge))
    q.constant = f"e = {eCharge} c"
    if option == 1:
        q.questionBase = f"The current in a certain wire is {current}A.\nCalculate the number of electrons passing a point in the wire during {statedTime} {minSecs}."
        q.answerBase = f"{charge}"
        q.answerUnits = 'C'
    if option == 2:
        q.questionBase = f"{charge} electrons pass a point in a wire in {statedTime} {minSecs}. What is the average current at this point during this time?"
        q.answerBase = f"{current} A"
        q.answerUnits = 'A'
    if option == 3:
        q.questionBase = f"{charge} electrons pass a point in a wire at a current of {current} Amps. How long does this take?"
        q.answerBase = f"{time} s"
        q.answerUnits = 's'
    q.qtype = 'type'
    return q.returnAll()


def daa3_electron_beam_experimentpiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    option, current, minSecs, statedTime, time, charge = setup()
    option = randint(1,2)
    eCharge = electronCharge()
    charge = (current * time)
    numElectrons = charge/eCharge
    numElectrons = ("{:.2e}".format(numElectrons))
    q.constant = f"e = {eCharge} c"
    if option == 1:
        q.questionBase = f"In an electron beam experiment, the beam current is {current}A.\nCalculate the charge which flows along the beam in {statedTime} {minSecs}."
        q.answerBase = f"{charge}"
        q.answerUnits = 'C'
    if option == 2:
        q.questionBase = f"In an electron beam experiment, the beam current is {current}A.\nCalculate the number of electrons which flow along the beam in {statedTime} {minSecs}."
        q.answerBase = f"{numElectrons}"
        q.answerUnits = 'electrons'
    q.qtype = 'type'
    return q.returnAll()


def daa4_rechargable_batterypiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    q.constant = None
    
    option, current, minSecs, statedTime, time, charge = setup()
    option, current2, minSecs2, statedTime2, time2, charge2 = setup()
    charge = (current * time)
    time2 = round(charge/current2, 2)
    
    q.questionBase = f"A certain type of rechargable battery can delivers {current}A for {statedTime} {minSecs} before its voltage drops and it needs to be recharged.\nCalculate the maximum time it could be used before being recharged if the current drawn from it were {current2} Amps."
    q.answerBase = f"{time2}"
    q.answerUnits = ' seconds'
    return q.returnAll()

def daa5_work_PD_and_currentpiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    complist = ["hairdryer", "buzzer", "klaxon warning of immenent alien invasion", "disco light", "subwoofer", "warning becon", "pair of hair straighteners"]
    component = complist[randint(0, len(complist)-1)]
    option = randint(1,4)
    time = randint(10,2000)
    current = randint(5, 500)/100
    pd = randint(5,20)
    work = round(time * current * pd, 2)
    q.constant = None
    if option == 1:
        q.questionBase = f"Calculate the energy transfered in {time}s in a {component} where the the potential difference is {pd}v and current is {current}A."
        q.answerBase = f"{work}"
        q.answerUnits = ' Joules'
    if option == 2:
        q.questionBase = f"Calculate the time taken to transfer {work}J of energy where the the potential difference accross a {component} is {pd}v and the current is {current}A."
        q.answerBase = f"{time}"
        q.answerUnits = 'seconds'
    if option == 3:
        q.questionBase = f"Calculate the average potential difference accross a {component} where a current of {current}A does {work}J of work over {time}s."
        q.answerBase = f"{pd}"
        q.answerUnits = 'v'
    if option == 4:
        q.questionBase = f"Calculate the average current drawn by a {component} where the average potential difference accross the component is {pd}v over {time} seconds and {work}J of work is done."
        q.answerBase = f"{current}"
        q.answerUnits = ' Amps'
    q.qtype = 'type'
    return q.returnAll()