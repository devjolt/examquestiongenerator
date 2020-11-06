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

def componentSetup():
    complist = ["screen showing the ambient temperature", "buzzer", "klaxon warning of immenent alien invasion", "disco light", "subwoofer", "warning becon", "robotic monkey", "electric pencil sharpener"]
    component = complist[randint(0, len(complist)-1)]
    return component

def parallelCircuitSetup():
    batteryPd = randint(1,24)
    comp1Pd = batteryPd
    comp1Power = randint(1,24)
    comp1Current = round(comp1Power / comp1Pd, 2)
    comp2Pd = batteryPd
    comp2Power = randint(1,24)
    comp2Current = round(comp2Power / comp2Pd, 2)
    batteryCurrent = comp1Current + comp2Current
    batteryPower = batteryCurrent * batteryPd
    return batteryPd, batteryCurrent, batteryPower, comp1Pd, comp1Power, comp1Current,comp2Pd, comp2Power, comp2Current

def seriesCircuitSetup():
    batteryPd = randint(1,24)
    batteryCurrent = randint(1,24)
    comp1Pd = randint(1,12)
    comp1Current = batteryCurrent
    comp1Power = comp1Current * comp1Pd
    comp2Pd = batteryPd - comp1Pd
    comp2Current = round(batteryCurrent, 2)
    comp2Power = comp2Current * comp2Pd
    batteryPower = batteryCurrent * batteryPd
    return batteryPd, batteryCurrent, batteryPower, comp1Pd, comp1Power, comp1Current,comp2Pd, comp2Power, comp2Current

def dba1_two_components_parallelpxax6():
    q = ucf.Question(ucf.currentFuncName())
    batPd, batI, batP, comp1Pd, comp1P, comp1I,comp2Pd, comp2P, comp2I = parallelCircuitSetup()
    thing = componentSetup()
    q.questionBase = f"The battery in the circuit above has an emf of {batPd}v and negligible internal resistance is connected to a {comp1Pd}v, {comp1P}W {thing} (a) in parallel with another {comp2Pd}v, {comp2P}W {thing} (b). Calculate:"
    question1 = f'the current through each {thing}'
    question2 = f'the current from the battery'
    question3 = f'the power supplied by the battery.'
    answer1 = f'{thing} 1 = {comp1I}A, {thing} 2 = {comp2I}A'
    answer2 = f'{batI}A'
    answer3 = f'{batP}W'
    q.constant = None
    q.diagram= "/diagrams/physics/circuit_ab_parallel.jpg"
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    marks1 = '2'
    marks2 = '2'
    marks3 = '2'
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
       {'sub_number': 3, 'sub_question': question3, 'sub_answer': answer3, 'sub_mark': 2}, 
    ]
    return q.returnAll()

def dba2_two_components_seriespxax4():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    batPd, batI, batP, comp1Pd, comp1P, comp1I,comp2Pd, comp2P, comp2I = parallelCircuitSetup()
    thing = componentSetup()
    q.questionBase = f"A {batPd}v battery of negligible internal resistance as shown above is connected in series with a {comp1Pd}v, {comp1P}W {thing} (a) and a variable resistor (b). When the resistor is adjusted so that the pd. accross the {thing} is {comp2Pd}, work out:"
    question1 = f'the potential difference across the resistor'
    question2 = f'the current through the {thing}.'
    answer1 = f'{comp1Pd}v'
    answer2 = f'{comp2I}A'
    q.constant = None
    marks1 = '2'
    marks2 = '2'
    q.diagram = "/diagrams/physics/circuit_ab_series.jpg"
    
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
    ]
    return q.returnAll()

def dba3_two_components_series2pxax4():
    q = ucf.Question(ucf.currentFuncName())
    batPd, batI, batP, comp1Pd, comp1P, comp1I,comp2Pd, comp2P, comp2I = seriesCircuitSetup()
    thing = componentSetup()
    comp1R = round(comp1Pd/comp1I,2)
    comp2R = round(comp2Pd/comp2I,2)
    if comp2R < 0: comp2R *= -1
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram= "/diagrams/physics/circuit_ab_series.jpg"
    q.constant = None
    q.questionBase = f"The {batPd}v battery in the diagram above has negligible internal resistance and is connected in series with a {comp1R} Ohm resistor (a), a {thing} (b) and an ammeter reading {comp1I}A. Calculate:"
    question1 = f'the potential difference across the resistor'
    answer1 = f'{comp1Pd}v'
    marks1 = '2'
    question2 = f'the resistance of the {thing}.'
    answer2 = f'{comp2R} Ohms'
    marks2 = '2'
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
    ]
    return q.returnAll()
