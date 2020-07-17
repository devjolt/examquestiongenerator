from django.shortcuts import render
from random import randint

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[4:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
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

def resistivitySetup():
    r = [["copper", 1.7e-8], ["constantan", 5e-7],["carbon",3e-5],["silicon",2300],["PVC",10e14]]
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

#allArguments makes it less messy to return dictionary values to templates
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None, question4=None, answer4=None, marks4=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            'question4':question4, 'answer4': answer4, 'marks4':marks4
            }

def resistance_pd_current(request):
    place = 0
    previousQ, nextQ=previousNext(place)
    diagram = None
    component, option, pd, current, resistance, length, material, resistivityConstant, area = resistancePdCurrentSetup()
    constant = ''
    if option == 1:
        questionBase = f"The current through a {component} is {current}A when the pd across it is {pd}V. Calculate the resistance at this current."
        answer = f"{resistance} \u03A9"
    if option == 2:
        questionBase = f"The current through a {component} is {current}A and the resistance is {resistance} \u03A9 What is the pd accross this component?"
        answer = f"{pd}V"
    if option == 3:
        questionBase = f"The pd accross a {component} is {pd}V when the resistance is {resistance} \u03A9. Calculate the current through this component."
        answer = f"{current}A"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase,  answer, 2))

def resistivity_uniform_wire(request):
    place = 1
    previousQ, nextQ=previousNext(place)
    diagram = None
    component, option, pd, current, resistance, length, material, resistivityConstant, area = resistancePdCurrentSetup()
    constant = ''
    resistivityConstant = ("{:.2e}".format(resistivityConstant))
    if option == 1:
        questionBase = f"Calculate the resistance of a uniform {material} cable of a diameter {round(area/3.15159, 2)} and length {length}m. The resistivity of the material is {resistivityConstant} Ohm metres."
        answer = f"{resistance} \u03A9"
    if option == 2:
        questionBase = f"What is the area of a uniform {material} wire of length {length}m and resistance of {resistance} \u03A9 if the resistivity of the material is {resistivityConstant} Ohm metres?"
        answer = f"{area}metres squared"
    if option == 3:
        questionBase = f"What is the length of a uniform {material} wire with resistance of {resistance} \u03A9 and radius of {round((area/3.15159)/2,2)} if the resistivity of the material is {resistivityConstant} Ohm metres?"
        answer = f"{length}m"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase,  answer, 2))

def resistivity_rectangular_wire(request):
    place = 2
    previousQ, nextQ=previousNext(place)
    diagram = None
    component, option, pd, current, resistance, length, material, resistivityConstant, area = resistancePdCurrentSetup()
    constant = ''
    thickness = randint(1,20)/1000
    resistivityConstant = ("{:.2e}".format(resistivityConstant))
    radius = ("{:.2e}".format(area/3.14159265 * 2))
    width = ("{:.2e}".format(area/thickness))
    if option == 1:
        questionBase = f"Calculate the resistance of a piece of rectangular {material} of thickness {thickness}m, width of {width}m and length {length}m. The resistivity of the material is {resistivityConstant} Ohm metres."
        answer = f"{resistance} \u03A9"
    if option == 2:
        questionBase = f"What is the cross-sectional area of a rectangular piece of {material} of length {length}m and resistance of {resistance} \u03A9 if the resistivity of the material is {resistivityConstant} Ohm metres?"
        answer = f"{area}metres squared"
    if option == 3:
        questionBase = f"What is the length of a rectangular piece of {material} with resistance of {resistance} \u03A9 and radius of {radius}m if the resistivity of the material is {resistivityConstant} Ohm metres?"
        answer = f"{length}m"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase,  answer, 2))

def two_part_resistivity(request):
    place = 3
    previousQ, nextQ=previousNext(place)
    diagram = None
    component, option, pd, current, resistance, length, material, resistivityConstant, area = resistancePdCurrentSetup()
    constant = ''
    resistivityConstant = ("{:.2e}".format(resistivityConstant))
    questionBase = f'A {material} wire of uniform diameter {round(area/3.15159, 2)}m  and length {length}m has a resistance of {resistance} \u03A9.'
    question1 = f"What is its resistivity?"
    answer1 = f"{resistivityConstant} \u03A9 metres"
    randOhm = randint(1,3)
    question2 = f"How long would a length of this wire with {randOhm} \u03A9 be?"
    answer2 = f"{(randOhm*area)/float(resistivityConstant)}m"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2, 2))
