from django.shortcuts import render
from random import randint

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[4:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
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

def chargeCurrentTime(request):
    place = 0
    previousQ, nextQ=previousNext(place)
    diagram = None
    option, current, minSecs, statedTime, time, charge = setup()
    constant = ''
    if option == 1:
        questionBase = f"The current in a certain wire is {current}A.\nCalculate the charge passing a point in the wire during {statedTime} {minSecs}."
        answer = f"{charge} C"
    if option == 2:
        questionBase = f"{charge} coulombs pass a point in a wire in {statedTime} {minSecs}. What is the average current at this point during this time?"
        answer = f"{current} A"
    if option == 3:
        questionBase = f"{charge} coulombs pass a point in a wire at a current of {current} Amps. How long does this take?"
        answer = f"{time} s"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 2))


def electronsCurrentTime(request):
    place = 1
    previousQ, nextQ=previousNext(place)
    diagram = None
    option, current, minSecs, statedTime, time, charge = setup()
    eCharge = electronCharge()
    charge = (current * time) / eCharge
    charge = ("{:.2e}".format(charge))
    constant = f"e = {eCharge} c"
    if option == 1:
        questionBase = f"The current in a certain wire is {current}A.\nCalculate the number of electrons passing a point in the wire during {statedTime} {minSecs}."
        answer = f"{charge}"
    if option == 2:
        questionBase = f"{charge} electrons pass a point in a wire in {statedTime} {minSecs}. What is the average current at this point during this time?"
        answer = f"{current} A"
    if option == 3:
        questionBase = f"{charge} electrons pass a point in a wire at a current of {current} Amps. How long does this take?"
        answer = f"{time} s"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 2))


def electronBeamExperiment(request):
    place = 2
    previousQ, nextQ=previousNext(place)
    diagram = None
    option, current, minSecs, statedTime, time, charge = setup()
    option = randint(1,2)
    eCharge = electronCharge()
    charge = (current * time)
    numElectrons = charge/eCharge
    numElectrons = ("{:.2e}".format(numElectrons))
    constant = f"e = {eCharge} c"
    if option == 1:
        questionBase = f"In an electron beam experiment, the beam current is {current}A.\nCalculate the charge which flows along the beam in {statedTime} {minSecs}."
        answer = f"{charge} C"
    if option == 2:
        questionBase = f"In an electron beam experiment, the beam current is {current}A.\nCalculate the number of electrons which flow along the beam in {statedTime} {minSecs}."
        answer = f"{numElectrons}"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 2))


def rechargableBattery(request):
    place = 3
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    
    option, current, minSecs, statedTime, time, charge = setup()
    option, current2, minSecs2, statedTime2, time2, charge2 = setup()
    charge = (current * time)
    time2 = round(charge/current2, 2)
    
    questionBase = f"A certain type of rechargable battery can delivers {current}A for {statedTime} {minSecs} before its voltage drops and it needs to be recharged.\nCalculate the maximum time it could be used before being recharged if the current drawn from it were {current2} Amps."
    answer = f"{time2} seconds"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 2))

def workPdCurrent(request):
    place = 4
    previousQ, nextQ=previousNext(place)
    diagram = None
    complist = ["hairdryer", "buzzer", "klaxon warning of immenent alien invasion", "disco light", "subwoofer", "warning becon", "pair of hair straighteners"]
    component = complist[randint(0, len(complist))]
    option = randint(1,4)
    time = randint(10,2000)
    current = randint(5, 500)/100
    pd = randint(5,20)
    work = round(time * current * pd, 2)
    constant = ''
    if option == 1:
        questionBase = f"Calculate the energy transfered in {time}s in a {component} where the the potential difference is {pd}v and current is {current}A."
        answer = f"{work}J"
    if option == 2:
        questionBase = f"Calculate the time taken to transfer {work}J of energy where the the potential difference accross a {component} is {pd}v and the current is {current}A."
        answer = f"{time}s"
    if option == 3:
        questionBase = f"Calculate the average potential difference accross a {component} where a current of {current}A does {work}J of work over {time}s."
        answer = f"{pd}v"
    if option == 4:
        questionBase = f"Calculate the average current drawn by a {component} where the average potential difference accross the component is {pd}v over {time} seconds and {work}J of work is done."
        answer = f"{current}A"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 2))




