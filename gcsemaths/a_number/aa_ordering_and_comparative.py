from django.shortcuts import render
from random import randint
from fractions import Fraction

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[7:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
    return usableModuleList

def previousNext(place):
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
    return f"/gcsemaths/number/{previous_q}", f"/gcsemaths/number/{next_q}"

def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            }

def placePrevNextDiagramConstant(place, diagram=None, constant=''):
    previousQ, nextQ=previousNext(place)
    return place, previousQ, nextQ, diagram, constant

def orderingSetup():
    num1 = randint(1,20)
    num2 = randint(1,20)
    while num1 == num2:
        num2 = randint(1,20)
    if randint(1,2) == 1: num1 = -num1
    if randint(1,2) == 1: num2 = -num2
    if randint(1,2) == 1:
        greaterSmaller = "greater"
    else:
        greaterSmaller = "smaller"
    return num1, num2, greaterSmaller

def fractionSetup():
    den = [2,3,4,5,6,8,9,10,12,15,16]
    d = den[randint(0,len(den)-1)]
    n = randint(1, 2*d-1)
    frac = Fraction(n,d)
    return frac

def decimalSetup():
    den = [1,2,3,4,5,6,8,9,10,12,15,16]
    d = den[randint(0,len(den)-1)]
    n = randint(1, d)
    return round(n/d, 2)

def ordering_numbers(request):
    num1, num2, greaterSmaller = orderingSetup()
    questionBase = f"Which number is {greaterSmaller}: {num1} or {num2}?"
    if greaterSmaller == "greater":
        if num1>num2: answer = num1
        else: answer = num2
    else:
        if num1<num2: answer = num1
        else: answer = num2
    place, previousQ, nextQ, diagram, constant = placePrevNextDiagramConstant(0)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def ordering_decimals(request):
    num1, num2, greaterSmaller = orderingSetup()
    num1 = num1/10
    num2 = num2/10
    questionBase = f"Which number is {greaterSmaller}: {num1} or {num2}?"
    if greaterSmaller == "greater":
        if num1>num2: answer = num1
        else: answer = num2
    else:
        if num1<num2: answer = num1
        else: answer = num2
    place, previousQ, nextQ, diagram, constant = placePrevNextDiagramConstant(1)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))



def ordering_fractions(request):
    if randint(1,2) == 1:
        greaterSmaller = "greater"
    else:
        greaterSmaller = "smaller"
    num1 = fractionSetup()
    num2 = fractionSetup()
    questionBase = f"Which is {greaterSmaller}: {num1} or {num2}?"
    if greaterSmaller == "greater":
        if num1>num2: answer = num1
        else: answer = num2
    else:
        if num1<num2: answer = num1
        else: answer = num2
    if num1 == num2: answer = "Acutally, they're the same!"
    place, previousQ, nextQ, diagram, constant = placePrevNextDiagramConstant(2)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def ordering_fractions_and_decimals(request):
    if randint(1,2) == 1:
        greaterSmaller = "greater"
    else:
        greaterSmaller = "smaller"
    num1 = fractionSetup()
    num2 = decimalSetup()
    questionBase = f"Which is {greaterSmaller}: {num1} or {num2}?"
    if greaterSmaller == "greater":
        if num1>num2: answer = num1
        else: answer = num2
    else:
        if num1<num2: answer = num1
        else: answer = num2
    if num1 == num2: answer = "Acutally, they're the same!"
    place, previousQ, nextQ, diagram, constant = placePrevNextDiagramConstant(3)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def comparative_operators_with_integers(request):
    num1 = randint(1,20)
    num2 = randint(1,20)
    op = ['<', '<=', '>', '>=']
    operator = op[randint(0,len(op)-1)]
    statement = f"{num1}{operator}{num2}"
    answer = eval(statement)
    questionBase = f"Is the following statement true or false: {statement}"
    place, previousQ, nextQ, diagram, constant = placePrevNextDiagramConstant(4)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def comparative_operators_with_fractions(request):
    num1 = fractionSetup()
    num2 = fractionSetup()
    op = ['<', '<=', '>', '>=']
    operator = op[randint(0,len(op)-1)]
    statement = f"{num1}{operator}{num2}"
    answer = eval(statement)
    questionBase = f"Is the following statement true or false: {statement}"
    place, previousQ, nextQ, diagram, constant = placePrevNextDiagramConstant(5)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def comparative_operators_with_fractions_and_decimals(request):
    num1 = fractionSetup()
    num2 = decimalSetup()
    op = ['<', '<=', '>', '>=']
    operator = op[randint(0,len(op)-1)]
    statement = f"{num1}{operator}{num2}"
    answer = eval(statement)
    questionBase = f"Is the following statement true or false: {statement}"
    place, previousQ, nextQ, diagram, constant = placePrevNextDiagramConstant(6)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

