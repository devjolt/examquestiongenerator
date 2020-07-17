from django.shortcuts import render
from random import randint

from os.path import join
from random import randint

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = thing[7:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
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

#allArguments makes it less messy to return dictionary values to templates
def allArguments(previousQ='', nextQ='', diagram='', questionBase='', line =None, answer = None, marks = None, question1=None, answer1=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,
            'questionBase':questionBase, 'line':line, 'marks':marks,
            'question1':question1, 'answer1': answer1, 
            }

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random_view():
    moduleList = makeUsableModuleList()
    
    previousQ, nextQ, constant, questionBase, line, marks, question1, answer1 = eval(f"{newThing[randint(0,len(newThing)-1)]}()")
    return render(request, "multiChoiceCodeButtons.html", allArguments(previousQ, nextQ, questionBase, line, marks, question1, answer1))

def a3_bitwise_operators():
    previousQ, nextQ=previousNext(place)
    diagram = None

    bitwiseOps = ["<<", ">>", "&", "|"]
    bitwiseOp1 = bitwiseOps[randint(0,(len(bitwiseOps)-1))]
    bitwiseOp2 = bitwiseOps[randint(0,(len(bitwiseOps)-1))]
    regularOps = ["+", "-"]
    regularOp = regularOps[randint(0,(len(regularOps)-1))]

    numbers = [x for x in range(1,4)]
    number1 = numbers[randint(0,(len(numbers)-1))]
    number2 = numbers[randint(0,(len(numbers)-1))]
    number3 = numbers[randint(0,(len(numbers)-1))]
    number4 = numbers[randint(0,(len(numbers)-1))]

    line = f"{number1} {bitwiseOp1} {number2}\n"

    questionBase = (f"What is the output of the following code:")
    
    try:
        thing = eval(line)
    except BaseException:
        thing = "Error"

    if thing == 0: correct, incorrect1, incorrect2, incorrect3 = thing, "Error", numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)], numbers[randint(0, len(numbers)-1)]
    elif thing == "Error": correct, incorrect1, incorrect2, incorrect3 = thing, numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)], 0, numbers[randint(0, len(numbers)-1)]-numbers[randint(0, len(numbers)-1)]
    else: correct, incorrect1, incorrect2, incorrect3 = thing, "Error", 0, numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)]

    order = []
    for i in range(4):
        n = randint(1,4)
        while n in order:
            n = randint(1,4)
        order.append(n)

    answers = [correct, incorrect1, incorrect2, incorrect3]

    answersDict = {key: value for key, value in sorted(zip(order, answers))}

    question1=''
    for key, value in answersDict.items():
        question1+= str(key) + ". " + str(value) + '\n'

    return previousQ, nextQ, diagram, questionBase, line, 1, question1, correct




