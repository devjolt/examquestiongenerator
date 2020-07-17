from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal
from . import algebra_logic
import sys

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[-1:]  #all modules not to be used for views kept at the front of the file are not added to the usable list. Usually 14
    return usableModuleList

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

def moduleListGen(qtype = None, low = 0, high = None): 
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
    return poop

def previousNext(qtype = None, low = 0, high = None, name=''):
    modList = moduleListGen(qtype, low, high)
    modDict = {}
    count = -1
    for thing in modList:
        count+=1
        modDict.update({str(thing):count})
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
    return f"/gcsemaths/algebra/{previous_q}", f"/gcsemaths/algebra/{next_q}"

#allArguments makes it less messy to return dictionary values to templates
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None, question4=None, answer4=None, marks4=None, pre=None, preans = None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            'question4':question4, 'answer4': answer4, 'marks4':marks4,
            'pre':pre, 'preans':preans
            }

#selects a random selection module (as below) at random from algebra_logic.py 
def select_random(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = algebra_logic.select_random()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

#selects a random module from one of the categories in title
def algebra_basics_random(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = algebra_logic.algebra_basics_random()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

def algebra_brackets_random(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = algebra_logic.algebra_brackets_random()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

def algebra_powers_random(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = algebra_logic.algebra_powers_random()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

def algebra_surds_random(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = algebra_logic.algebra_surds_random()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

def algebra_solve_random(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = algebra_logic.algebra_solve_random()
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

def posNeg(num):
    selection = randint(0,1)
    if selection == 0:
        num *=-1
    return num

def letterGen():
    letter = chr(randint(97, 122))
    return letter

def termGen(low = 97, high = 122, letterChance = 2):
    value, letters = 0,''
    #will term have a value?
    if randint(0,letterChance) == 0: value = 1
    else: value = randint(2,9)
    #will term have a letter?
    if value > 1:
        if randint(0,letterChance)>0: letters = ''
        elif randint(0,letterChance)==0: letters = chr(randint(low,high))
    else: letters = chr(randint(low,high))
    return [value, letters]

def termxTermy(op1,termx,op2,termy):
    print(f"{termx}, {termy}")
    x,y = termx[0], termy[0]
    if op1 == -1:
        x*=-1
        print("op1neg")
    if op2 == -1: 
        y*=-1
        print("op2neg")
    value = x * y
    print(f"{value}{termx[1]}{termy[1]}")
    return [value, f"{termx[1]}{termy[1]}"]

def randchar():
    if randint(0,2) == 0: return chr(randint(97, 122))
    else: return randint(1,12)

#powers and roots: mult = add, divide = sub, brackets = mult, anything to power of 1 = itself, anything to power of 0 = 1, 1 to any power =1, frac = apply power to top and bottom of frac
#leah is tiling  asection of her bathroom wall, the tiles are a cm wide and b cm tall. and she needs 20 tiles in total find an expression for the area of th ewal she is tiling in terms of 8 and b
#on the diagram below, shade the area represented by pq + 3pr
#peter is making a sculpture using different pieces of metal tubing. He makes a tower by stacking 7 pieces that are (f + g)cm tall, 9 pieces that are (h-g) cm tall and 5 that are 2h cm tall on top of each other find an expression for the height of the tower in terms of f,g and h
#s rectangle has sides that are 4x+3 cm and 5x-9 cm long find an expression in terms of x for the side of a regular hexagon with the same perimeter as the rectangle
#circle the correct value of 5**-2
#show that 8 to the pwer of 3/5 is 16
#negative powers upside down
#fractional powers are roots
#two stage fractional powers

#multiplying out brackets

def qbasics_negative_numbers():
    name = "qbasics_negative_numbers"
    number1 = posNeg(randint(2,9))
    number2 = posNeg(randint(2,9))
    ans = number1 * number2
    actualOperators = ["*","/"]
    printedOp = ["x", f"\u00F7"]
    choice = randint(0,1)
    if choice == 0: answer, questionBase = ans, f"{number1} {printedOp[choice]} {number2}"
    if choice == 1: answer, questionBase = number1, f"{ans} {printedOp[choice]} {number2}"
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qbasics_multiplyingLetters():
    letter1, letter2, letter3 = letterGen(), letterGen(), letterGen()
    starterLetters = [f"{letter1}", f"{letter2}",f"{letter3}"]

    letterList=[]
    for i in range(4):
        letterList.append(starterLetters[randint(0, len(starterLetters)-1)])
        
    firstString = "\u00D7".join(letterList)

    questionBase = f"Simplify this expression: {firstString}"

    letterListGather = letterList[:].sort()

    letter1Counter, letter2Counter, letter3Counter  = 0,0,0
      #counting the letters
    for i in range(len(letterList)):
        if letterList[i] == letter1: letter1Counter+=1
        elif letterList[i] == letter2: letter2Counter+=1
        elif letterList[i] == letter3: letter3Counter+=1

    counters = [letter1Counter, letter2Counter, letter3Counter]

    finalString = ''
    for i in range(len(counters)):
        if counters[i] == 0: continue
        elif counters[i] == 1: finalString += starterLetters[i]
        elif counters[i] == 2: finalString += f"{starterLetters[i]}2"
        elif counters[i] == 3: finalString += f"{starterLetters[i]}3"
        elif counters[i] == 4: finalString += f"{starterLetters[i]}4"

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    finalStringSup = f"{finalString}".translate(SUP)
    
    answer = finalStringSup
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qbasics_collecting_like_terms():
    letter1, letter2, number1, number2 = letterGen(), letterGen(), randint(1,9), randint(1,9)
    letterCombo = f"{letter1}{letter2}"

    starterTerms = [f"{letter1}", f"{letter2}",f"{letterCombo}", f"{number1}",f"{number2}"]

    termList=[]
    for i in range(8):
        termList.append(starterTerms[randint(0, len(starterTerms)-1)])
        
    firstString = " \u002B ".join(termList)

    letterListGather = termList[:]
    letterListGather.sort()

    letter1Counter,letter2Counter,letterComboCounter,numberCounter = 0,0,0,0
  
    for i in range(len(termList)):
        if termList[i] == letter1: letter1Counter+=1
        elif termList[i] == letter2: letter2Counter+=1
        elif termList[i] == letterCombo: letterComboCounter +=1
        elif termList[i] == str(number1): numberCounter += int(number1)
        elif termList[i] == str(number2): numberCounter += int(number2)

    counters = [letter1Counter, letter2Counter, letterComboCounter]

    finalString = ''
    for i in range(len(counters)):
        if counters[i] == 0: continue
        elif counters[i] == 1: finalString += f"{starterTerms[i]} \u002B "
        elif counters[i] == 2: finalString += f"2{starterTerms[i]} \u002B "
        elif counters[i] == 3: finalString += f"3{starterTerms[i]} \u002B "
        elif counters[i] == 4: finalString += f"4{starterTerms[i]} \u002B "
        elif counters[i] == 5: finalString += f"5{starterTerms[i]} \u002B "
        elif counters[i] == 4: finalString += f"6{starterTerms[i]} \u002B "

    questionBase = f"Simplify the following expression: {firstString}"
    answer = finalString + str(numberCounter)
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qexpand_brackets_three_letters():
    letter1, letter2, letter3 = letterGen(), letterGen(), letterGen()
    ops = ["-", "+"]
    op = ops[randint(0, len(ops)-1)]
    questionBase = f'''
    Expand the brackets:
    {letter1}({letter2} {op} {letter3})'''
    answer = f"{letter1}{letter2} {op} {letter1}{letter3}"
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qexpand_brackets_numbers_letters():
    term1, term2, term3 = termGen(), termGen(), termGen()
    ops = ["+"]
    op = ops[randint(0, len(ops)-1)]

    t12 = [term1[0] * term2[0], f"{term1[1]}{term2[1]}"]
    t13 = [term1[0] * term3[0], f"{term1[1]}{term3[1]}"]
    
    def finalTermGen(term):
        if term[0] == 1:
            if term[1] != '': return f"{term[1]}"
            else: return f"{term[0]}"
        elif term[0] == -1:
            if term[1] != '': return f"{term[1]}"
            else: return f"{term[0]}"
        else: return f"{term[0]}{term[1]}"

    def power(term):
        if len(term[1]) < 2: return term
        else:
            if term[1][-1] == term[1][-2]:
                term[1] = f"{term[1][0:1]}\u00B2"
            elif term[1][0] == term[1][1]:
                term[1] = f"{term[1][-1:]}\u00B2"
        return term

    questionBase = f'{(finalTermGen(power(term1)))}({(finalTermGen(power(term2)))} + {(finalTermGen(power(term3)))})'
    answer = f'{(finalTermGen(power(t12)))} + {(finalTermGen(power(t13)))}'
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_of_zero():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    questionBase = f"What is the value of {value}⁰?"
    answer = 1
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_of_one():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    questionBase = f"What is the value of {value}¹?"
    answer = value
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_one_to_the_power_of():
    value = 1
    power = randint(1,99)
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSup = f"{power}".translate(SUP)
    questionBase = f"What is the value of {value}{powerSup}?"
    answer = value
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_multiplying_powers():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    
    power1, power2, power3, = randint(1,9), randint(1,9), randint(1,9)
    total = power1 + power2 + power3

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    power1Sup, power2Sup, power3Sup, totalSup = f"{power1}".translate(SUP), f"{power2}".translate(SUP), f"{power3}".translate(SUP), f"{total}".translate(SUP) 
    
    questionBase = f"{value}{power1Sup}\u00D7 {value}{power2Sup}\u00D7 {value}{power3Sup}\u003D"
    answer = f"{value}{totalSup}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_dividing():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    
    power1, power2, power3, = randint(1,9), randint(1,9), randint(1,9)
    total = power1+ power2 + power3

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    power1Sup, power2Sup, power3Sup, totalSup = f"{power1}".translate(SUP), f"{power2}".translate(SUP), f"{power3}".translate(SUP), f"{total}".translate(SUP) 
    
    questionBase = f"{value}{totalSup}\u00F7 {value}{power2Sup}\u00F7 {value}{power3Sup}\u003D"
    answer = f"{value}{power1Sup}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_raising_to():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    
    power1, power2, power3, = randint(1,9), randint(1,9), randint(1,9)
    total = power1 * power2 

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    power1Sup, power2Sup, power3Sup, totalSup = f"{power1}".translate(SUP), f"{power2}".translate(SUP), f"{power3}".translate(SUP), f"{total}".translate(SUP) 
    
    questionBase = f"({value}{power1Sup}){power2Sup}\u003D"
    answer = f"{value}{totalSup}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_raising_two_powers_to():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    
    power1, power2, power3, = randint(1,9), randint(1,9), randint(1,9)
    total = (power1 + power2 ) * power3

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    power1Sup, power2Sup, power3Sup, totalSup = f"{power1}".translate(SUP), f"{power2}".translate(SUP), f"{power3}".translate(SUP), f"{total}".translate(SUP) 
    
    questionBase = f"({value}{power1Sup}\u00D7 {value}{power2Sup}){power3Sup}\u003D"
    answer = f"{value}{totalSup}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_with_fractions():
    number1, number2 = randint(1,9), randint (1,9)
    power = randint(1, 4)

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)

    questionBase = f"Evaluate: ({number1}\u2044{number2}){powerSUP}"    
    answer = f"{number1**power}\u2044{number2**power}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_with_fractions_letters():
    number1, number2 = letterGen(), letterGen()
    power = randint(1, 4)

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)

    questionBase = f"Evaluate: ({number1}\u2044{number2}){powerSUP}"
    answer = f"{number1}{powerSUP}\u2044{number2}{powerSUP}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_negative():
    number1 = randint(1,9)
    power = randint(1, 4)

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)


    questionBase = f"Evaluate: {number1}\u207b{powerSUP}"
    answer = f"1\u2044{number1**power}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_negative_letters():
    number1 = letterGen()
    power = randint(1, 9)

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)

    questionBase = f"Evaluate: {number1}\u207b{powerSUP}"
    answer = f"1\u2044{number1}{powerSUP}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qpower_fractional():
    power = randint(2, 3)
    ans = randint(1,10)
    number1 = ans**power

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)

    questionBase = f"Evaluate: {number1} \u00b9\u2e0d{powerSUP}"
    answer = f"{ans}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qexpand_double_brackets(): # requires termGen() and termxTermy()
    term1, term2, term3, term4 = termGen(), termGen(), termGen(), termGen()
    ops = [[1,"+"],[-1,"-"]]
    op1, op2 = ops[randint(0, 1)], ops[randint(0, 1)]

    def termxTermy(op1,termx,op2,termy):
        print(f"{termx}, {termy}")
        x,y = termx[0], termy[0]
        if op1 == -1:
            x*=-1
            print("op1neg")
        if op2 == -1: 
            y*=-1
            print("op2neg")
        value = x * y
        print(f"{value}{termx[1]}{termy[1]}")
        return [value, f"{termx[1]}{termy[1]}"]

    t13, t14, t23, t24 = termxTermy(None,term1,None,term3), termxTermy(None,term1,op2[0],term4), termxTermy(op1[0],term2,None,term3), termxTermy(op1[0],term2,op2[0],term4)
    firstTermList = [t13, t14, t23, t24]

    print(firstTermList)

    counter = 0
    valueLetters = []
    for i in range(len(firstTermList)):
        if firstTermList[i][1] =='': counter += firstTermList[i][0]
        else: valueLetters.append([firstTermList[i][1], firstTermList[i][0]])

    valueLetters.sort()
    print(valueLetters)
    collectedLetters = []
    while len(valueLetters) > 0:
        try:
            if valueLetters[0][0] == valueLetters[1][0]:
                collectedLetters.append([valueLetters[0][1] + valueLetters[1][1],valueLetters[0][0]])
                valueLetters = valueLetters[2:]
            else:
                collectedLetters.append([valueLetters[0][1],valueLetters[0][0]])
                valueLetters = valueLetters[1:]
        except IndexError:
            if len(valueLetters) == 1:
                collectedLetters.append([valueLetters[0][1],valueLetters[0][0]])
                valueLetters.clear()
                
    print(collectedLetters)

    finalList = []
    for letter in collectedLetters:
        finalList.append(letter)
    if counter != 0: finalList.append([counter,''])

    print(finalList)
           
    def finalTermGen(term):
        if term[0] == 1:
            if term[1] != '': return f"{term[1]}"
            else: return f"{term[0]}"
        elif term[0] == -1:
            if term[1] != '': return f"-{term[1]}"
            else: return f"{term[0]}"
        else: return f"{term[0]}{term[1]}"

    def power(term):
        if len(term[1]) < 2: return term
        else:
            if term[1][-1] == term[1][-2]:
                term[1] = f"{term[1][0:1]}\u00B2"
            elif term[1][0] == term[1][1]:
                term[1] = f"{term[1][-1:]}\u00B2"
        return term
    
    finalString = ' '
    for i in range(len(finalList)):
        if finalList[i][0] < 0:
            finalString = finalString[:-2]
            finalString += f"{finalTermGen(power(finalList[i]))} + "
        else: finalString += f"{finalTermGen(power(finalList[i]))} + "
    answer = finalString[:-2]

    questionString = f"({(finalTermGen(power(term1)))}"

    if term2[0] < 0:questionString+= f" {(finalTermGen(power(term2)))})({(finalTermGen(power(term3)))}"
    else: questionString+= f" {op1[1]} {(finalTermGen(power(term2)))})({(finalTermGen(power(term3)))}"
    if term4[0] < 0: questionString+= f" {finalTermGen(power(term4))})"
    else: questionString+= f" {op2[1]} {(finalTermGen(power(term4)))})"
    
    questionBase = questionString
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsurd_rule_17():
    char1, char2 = randchar(), randchar()
    questionBase = f"\u221A{char1} \u00d7 \u221A{char2}"

    if type (char1) == int:
        if type(char2) == int:
            answer = f"\u221A({char1 * char2})"
        elif type(char2) == str:
            answer = f"\u221A({char1}{char2})"
    elif type (char1) == str:
        if type (char2) == str:
            answer = f"\u221A({char1}{char2})"
        elif type(char2) == int:
            answer = f"\u221A({char2}{char1})"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsurd_rule_2b7():
    char1, char2 = randchar(), randchar()
    questionBase = "Simplify:"
    pre = f'''
    \u221A{char1}
    \u2500\u2500\u2500
    \u221A{char2}'''
    if type (char1) == int:
        if type(char2) == int:
            if char1%char2==0:
                if ((char1/char2)**0.5)%1==0:
                    answer = f"{int((char1/char2)**0.5)}"
                else: answer = f"\u221A{int(char1/char2)}"
            else:answer =  f"\u221A({char1}\u2044{char2})"
        elif type(char2) == str:
            answer = f"\u221A({char1}\u2044{char2})"
    elif type (char1) == str:
        if type (char2) == str:
            if ord(char1) == ord(char2): answer = 1
            else: answer = f"\u221A({char1}\u2044{char2})"
        elif type(char2) == int:
            answer = f"\u221A({char1}\u2044{char2})"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, pre, None

def qsurd_rule_2a7():
    char2 = randint(2,12)
    char1 = char2*randint(1,10)
    questionBase = "Simplify:"
    pre = f'''
    \u221A{char1}
    \u2500\u2500\u2500
    \u221A{char2}'''
    if type (char1) == int:
        if type(char2) == int:
            if char1%char2==0:
                if ((char1/char2)**0.5)%1==0:
                    answer = f"{int((char1/char2)**0.5)}"
                else: answer = f"\u221A{int(char1/char2)}"
            else:answer =  f"\u221A({char1}\u2044{char2})"
        elif type(char2) == str:
            answer = f"\u221A({char1}\u2044{char2})"
    elif type (char1) == str:
        if type (char2) == str:
            if ord(char1) == ord(char2): answer = 1
            else: answer = f"\u221A({char1}\u2044{char2})"
        elif type(char2) == int:
            answer = f"\u221A({char1}\u2044{char2})"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, pre, None

def qsurd_rule_3a7():
    char1, char2 = letterGen(), letterGen()
    questionBase = f"\u221A{char1} \u002b \u221A{char2}"
    if ord(char1)== ord(char2): answer = f"2\u221A{char2}"
    else: answer = questionBase
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_rule_3b7():
    value1, value2 = randint(1, 15), randint(1, 15)
    print(value1)
    print(value2)
    char1 =randint(1,100) if randint(0,1)==0 else value1**2
    char2 =randint(1,100) if randint(0,1)==0 else value2 **2
    questionBase = f"\u221A{char1} \u002b \u221A{char2}"
    add, char1done, char2done  = 0, False, False
    answer = f"\u221A{char1} \u002b \u221A{char2}"
    if (char1**0.5)%1 == 0: 
        char1 = (int(char1**0.5))
        add += 1
        char1done = True
    if (char2**0.5)%1 == 0: 
        char2 = (int(char2**0.5))
        add += 1
        char2done = True
    if add == 2: answer = f"{int(char1 + char2)}"
    if add == 0: 
        if char1 == char2: answer = f"2\u221A{char1}"
    if add == 1:
        if char1done == True: answer = f"{char1} \u002b \u221A{char2}"
        if char2done == True: answer = f"\u221A{char1} \u002b {char2}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_rule_3c7():
    if randint(0,1) == 1: char1, char2 = randint(1,100), letterGen()  
    else: char1, char2 = letterGen(), randint(1,100)
    questionBase = f"\u221A{char1} \u002b \u221A{char2}"
    answer = questionBase
    if type(char1) == int: 
        if (char1**0.5)%1 == 0: 
            char1 = (int(char1**0.5))
            answer = f"{char1} + \u221A{char2}"
    if type(char2) == int: 
        if (char2**0.5)%1 == 0: 
            char2 = (int(char2**0.5))
            answer = f"\u221A{char1} + {char2}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_rule_4a7():
    char1, char2 = letterGen(), letterGen()
    questionBase = f"({char1} + \u221A{char2})\u00b2"
    answer = f"{char1}\u00b2 + 2{char1}\u221a{char2} + {char2}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_rule_4b7():
    if randint(0,1) == 1: 
        char1, char2 = randint(1,100), letterGen()
        questionBase = f"({char1} \u002b \u221A{char2})\u00b2"
        answer = f"{char1**2} + {2*char1}\u221A{char2} + {char2}"
    else: 
        char1, char2 = letterGen(), randint(1,100)
        questionBase = f"({char1} \u002b \u221A{char2})\u00b2"
        answer = f"{char1}\u00b2 + 2{char1}\u221A{char2} + {char2}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_rule_5a7():
    char1, char2 = letterGen(), letterGen()
    questionBase = f"({char1} + \u221A{char2})({char1} - \u221A{char2})"
    answer = f"{char1}\u00b2 - {char2}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_rule_5b7():
    if randint(0,1) == 1: 
        char1, char2 = randint(1,15), letterGen()
        questionBase = f"({char1} + \u221A{char2})({char1} - \u221A{char2})"
        answer = f"{char1**2} - {char2}"
    else: 
        char1, char2 = letterGen(), randint(1,100)
        questionBase = f"({char1} + \u221A{char2})({char1} - \u221A{char2})"
        answer = f"{char1}\u00b2 - {char2}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsurd_rule_6a7():
    char1, char2 = letterGen(), letterGen()
    questionBase = f"simplify:"
    pre=f'''
     {char1}
    \u2500\u2500\u2500
    \u221A{char2}'''
    answer = f""
    preans = f'''
    {char1}\u221A{char2}
    \u2500\u2500\u2500
     {char2}'''
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, pre, preans

def qsurd_rule_6b7():
    if randint(0,1)==0:char1, char2 = letterGen(), randint(1,100)
    else: char1, char2 = randint(1,100), letterGen()
    questionBase = f"Simplify:"
    pre=f'''
    {char1}
    \u2500\u2500\u2500
    \u221A{char2}'''
    answer = f""
    preans = f'''
    {char1}\u221A{char2}
    \u2500\u2500\u2500
     {char2}'''
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None, pre, preans

def qsurd_simplify_addition_a8():
    surd, letter = randint(2, 9), letterGen()
    a1, a2, a3, a4 = randint(1,12),randint(1,12),randint(1,12),randint(1,12) 
    qu1, qu2, qu3, qu4 = (a1**2)*surd, (a2**2)*surd,(a3**2)*surd,(a4**2)*surd
    questionBase = f" Write \u221A{qu1} + \u221A{qu2} + \u221A{qu3} in the form {letter}\u221A{surd} where {letter} is an integer."
    answer = f"{a1+a2+a3}\u221A{surd}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 3, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_simplify_addition_b8():
    surd, letter = randint(2, 9), letterGen()
    a1, a2, a3, a4 = randint(1,12),randint(1,12),randint(1,12),randint(1,12) 
    qu1, qu2, qu3, qu4 = (a1**2)*surd, (a2**2)*surd,(a3**2)*surd,(a4**2)*surd
    questionBase = f" Write \u221A{qu1} + \u221A{qu2} - \u221A{qu3} in the form {letter}\u221A{surd} where {letter} is an integer."
    answer = f"{a1+a2-a3}\u221A{surd}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 3, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_simplify_addition_c8():
    surd, letter = randint(2, 9), letterGen()
    a1, a2, a3, a4 = randint(1,12),randint(1,12),randint(1,12),randint(1,12) 
    qu1, qu2, qu3, qu4 = (a1**2)*surd, (a2**2)*surd,(a3**2)*surd,(a4**2)*surd
    questionBase = f" Write \u221A{qu1} - \u221A{qu2} + \u221A{qu3} in the form {letter}\u221A{surd} where {letter} is an integer."
    answer = f"{a1-a2+a3}\u221A{surd}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 3, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_simplify_area8():
    surds = [2,3,5,6,7,10,11]
    surd = surds[randint(0, len(surds)-1)]    
    multiplier,known,letter = randint(2, 7), randint(2, 7), letterGen()
    squared = surd * multiplier**2
    area = squared * known
    questionBase = f"A rectangle with length {known}{letter} cm and width {letter} cm has an area of {area} cm\u00b2. Find the exact value of {letter} giving your answer in its simplest form."
    answer = f"{multiplier}\u221A{surd}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 3, None, None, None, None, None, None,None, None, None,None, None, None, None, None

def qsurd_in_the_form9():
    legit = [[1,2],[2,5],[3,10],[4,17]]
    choice = legit[randint(0, len(legit)-1)] 
    top = randint(1,8)
    bottomPlus = choice[0]
    surd = choice[1]
    questionBase = f"Write the following in the form a +b\u221A{surd}:"
    pre = f'''
      {top}
    \u2500\u2500\u2500\u2500\u2500
    {bottomPlus} + \u221A{surd}
    '''
    a = top*bottomPlus
    b = top
    answer = f"-{a} + {b}\u221A{surd}"
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 3, None, None, None, None, None, None,None, None, None,None, None, None, pre, None




'''unicode small slash = \u2e0d
unicode fraction slash = \u2044
multiplication: \u00D7
root: \u221A
power of 2: \u00b2
'''



def needswork_expanding_tripple_brackets():
    term1, term2, term3, term4, term5, term6 = termGen(), termGen(), termGen(), termGen(), termGen(),termGen()
    ops = [[1,"+"],[-1,"-"]]
    op1, op2, op3 = ops[randint(0, 1)], ops[randint(0, 1)], ops[randint(0, 1)]

    def termxTermy(op1,termx,op2,termy,op3 = None):
        print(f"{termx}, {termy}")
        x,y = termx[0], termy[0]
        if op1 == -1:
            print("op1neg")
            y*=-1
        if op2 == -1:
            print("op2neg")
            y*=-1
        if op3 == -1:
            y*=-1
            print("op3Neg")
        
        value = x * y
        print(f"{value}{termx[1]}{termy[1]}")
        return [value, f"{termx[1]}{termy[1]}"]
    
    t13, t14, t15, t16 = termxTermy(None,term1,None,term3), termxTermy(None,term1,op2[0],term4), termxTermy(None,term1,None,term5), termxTermy(None,term1,None,term6, op3[0])
    t23, t24, t25, t26 = termxTermy(op1[0],term2,None,term3), termxTermy(op1[0],term2,op2[0],term4), termxTermy(op1[0],term2,None,term5), termxTermy(op1[0],term2,None,term6, op3[0])
    t35, t36, t45, t46 = termxTermy(None,term3,None,term5), termxTermy(None,term3,None,term6,op3[0]), termxTermy(op2[0],term4,None,term5), termxTermy(op2[0],term4,None,term6, op3[0])

    firstTermList = [t13, t14, t15, t16, t23, t24, t25, t26, t35, t36, t45, t46]

    print(firstTermList)

    counter = 0
    valueLetters = []
    for i in range(len(firstTermList)):
        if firstTermList[i][1] =='': counter += firstTermList[i][0]
        else: valueLetters.append([firstTermList[i][1], firstTermList[i][0]])

    valueLetters.sort()
    print(valueLetters)
    collectedLetters = []
    while len(valueLetters) > 0:
        try:
            if valueLetters[0][0] == valueLetters[1][0]:
                collectedLetters.append([valueLetters[0][1] + valueLetters[1][1],valueLetters[0][0]])
                valueLetters = valueLetters[2:]
            else:
                collectedLetters.append([valueLetters[0][1],valueLetters[0][0]])
                valueLetters = valueLetters[1:]
        except IndexError:
            if len(valueLetters) == 1:
                collectedLetters.append([valueLetters[0][1],valueLetters[0][0]])
                valueLetters.clear()
                
    print(collectedLetters)

    finalList = []
    for letter in collectedLetters:
        finalList.append(letter)
    if counter != 0: finalList.append([counter,''])

    print(finalList)
           
    def finalTermGen(term):
        if term[0] == 1:
            if term[1] != '': return f"{term[1]}"
            else: return f"{term[0]}"
        elif term[0] == -1:
            if term[1] != '': return f"-{term[1]}"
            else: return f"{term[0]}"
        else: return f"{term[0]}{term[1]}"

    def power(term):
        if len(term[1]) < 2: return term
        else:
            if term[1][-1] == term[1][-2]:
                term[1] = f"{term[1][0:1]}\u00B2"
            elif term[1][0] == term[1][1]:
                term[1] = f"{term[1][-1:]}\u00B2"
        return term
    
    finalString = ' '
    for i in range(len(finalList)):
        if finalList[i][0] < 0:
            finalString = finalString[:-2]
            finalString += f"{finalTermGen(power(finalList[i]))} + "
        else: finalString += f"{finalTermGen(power(finalList[i]))} + "
    answer = finalString[:-2]

    questionString = f"({(finalTermGen(power(term1)))}"

    if term2[0] < 0:questionString+= f" {(finalTermGen(power(term2)))})({(finalTermGen(power(term3)))}"
    else: questionString+= f" {op1[1]} {(finalTermGen(power(term2)))})({(finalTermGen(power(term3)))}"
    if term4[0] < 0: questionString+= f" {finalTermGen(power(term4))})({finalTermGen(power(term5))}"
    else: questionString+= f" {op2[1]} {(finalTermGen(power(term4)))})({finalTermGen(power(term5))}"
    if term6[0] < 0: questionString+= f" {finalTermGen(power(term6))})"
    else: questionString+= f" {op3[1]} {(finalTermGen(power(term6)))})"

    questionBase = questionString
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 4, None, None, None, None, None, None,None, None, None,None, None, None,  None, None


def qfactorising_two_letters():
    term1, term2, term3 = termGen(97,98, 1), termGen(97,98, 1), termGen(97,98, 1)
    ops = ["+", "-"]
    op = ops[randint(0, len(ops)-1)]

    t12 = [term1[0] * term2[0], f"{term1[1]}{term2[1]}"]
    t13 = [term1[0] * term3[0], f"{term1[1]}{term3[1]}"]
    
    def finalTermGen(term):
        if term[0] == 1:
            if term[1] != '': return f"{term[1]}"
            else: return f"{term[0]}"
        elif term[0] == -1:
            if term[1] != '': return f"{term[1]}"
            else: return f"{term[0]}"
        else: return f"{term[0]}{term[1]}"

    def power(term):
        if len(term[1]) < 2: return term
        else:
            if term[1][-1] == term[1][-2]:
                term[1] = f"{term[1][0:1]}\u00B2"
            elif term[1][0] == term[1][1]:
                term[1] = f"{term[1][-1:]}\u00B2"
        return term

    answer = f'{(finalTermGen(power(term1)))}({(finalTermGen(power(term2)))} {op} {(finalTermGen(power(term3)))})'
    questionBase = f'Factorise: {(finalTermGen(power(t12)))} {op} {(finalTermGen(power(t13)))}'
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qfactorising_more_letters():
    term1, term2, term3 = termGen(97,110, 2), termGen(97,110, 1), termGen(97,110, 2)
    ops = ["+", "-"]
    op = ops[randint(0, len(ops)-1)]

    t12 = [term1[0] * term2[0], f"{term1[1]}{term2[1]}"]
    t13 = [term1[0] * term3[0], f"{term1[1]}{term3[1]}"]
    
    def finalTermGen(term):
        if term[0] == 1:
            if term[1] != '': return f"{term[1]}"
            else: return f"{term[0]}"
        elif term[0] == -1:
            if term[1] != '': return f"{term[1]}"
            else: return f"{term[0]}"
        else: return f"{term[0]}{term[1]}"

    def power(term):
        if len(term[1]) < 2: return term
        else:
            if term[1][-1] == term[1][-2]:
                term[1] = f"{term[1][0:1]}\u00B2"
            elif term[1][0] == term[1][1]:
                term[1] = f"{term[1][-1:]}\u00B2"
        return term

    answer = f'{(finalTermGen(power(term1)))}({(finalTermGen(power(term2)))} {op} {(finalTermGen(power(term3)))})'
    questionBase = f'Factorise: {(finalTermGen(power(t12)))} {op} {(finalTermGen(power(t13)))}'
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsolve_divide():
    x = randint(2,12)
    answer = (f"x = {x}")
    newx = randint(2, 5)
    newint = newx * x
    questionBase = (f"{newx}x = {newint}")
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsolve_collectint_divide():
    x = randint(2,12)
    answer = (f"x = {x}")
    newx = randint(2, 5)
    newint = newx * x
    questionBase = (f"{newx}x = {newint}")
    addmult, add = randint(2, 5), randint(1, 5)
    addnum = addmult * add
    newint += addnum
    questionBase = (f"{newx}x + {addnum} = {newint}")
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsolve_collectx_collectint_divide():
    x = randint(2,12)
    answer = (f"x = {x}")
    newx = randint(2, 5)
    newint = newx * x
    questionBase = (f"{newx}x = {newint}")
    addmult, add = randint(2, 5), randint(1, 5)
    addnum = addmult * add
    newint += addnum
    questionBase = (f"{newx}x + {addnum} = {newint}")
    add = randint(1,5)
    addx = addmult * add
    newx = newx + addx
    questionBase = (f"{newx}x + {addnum} = {newint} + {addx}x")
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsolve_collectx_collectint_divide_brackets():
    x = randint(2,6)
    answer = (f"x = {x}")
    print(answer)
    newx = randint(2, 5)
    newint = newx * x    
    addmult = randint(2, 5)
    add = randint(1, 5)
    addnum = addmult * add
    newint += addnum 
    add = randint(1,5)
    addx = addmult * add
    newx = newx + addx
    brackmult = randint(2,5)
    if randint(0,1) == 1:questionBase = (f"{newx * brackmult}x + {addnum * brackmult} = {brackmult}({newint} + {addx}x)")
    else: questionBase = (f"{brackmult}({newx}x + {addnum}) = {newint*brackmult} + {addx*brackmult}x")
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsolve_collectx_collectint_divide_brackets_double():
    x = randint(2,12)
    answer = (f"x = {x}")
    print(answer)
    newx = randint(2, 5)
    newint = newx * x
    addmult = randint(2, 5)
    add = randint(1, 5)
    addnum = addmult * add
    newint += addnum
    add = randint(1,5)
    addx = addmult * add
    newx = newx + addx
    brackmult = randint(2,5)
    questionBase = (f"{brackmult}({newx}x + {addnum}) = {brackmult}({newint} + {addx}x)")
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None, None, None, None,  None, None

def qsolve_negative_collectx_collectint_divide_brackets():
    multnum, addx = 0, 0
    while multnum+addx == 0:
        x = randint(-12,-1)
        answer = (f"x = {x}")    
        xmultnum = randint(2, 5)
        xmult = x * xmultnum   
        addnum = x * randint(2, 5)
        addint = x + addnum
        addxnum = randint(2,6)
        addx = x * xmultnum
        if randint(0,1) == 1: questionBase = f'''{addint} + {xmultnum - addx}x = {xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x)'''
        else: questionBase = f'''{xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x) = {addint} + {xmultnum - addx}x'''
    pre, nex = previousNext("q", 0, 1, currentFuncName())
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsolve_posneg_collectx_collectint_divide_brackets():
    x = 0
    while x == 0:
        x = randint(-12, 12)
    xmultnum, addx = 0, 0
    while xmultnum + addx == 0:
        answer = (f"x = {x}")    
        xmultnum = randint(2, 5)
        xmult = x * xmultnum   
        addnum = x * randint(2, 5)
        addint = x + addnum
        addxnum = randint(2,6)
        addx = x * xmultnum
    if x > 0:
        if randint(0,1) == 1: questionBase = f"{addint} + {xmultnum + addx}x = {xmultnum}({int((xmult + addint)/xmultnum)} + {int(addx/xmultnum)}x)"
        else: questionBase = f"{xmultnum}({int((xmult + addint)/xmultnum)} + {int(addx/xmultnum)}x) = {addint} + {xmultnum + addx}x"
    else:
        if randint(0,1) == 1: questionBase = f'''{addint} + {xmultnum - addx}x = {xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x)'''
        else: questionBase = f'''{xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x) = {addint} + {xmultnum - addx}x'''

    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None,  None, None

def qsolve_posneg_collectx_collectint_divide_brackets_fractions():
    x = 0
    while x == 0:
        x = randint(-12, 12)
    xmultnum, addx = 0, 0
    while xmultnum + addx == 0:
        answer = (f"x = {x}")    
        xmultnum = randint(2, 5)
        xmult = x * xmultnum   
        addnum = x * randint(2, 5)
        addint = x + addnum
        addxnum = randint(2,6)
        addx = x * xmultnum
    if x > 0:
        if randint(0,1) == 1: pre = f'''
        {addint} + {xmultnum + addx}x        {xmultnum}({int((xmult + addint)/xmultnum)} + {int(addx/xmultnum)}x)
         \u2500\u2500\u2500\u2500\u2500\u2500\u2500    =    \u2500\u2500\u2500\u2500\u2500\u2500\u2500
            {randint(2,5)}               {randint(2,5)}
        '''
        else: pre = f'''
        {xmultnum}({int((xmult + addint)/xmultnum)} + {int(addx/xmultnum)}x)      {addint} + {xmultnum + addx}x
         \u2500\u2500\u2500\u2500\u2500\u2500\u2500    =    \u2500\u2500\u2500\u2500\u2500\u2500\u2500
            {randint(2,5)}               {randint(2,5)}
        '''
    else:
        if randint(0,1) == 1: pre = f'''
        {addint} + {xmultnum - addx}x        {xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x)
         \u2500\u2500\u2500\u2500\u2500\u2500\u2500    =    \u2500\u2500\u2500\u2500\u2500\u2500\u2500
            {randint(2,5)}               {randint(2,5)}
        '''
        else: pre = f'''
        {xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x)        {addint} + {xmultnum - addx}x
         \u2500\u2500\u2500\u2500\u2500\u2500\u2500    =    \u2500\u2500\u2500\u2500\u2500\u2500\u2500
            {randint(2,5)}               {randint(2,5)}

        '''
    questionBase = "Solve to find x"
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None, pre, None

def qsolve_posneg_collectx_collectint_divide_brackets_first_fraction():
    x = 0
    while x == 0:
        x = randint(-12, 12)
    xmultnum, addx = 0, 0
    while xmultnum + addx == 0:
        answer = (f"x = {x}")    
        xmultnum = randint(2, 5)
        xmult = x * xmultnum   
        addnum = x * randint(2, 5)
        addint = x + addnum
        addxnum = randint(2,6)
        addx = x * xmultnum
    if x > 0:
        if randint(0,1) == 1: pre = f'''
        {addint} + {xmultnum + addx}x        
         \u2500\u2500\u2500\u2500\u2500\u2500\u2500    =    {xmultnum}({int((xmult + addint)/xmultnum)} + {int(addx/xmultnum)}x)
            {randint(2,5)}               
        '''
        else: pre = f'''
        {xmultnum}({int((xmult + addint)/xmultnum)} + {int(addx/xmultnum)}x)      
         \u2500\u2500\u2500\u2500\u2500\u2500\u2500    =    {addint} + {xmultnum + addx}x
            {randint(2,5)}               
        '''
    else:
        if randint(0,1) == 1: pre = f'''
        {addint} + {xmultnum - addx}x        
         \u2500\u2500\u2500\u2500\u2500\u2500\u2500    =    {xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x)
            {randint(2,5)}               
        '''
        else: pre = f'''
        {xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x)        
         \u2500\u2500\u2500\u2500\u2500\u2500\u2500    =    {addint} + {xmultnum - addx}x
            {randint(2,5)}              

        '''
    questionBase = "Solve to find x"
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None, pre, None

def qsolve_posneg_collectx_collectint_divide_brackets_second_fraction():
    x = 0
    while x == 0:
        x = randint(-12, 12)
    xmultnum, addx = 0, 0
    while xmultnum + addx == 0:
        while xmultnum - addx ==0:
            answer = (f"x = {x}")    
            xmultnum = randint(2, 5)
            xmult = x * xmultnum   
            addnum = x * randint(2, 5)
            addint = x + addnum
            addxnum = randint(2,6)
            addx = x * xmultnum   
    if x > 0:
        if randint(0,1) == 1: pre = f'''
                        {xmultnum}({int((xmult + addint)/xmultnum)} + {int(addx/xmultnum)}x)
        {addint} + {xmultnum + addx}x    =    \u2500\u2500\u2500\u2500\u2500\u2500\u2500
                            {randint(2,5)}
        '''
        else: pre = f'''
                            {addint} + {xmultnum + addx}x
         {xmultnum}({int((xmult + addint)/xmultnum)} + {int(addx/xmultnum)}x)    =    \u2500\u2500\u2500\u2500\u2500\u2500\u2500
                              {randint(2,5)}
        '''
    else:
        if randint(0,1) == 1: pre = f'''
                          {xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x)
        {addint} + {xmultnum - addx}x    =    \u2500\u2500\u2500\u2500\u2500\u2500\u2500
                              {randint(2,5)}
        '''
        else: pre = f'''
                        {addint} + {xmultnum - addx}x
        {xmultnum}({int((xmult - addint)/xmultnum)} {int(addx/xmultnum)}x)    =    \u2500\u2500\u2500\u2500\u2500\u2500\u2500
                            {randint(2,5)}
        '''
    questionBase = "Solve to find x"
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None, pre, None
    