from django.shortcuts import render
from random import randint

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[6:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
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

def resistorSeriesSetup():
    batPd = randint(1,24)
    r1r, r2r = randint(1,24), randint(1,24)
    rt = r1r+r2r
    I= round(batPd/rt)
    r1Pd, r2Pd = r1r * I, r2r * I
    r1I, r2I = I, I
    q = "series"
    return q, batPd, I, rt, r1r, r1Pd, r1I, r2r, r2Pd, r2I

def resistorParallelSetup():
    batPd = randint(1,24)
    r1r, r2r = randint(1,24), randint(1,24)
    rt = round(1/(1/r1r + 1/r2r), 3)
    I = round(batPd/rt, 2)
    r1Pd,r2Pd = batPd, batPd
    r1I,r2I = r1Pd / r1r,  r2Pd / r2r
    q = "parallel"
    return q, batPd, I, rt, r1r, r1Pd, r1I, r2r, r2Pd, r2I

def oneSeriesTwoParallelSetup():
    #r1 and r2 in parallel, r3 in series
    batPd = randint(1,24)
    r1r, r2r, r3r = randint(1,24), randint(1,24), randint(1,24)
    rt = (1/(1/r1r + 1/r2r)) + r3r
    I = round(batPd/rt, 2)
    r3Pd = r3r * I
    r1Pd = round((batPd - r3Pd) / r1r, 2)
    r2Pd = round((batPd - r3Pd) / r2r, 2)
    r1I, r2I, r3I = round(r1Pd / r1r, 2), round(r2Pd / r2r, 2), I
    return batPd, I, rt, r1r, r1Pd, r1I, r2r, r2Pd, r2I, r3r, r3Pd, r3I

def parallelIncludingTwoSeries():
    #All resistors in parallel, with r1 and r2 in series and r3 in its own branch
    batPd = randint(1,24)
    r1r, r2r, r3r = randint(1,24), randint(1,24), randint(1,24)
    r3Pd = batPd
    rt = 1/((1/(r1r + r2r)) + 1/r3r)
    I = round(batPd/rt, 2)
    r3I = r3Pd / r3r
    r1I, r2I = I-r3I, I-r3I
    r1Pd, r2Pd = r1r * r1I, r2r * r2I
    return batPd, I, rt, r1r, r1Pd, r1I, r2r, r2Pd, r2I, r3r, r3Pd, r3I

def seriesParallelChoice(request):
    place = 0
    choice = randint(0,1)
    diagram = None
    if choice == 0:q, batPd, I, rt, r1r, r1Pd, r1I, r2r, r2Pd, r2I = resistorSeriesSetup()
    else: q, batPd, I, rt, r1r, r1Pd, r1I, r2r, r2Pd, r2I = resistorParallelSetup()
    if choice == 0: diagram = "/diagrams/physics/circuit_ab_series.jpg" 
    else: diagram = "/diagrams/physics/circuit_ab_parallel.jpg"
    previousQ, nextQ=previousNext(place)
    constant = ''
    questionBase = f"Calculate the total resistance of a {r1r} \u03A9 and a {r2r} \u03A9 resistor at a and b in {q}"
    answer = f"{rt} \u03A9"
    marks = '2'
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

def oneSeriesTwoParallel(request):
    place = 1
    batPd, I, rt, r1r, r1Pd, r1I, r2r, r2Pd, r2I, r3r, r3Pd, r3I = oneSeriesTwoParallelSetup()

    choice = randint(0,2)
    if choice == 0: res, power = r3r, r3I * r3Pd
    if choice == 1: res, power = r1r, r1I * r1Pd
    if choice == 2: res, power = r2r, r2I * r2Pd

    diagram = "/diagrams/physics/circuit_ab_series.jpg"
    previousQ, nextQ=previousNext(place)

    questionBase = f"A {batPd}v battery is setup in a circuit where a and b are resitsors in parallel {r1r} and {r2r} \u03A9 and c is a {r3r} \u03A9 resistor in series."
    answer = None
    marks = None
    question1 = f"What is the total resistance of this circuit?"
    question2 = f"What is the current supplied by the battery?"
    question3 = f"What is the power supplied to the {res} \u03A9 resistor?"
    answer1 = f"{round(rt,2)} \u03A9"
    answer2 = f"{round(I, 2)} A"
    answer3 = f"{round(power, 2)} W"
    constant = ''
    marks1 = 2
    marks2 = 2
    marks3 = 2
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1, question2, answer2, marks2, question3, answer3, marks3))

def oneSeriesTwoParallelSecond(request):
    place = 2
    batPd, I, rt, r1r, r1Pd, r1I, r2r, r2Pd, r2I, r3r, r3Pd, r3I = parallelIncludingTwoSeries()

    power1 = r1I * r1Pd
    power2 = r2I * r2Pd
    power3 = r3I * r3Pd
    powerBat = power1 + power2 + power3

    
    previousQ = '/physics/electricity/oneSeriesTwoParallel'
    nextQ='/physics/electricity/element'
    diagram = "/diagrams/physics/circuit_ab_series_parallel_c.jpg"
    constant = ''

    questionBase = f"A series of two resistors with a resistance of {r1r} \u03A9 at a and {r2r} \u03A9 at b are set up in parallel with a {r3r} \u03A9 resistor at c in a circuit with a {batPd}v battery as above."
    question1 = f"What is the total resistance of this circuit?"
    question2 = f"What is the current supplied by the battery?"
    question3 = f"What is the power supplied to each resistor?"
    answer1 = f"{round(rt,2)} \u03A9"
    answer2 = f"{round(I, 2)} A"
    answer3 = f"{round(r1r, 2)} \u03A9 resistor = {round(power1, 2)} W, {r2r} \u03A9 resistor = {round(power2,2)} W, {r3r} \u03A9 resistor = {round(power3, 2)} W"
    constant = ''
    marks1 = 2
    marks2 = 2
    marks3 = 3
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, marks1, question2, answer2, marks2, question3, answer3, marks3))

def element(request):
    place = 3
    pd = randint(1,24)
    p = randint(1,24)
    i = p/pd
    r = pd/i

    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''

    questionBase =f"Calculate the resistance of a light bulb designed to operate at {p} watts and {pd} volts."
    answer =f'{round(r,2)} \u03A9'
    marks = 2
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks))

