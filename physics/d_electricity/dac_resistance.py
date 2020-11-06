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

def resistivitySetup():
    r = [["copper", 1.7e-8], ["constantan", 5e-7],["carbon",3e-5],["silicon",2300]]
    selection = randint(0, len(r)-1)
    material, resistivity = r[selection][0], r[selection][1]
    return material, resistivity

def resistancePdCurrentSetup():
    complist = ["hairdryer", "buzzer", "klaxon warning of immenent alien invasion", "disco light", "subwoofer", "warning becon", "pair of hair straighteners", "robotic monkey", "electric pencil sharpener"]
    component = complist[randint(0, len(complist)-1)]
    option = randint(1,3)
    pd = randint(1,2000)/1000
    current = randint(5, 1000)/100
    resistance = round(pd/current, 3)
    length = randint(5,200)/10
    material, resistivityConstant = resistivitySetup()
    area =(resistivityConstant * length)/resistance
    return component, option, pd, current, resistance, length, material, resistivityConstant, area

def dac1_resistance_pd_currentpiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, pd, current, resistance, length, material, resistivityConstant, area = resistancePdCurrentSetup()
    q.constant = None
    if option == 1:
        q.questionBase = f"The current through a {component} is {current}A when the pd across it is {pd}V. Calculate the resistance at this current."
        q.answerBase= f"{resistance}"
        q.answerUnits = ' \u03A9'
    if option == 2:
        q.questionBase = f"The current through a {component} is {current}A and the resistance is {resistance} \u03A9 What is the pd accross this component?"
        q.answerBase= f"{pd}"
        q.answerUnits = ' V'
    if option == 3:
        q.questionBase = f"The pd across a {component} is {pd}V when the resistance is {resistance} \u03A9. Calculate the current through this component."
        q.answerBase= f"{current}"
        q.answerUnits = ' A'
    q.qtype = 'type'
    return q.returnAll()

def dac2_resistivity_uniform_wirepiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, pd, current, resistance, length, material, resistivityConstant, area = resistancePdCurrentSetup()
    q.constant = None
    resistivityConstant = ("{:.2e}".format(resistivityConstant))
    if option == 1:
        q.questionBase = f"Calculate the resistance of a uniform {material} cable of a diameter {round(area/3.15159, 2)} and length {length}m. The resistivity of the material is {resistivityConstant} Ohm metres."
        q.answerBase= f"{resistance}"
        q.answerUnits = ' \u03A9'
    if option == 2:
        q.questionBase = f"What is the area of a uniform {material} wire of length {length}m and resistance of {resistance} \u03A9 if the resistivity of the material is {resistivityConstant} Ohm metres?"
        q.answerBase= f"{area}"
        q.answerUnits = ' m\u00b2'
    if option == 3:
        q.questionBase = f"What is the length of a uniform {material} wire with resistance of {resistance} \u03A9 and radius of {round((area/3.15159)/2,2)} if the resistivity of the material is {resistivityConstant} Ohm metres?"
        q.answerBase= f"{length}"
        q.answerUnits = ' m'
    q.qtype = 'type'
    return q.returnAll()

def dac3_resistivity_rectangular_wirepiax2():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, pd, current, resistance, length, material, resistivityConstant, area = resistancePdCurrentSetup()
    q.constant = None
    thickness = randint(1,20)/1000
    resistivityConstant = ("{:.2e}".format(resistivityConstant))
    radius = ("{:.2e}".format(area/3.14159265 * 2))
    width = ("{:.2e}".format(area/thickness))
    if option == 1:
        q.questionBase = f"Calculate the resistance of a piece of rectangular {material} of thickness {thickness}m, width of {width}m and length {length}m. The resistivity of the material is {resistivityConstant} Ohm metres."
        q.answerBase= f"{resistance}"
        q.answerUnits=' \u03A9'
    if option == 2:
        q.questionBase = f"What is the cross-sectional area of a rectangular piece of {material} of length {length}m and resistance of {resistance} \u03A9 if the resistivity of the material is {resistivityConstant} Ohm metres?"
        q.answerBase= f"{area}"
        q.answerUnits = ' m\u00b2'
    if option == 3:
        q.questionBase = f"What is the length of a rectangular piece of {material} with resistance of {resistance} \u03A9 and radius of {radius}m if the resistivity of the material is {resistivityConstant} Ohm metres?"
        q.answerBase= f"{length}"
        q.answerUnits = ' m'
    q.qtype = 'qtype'
    return q.returnAll()

def dac4_two_part_resistivitypxax4():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, pd, current, resistance, length, material, resistivityConstant, area = resistancePdCurrentSetup()
    q.constant = None
    resistivityConstant = ("{:.2e}".format(resistivityConstant))
    q.questionBase = f'A {material} wire of uniform diameter {round(area/3.15159, 2)}m  and length {length}m has a resistance of {resistance} \u03A9.'
    question1 = f"What is its resistivity?"
    answer1 = f"{resistivityConstant} \u03A9 metres"
    randOhm = randint(1,3)
    question2 = f"How long would a length of this wire with {randOhm} \u03A9 be?"
    answer2 = f"{(randOhm*area)/float(resistivityConstant)}m"
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
    ]
    return q.returnAll()
