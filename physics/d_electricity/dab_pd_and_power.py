from django.shortcuts import render
from random import randint

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[3:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
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

def work_pd_current(request):
    place = 0
    previousQ, nextQ=previousNext(place)
    diagram = None
    component, option, time, current, pd, work, power, constant = pdPowerSetup()
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

def power_pd_current(request):
    place = 1
    previousQ, nextQ=previousNext(place)
    diagram = None
    component, option, time, current, pd, work, power, constant = pdPowerSetup()
    questionBase = f"A {pd}V, {round(power,2)}W {component} is connected to a {pd}V battery. Work out:"
    question1= f"the current through the {component}"
    answer1 = f"{current}A"
    question2= f"the energy transfered to the {component} in {time}s."
    answer2 = f"{work}J"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2, question2, answer2, 2))

def pd_charge_energy_power_time(request):
    place = 2
    previousQ, nextQ=previousNext(place)
    diagram = None
    component, option, time, current, pd, work, power, constant = pdPowerSetup()
    bat = ["large potato battery", "lithium-ion battery", "curiously powerful watch battery", "NiMh battery", "battery made of lemons"]
    battery = bat[randint(0,len(bat)-1)]
    charge = round(current * time, 2)
    questionBase = f"A {battery} has an emf of {pd}V. It stores a total charge of {charge}C and has negligible internal resistance. Calculate:"
    question1= f"the maximum energy the {battery} could deliver"
    answer1 = f"{work}J"
    question2= f"the power it would deliver to a {component} drawing {current}A"
    answer2 = f"{power}W"
    question3= f"how long the {battery} would last in seconds if it supplied power at the rate calculated above."
    answer3 = f"{time}s"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2, question2, answer2, 2, question3, answer3,2 ))



