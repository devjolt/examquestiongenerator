from django.shortcuts import render
from random import randint
from gcsemaths import gcsemaths_classes_and_functions as cf
import fractions

def list_callable_functions():
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    return entireModuleList

def moduleListGen(qtype = None, low = 0, high = None): #generates a list of all functions with a certain pattern in their name
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    if qtype == None: # use qtype = None to use low high to select slice of list returned in relation to total modules in THIS file, low = -1 for last module only
        count = -1
        poop = []
        for thing in entireModuleList[low:high]:
            count += 1
            poop.append(thing)
    else:
        count = -1
        poop = []
        for thing in entireModuleList:
            if str(thing)[low:high] == qtype: # use qtype ='anystring', low = int representing start of string, high = int representing end of string for modules selected by name
                count += 1
                poop.append(thing)
    print(poop)
    return poop

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_callable_functions(), 'p', 0, 1)

def previousNext(qtype = None, low = 0, high = None, name='', module_path=''):#uses list of all functions to return previous and next modules in list
    modList = cf.moduleListGen(list_callable_functions(), qtype, low, high)
    modDict = {}
    count = -1
    for thing in modList:
        count+=1
        modDict.update({str(thing):count})
    print(modDict)
    place = modDict[name]
    current = modList[place]
    try:
        next_q = modList[place+1]
    except IndexError:
        next_q = modList[0]
    try:
        previous_q = modList[place-1]
    except IndexError:
        previous_q = modList[-1]
    return f"/gcsemaths/exam_non_calc/{previous_q}", f"/gcsemaths/exam_non_calc/{next_q}"

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[10:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
    return usableModuleList

def module_path():
    return '/gcsemaths/exam_non_calc/'

#paper, series, question, name, marks in names
def p1f_18n_9_fraction_half_way3(request):
    number1, number2 = randint(1, 15)/8, randint(1, 15)/8 #create two decimal numbers which can easily be converted to fractions
    while number1 == number2: number2 = randint(1, 16)/8 #make sure second decimal number is different to firs

    printed1 = f"1 {fractions.Fraction(number1-1).numerator}\u2044{fractions.Fraction(number1-1).denominator}" if number1 > 1 else f"{fractions.Fraction(number1).numerator}\u2044{fractions.Fraction(number1).denominator}"
    printed2 = f"1 {fractions.Fraction(number2-1).numerator}\u2044{fractions.Fraction(number2-1).denominator}" if number2 > 1 else f"{fractions.Fraction(number2).numerator}\u2044{fractions.Fraction(number2).denominator}"

    top, bottom = sorted([number1, number2], reverse = True)[0], sorted([number1, number2], reverse = True)[1]
    difference = top - bottom
    mid_point = difference / 2
    answer = bottom + mid_point

    correct = f"1 {fractions.Fraction(answer-1).numerator}\u2044{fractions.Fraction(answer-1).denominator}" if answer > 1 else f"{fractions.Fraction(answer).numerator}\u2044{fractions.Fraction(answer).denominator}" #creates mixed fraction if answer greater than one
    if answer  == 1: correct = '1'

    incorrect = [
        f"{fractions.Fraction(answer-1).numerator}\u2044{fractions.Fraction(answer-1).denominator}" if answer > 1 else f"1 {fractions.Fraction(answer).numerator}\u2044{fractions.Fraction(answer).denominator}",
        f" 1 {fractions.Fraction(difference*2-1).numerator}\u2044{fractions.Fraction(difference*2-1).denominator}" if difference*2 > 1 else f"{fractions.Fraction(difference*2).numerator}\u2044{fractions.Fraction(difference*2).denominator}",
        f"{fractions.Fraction(bottom + difference+ mid_point).numerator}\u2044{fractions.Fraction(bottom + difference + mid_point).denominator}"
    ]
    q = cf.Question(correct, incorrect)
    q.questionBase = f'''Work out the fraction that is halfway between {printed1} and {printed2}. Give your answer as a mixed fraction if appropriate.'''
    q.previousQ, q.nextQ = previousNext("p1", 0, 2, cf.currentFuncName(), module_path())
    q.marks = 3
    q.webLink = 'https://www.mathsisfun.com/fractions_subtraction.html' 
    q.workOn = 'Subtracting fractions'
    return render(request, "gcsemaths/multiChoicePlusReveal.html", cf.allArguments2(q.returnAll()))
