from django.shortcuts import render
from random import randint

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[5:]  #only modules used for views are added to the usable list. Non-view modules kept at the top of the file are sliced out!
    return usableModuleList

def previousNext(place): # generates urls for next and previous buttons
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

#just makes everything less messy
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            }

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

def two_components_parallel(request):
    place = 0
    batPd, batI, batP, comp1Pd, comp1P, comp1I,comp2Pd, comp2P, comp2I = parallelCircuitSetup()
    thing = componentSetup()
    questionBase = f"The battery in the circuit above has an emf of {batPd}v and negligible internal resistance is connected to a {comp1Pd}v, {comp1P}W {thing} (a) in parallel with another {comp2Pd}v, {comp2P}W {thing} (b). Calculate:"
    question1 = f'the current through each {thing}'
    question2 = f'the current from the battery'
    question3 = f'the power supplied by the battery.'
    answer1 = f'{thing} 1 = {comp1I}A, {thing} 2 = {comp2I}A'
    answer2 = f'{batI}A'
    answer3 = f'{batP}W'
    constant = ''
    diagram= "/diagrams/physics/circuit_ab_parallel.jpg"
    previousQ, nextQ=previousNext(place)
    marks1 = '2'
    marks2 = '2'
    marks3 = '2'
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None,question1, answer1, marks1, question2, answer2, marks2, question3, answer3, marks3))

def two_components_series(request):
    place = 1
    previousQ, nextQ=previousNext(place)
    batPd, batI, batP, comp1Pd, comp1P, comp1I,comp2Pd, comp2P, comp2I = parallelCircuitSetup()
    thing = componentSetup()
    questionBase = f"A {batPd}v battery of negligible internal resistance as shown above is connected in series with a {comp1Pd}v, {comp1P}W {thing} (a) and a variable resistor (b). When the resistor is adjusted so that the pd. accross the {thing} is {comp2Pd}, work out:"
    question1 = f'the potential difference accross the resistor'
    question2 = f'the current through the {thing}.'
    answer1 = f'{comp1Pd}v'
    answer2 = f'{comp2I}A'
    constant = ''
    marks1 = '2'
    marks2 = '2'
    diagram = "/diagrams/physics/circuit_ab_series.jpg"
    
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, marks1, question2, answer2, marks2))

def two_components_series2(request):
    place = 2
    batPd, batI, batP, comp1Pd, comp1P, comp1I,comp2Pd, comp2P, comp2I = seriesCircuitSetup()
    thing = componentSetup()
    comp1R = round(comp1Pd/comp1I,2)
    comp2R = round(comp2Pd/comp2I,2)
    if comp2R < 0: comp2R *= -1
    previousQ, nextQ=previousNext(place)
    diagram= "/diagrams/physics/circuit_ab_series.jpg"
    constant = ''
    questionBase = f"The {batPd}v battery in the diagram above has negligible internal resistance and is connected in series with a {comp1R} Ohm resistor (a), a {thing} (b) and an ammeter reading {comp1I}A. Calculate:"
    question1 = f'the potential difference accross the resistor'
    answer1 = f'{comp1Pd}v'
    marks1 = '2'
    question2 = f'the resistance of the {thing}.'
    answer2 = f'{comp2R} Ohms'
    marks2 = '2'
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, marks1, question2, answer2, marks2))






