from django.shortcuts import render
from random import randint, randrange
from gcsemaths import gcsemaths_classes_functions as cf
import fractions
import itertools

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
    return cf.moduleListGen(list_callable_functions(), 'p1', 0, 2)

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

def p1f_18n_10_four_possible_values2(request):
    while True:
        try:
            num = randint(2,9)*randint(2,8)
            correct = [i for i in range(1,num+1) if num%i == 0]

            def addStuff(correct, num):
                incorrect = correct.copy()
                del incorrect[randint(0,len(correct)-1)]
                num = randint(1,num-1)
                while num in incorrect:
                    num = randint(1,num-1)
                incorrect.append(num)
                return sorted(incorrect)
            incorrect = [addStuff(correct, num),addStuff(correct, num),addStuff(correct, num)]
            break
        except:
            continue
    q = cf.Question(correct, incorrect)
    q.questionBase = f'''x is a positive integer.
    \n{num} \u00f7 x is a positive integer.
    \nWork out the {len(correct)} possible values of x.'''
    q.previousQ, q.nextQ = previousNext("p1", 0, 2, cf.currentFuncName(), module_path())
    q.marks = 2
    q.webLink = 'https://www.bbc.co.uk/bitesize/topics/z6j2tfr/articles/zv9sv9q' 
    q.workOn = 'Finding the factors of a number'
    return render(request, "gcsemaths/multiChoicePlusReveal.html", cf.allArguments2(q.returnAll()))

def p1f_18n_11a_probability_dice1(request):
    sides, one_of_the_sides = randrange(4,12,2), randint(1,3)
    numbers = []
    for i in range(1,one_of_the_sides+1):
        poss = randint(1,sides)
        while poss in numbers:
            poss = randint(1,sides)
        numbers.append(poss)

    if len(numbers) == 1:
        nums = f'is {numbers[0]}'
    elif len(numbers)==2:
        nums = f'are {numbers[0]} or {numbers[1]}.'
    else:
        nums = f'are {numbers[0]}, {numbers[1]} or {numbers[2]}.'
  
    def all_options(one_of_the_sides, sides):
        correct = one_of_the_sides / sides
        return f"{fractions.Fraction(one_of_the_sides, sides).numerator}\u2044{fractions.Fraction(one_of_the_sides, sides).denominator} (fraction), {round(correct,3)} (decimal), or {round(correct*100,3)}% (percentage)"

    correct = all_options(one_of_the_sides, sides)
    incorrect = [all_options(one_of_the_sides, sides-1), all_options(one_of_the_sides, sides+1), all_options(one_of_the_sides - randrange(-1,1,2), sides)]
    
    q = cf.Question(correct, incorrect)
    q.questionBase = f'''A fair dice has {sides} sides, numbered 1 to {sides}.
    After it is rolled, {sides - 1} of the numbers can be seen.
    What is the probability that one of these {sides - 1} numbers {nums}'''
    q.previousQ, q.nextQ = previousNext("p1", 0, 2, cf.currentFuncName(), module_path())
    q.marks = 1
    q.webLink = 'https://revisionmaths.com/gcse-maths-revision/statistics-handling-data/probability' 
    q.workOn = 'Probability'
    return render(request, "gcsemaths/multiChoicePlusReveal.html", cf.allArguments2(q.returnAll()))

def p1f_18n_11b_probability_dice2(request):
    sides = randrange(4,12,2)
    num = randint(1,sides)
    all_sides = [i for i in range(1,sides+1)]
    total = sum(all_sides)
    correct = total-num
    incorrect = [total, total - randint(1,sides)+1, sides - num + 1]
    q = cf.Question(correct, incorrect)
    q.questionBase = f'''A fair dice has {sides} sides, numbered 1 to {sides}.
    After it is rolled, {sides - 1} of the numbers can be seen.
    If the number {num} can't be seen, what is the greatest possible sum of the sides which can be seen?'''
    q.previousQ, q.nextQ = previousNext("p1", 0, 2, cf.currentFuncName(), module_path())
    q.marks = 2
    q.webLink = 'https://revisionmaths.com/gcse-maths-revision/statistics-handling-data/probability' 
    q.workOn = 'Knowledge of dice. Kidding. Probability'
    return render(request, "gcsemaths/multiChoicePlusReveal.html", cf.allArguments2(q.returnAll()))


def p1f_18n_21_number_cards3(request):
    cards = list(set([randint(9,25) for i in range(randint(4,6))]))
    combos = [c for i in range(len(cards)+1) for c in itertools.combinations(cards,i)]
    pairs = [i for i in combos if len(i) ==2]
    totals = [i[0] + i[1] for i in pairs]
    target = randint(28,41)
    greater = randint(0,1)
    valid_totals = [i for i in totals if i > target] if greater == 1 else [i for i in totals if i < target]
    greater_less = 'more' if greater == 1 else 'less'
    correct = f"{fractions.Fraction(len(valid_totals),len(totals)).numerator}\u2044{fractions.Fraction(len(valid_totals),len(totals)).denominator}"
    if valid_totals == totals: 
        correct = '1'
        incorrect_option = '0'
    elif valid_totals == 0:
        correct = '0'
        incorrect_option = '1'
    else:
        incorrect_option = str(randint(0,1))

    incorrect = [
        f"{fractions.Fraction(len(valid_totals) + 1,len(totals)).numerator}\u2044{fractions.Fraction(len(valid_totals) + 1,len(totals)).denominator}",
        f"{fractions.Fraction(len(valid_totals) -1 ,len(totals)).numerator}\u2044{fractions.Fraction(len(valid_totals) - 1,len(totals)).denominator}",
        incorrect_option,
    ]
    q = cf.Question(correct, incorrect)
    q.questionBase = f'''Here are {len(cards)} number cards: {cards}. Two of the {len(cards)} cards are picked at random. Work out the probability that the total of the two numbers is {greater_less} than {target}'''
    q.previousQ, q.nextQ = previousNext("p1", 0, 2, cf.currentFuncName(), module_path())
    q.marks = 3
    q.webLink = 'https://revisionmaths.com/gcse-maths-revision/statistics-handling-data/probability' 
    q.workOn = 'Probability'
    return render(request, "gcsemaths/multiChoicePlusReveal.html", cf.allArguments2(q.returnAll()))

#def p1f_18n_30_work_out_the_percentage3(request):
#    fro, to = randint(2,12)*10, randint(24,36)*10
