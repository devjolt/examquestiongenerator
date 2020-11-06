from django.shortcuts import render
from random import randint, randrange
from fractions import Fraction
from decimal import Decimal
import sys
from gcsemaths import gcsemaths_classes_functions as cf
#from gcsemaths import variety_lists as vl

def list_callable_functions():
    """returns list of all modules in this file
    This function MUST remain in this file to work correctly!
    Used by:
    modulesList
    previousNext
    """
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    return entireModuleList

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_callable_functions(), 'b', 0, 1)

def module_path():
    return '/gcsemaths/b_algebra/'

def posNeg(num):
    selection = randint(0,1)
    if selection == 0:
        num *=-1
    return num

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
    return (value, letters)

def randchar():
    if randint(0,2) == 0: return chr(randint(97, 122))
    else: return randint(1,12)

def letterGen():
    letter = chr(randint(97, 122))
    return letter

def select_random():
    modList = moduleListGen("algebra",0, 7)
    selection = randint(0,len(modList)-1)
    passed = eval(f"{modList[selection]}()")
    return passed

def algebra_basics_random():
    modList = moduleListGen("ba", 0, 2)
    selection = randint(0,len(modList)-1)
    passed = eval(f"{modList[selection]}()")
    return passed

def algebra_brackets_random():
    modList = moduleListGen("bb", 0, 2)
    selection = randint(0,len(modList)-1)
    passed = eval(f"{modList[selection]}()")
    return passed

def algebra_powers_random():
    modList = moduleListGen("bc", 0, 2)
    selection = randint(0,len(modList)-1)
    passed = eval(f"{modList[selection]}()")
    return passed

def algebra_surds_random():
    modList = moduleListGen("bd", 0, 2)
    selection = randint(0,len(modList)-1)
    passed = eval(f"{modList[selection]}()")
    return passed

def algebra_factorising_random():
    modList = moduleListGen("be", 0, 2)
    selection = randint(0,len(modList)-1)
    passed = eval(f"{modList[selection]}()")
    return passed

def algebra_solve_random():
    modList = moduleListGen("bf", 0, 2)
    selection = randint(0,len(modList)-1)
    passed = eval(f"{modList[selection]}()")
    return passed



def ba_basics_negative_numbers12():
    q = Question(cf.currentFuncName())
    number1 = posNeg(randint(2,9))
    number2 = posNeg(randint(2,9))
    ans = number1 * number2
    actualOperators = ["*","/"]
    printedOp = ["x", f"\u00F7"]
    choice = randint(0,1)
    if choice == 0: q.answerBase, q.questionBase = ans, f"{number1} {printedOp[choice]} {number2}"
    if choice == 1: q.answerBase, q.questionBase = number1, f"{ans} {printedOp[choice]} {number2}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"basics", 0, 6, cf.currentFuncName(), module_path())
    return q.returnAll()

def ba_basics_multiplying_letters12():
    letter1, letter2, letter3 = letterGen(), letterGen(), letterGen()
    starterLetters = [f"{letter1}", f"{letter2}",f"{letter3}"]
    letterList=[]
    for i in range(4):
        letterList.append(starterLetters[randint(0, len(starterLetters)-1)])
    firstString = "\u00D7".join(letterList)
    q = Question(cf.currentFuncName())
    q.questionBase = f"Simplify this expression: {firstString}"
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
    q.answerBase = finalStringSup
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"basics", 0, 6, cf.currentFuncName(), module_path())
    return q.returnAll()

def ba_basics_collecting_like_terms13():
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
    q = Question(cf.currentFuncName())
    q.questionBase = f"Simplify the following expression: {firstString}"
    q.answerBase = finalString + str(numberCounter)
    previousQ, nextQ = previousNext("basics", 0, 6, currentFuncName())
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"basics", 0, 6, cf.currentFuncName(), module_path())
    return q.returnAll()

def bb_expand_brackets_three_letters13():
    letter1, letter2, letter3 = letterGen(), letterGen(), letterGen()
    ops = ["-", "+"]
    op = ops[randint(0, len(ops)-1)]
    q.questionBase = f'''
    Expand the brackets:
    {letter1}({letter2} {op} {letter3})'''
    q = Question(cf.currentFuncName())
    q.answerBase = f"{letter1}{letter2} {op} {letter1}{letter3}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"expand", 0, 6, cf.currentFuncName(), module_path())
    return q.returnAll()

def bb_expand_brackets_numbers_letters13():
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
    q = Question(cf.currentFuncName())
    q.questionBase = f'{(finalTermGen(power(term1)))}({(finalTermGen(power(term2)))} + {(finalTermGen(power(term3)))})'
    q.answerBase = f'{(finalTermGen(power(t12)))} + {(finalTermGen(power(t13)))}'
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"expand", 0, 6, cf.currentFuncName(), module_path())
    return q.returnAll()

def bb_expand_brackets_double24():
    q = Question(cf.currentFuncName())
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
    q.answerBase = finalString[:-2]

    questionString = f"({(finalTermGen(power(term1)))}"

    if term2[0] < 0:questionString+= f" {(finalTermGen(power(term2)))})({(finalTermGen(power(term3)))}"
    else: questionString+= f" {op1[1]} {(finalTermGen(power(term2)))})({(finalTermGen(power(term3)))}"
    if term4[0] < 0: questionString+= f" {finalTermGen(power(term4))})"
    else: questionString+= f" {op2[1]} {(finalTermGen(power(term4)))})"
    q.questionBase = questionString
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"expand", 0, 6, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_of_zero15():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    questionBase = f"What is the value of {value}⁰?"
    answer = 1
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_of_one15():
    letterNumber = randint(0,1)
    value = letterGen() if letterNumber == 0 else randint(1, 99)
    q = Question(cf.currentFuncName())
    q.questionBase = f"What is the value of {value}¹?"
    q.answerBase = value
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_one_to_the_power_of15():
    value = 1
    power = randint(1,99)
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSup = f"{power}".translate(SUP)
    q = Question(cf.currentFuncName())
    q.questionBase = f"What is the value of {value}{powerSup}?"
    q.answerBase = value
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_multiplying_powers15():
    value = letterGen() if randint(0,1) == 0 else randint(1, 99)
    
    power1, power2, power3, = randint(1,9), randint(1,9), randint(1,9)
    total = power1 + power2 + power3

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    power1Sup, power2Sup, power3Sup, totalSup = f"{power1}".translate(SUP), f"{power2}".translate(SUP), f"{power3}".translate(SUP), f"{total}".translate(SUP) 
    q = Question(cf.currentFuncName())
    q.questionBase = f"{value}{power1Sup}\u00D7 {value}{power2Sup}\u00D7 {value}{power3Sup}\u003D"
    q.answerBase = f"{value}{totalSup}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()


def bc_power_dividing15():
    value = letterGen() if randint(0,1) == 0 else randint(1, 99)
    
    power1, power2, power3, = randint(1,9), randint(1,9), randint(1,9)
    total = power1+ power2 + power3

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    power1Sup, power2Sup, power3Sup, totalSup = f"{power1}".translate(SUP), f"{power2}".translate(SUP), f"{power3}".translate(SUP), f"{total}".translate(SUP) 
    
    q = Question(cf.currentFuncName())
    q.questionBase = f"{value}{totalSup}\u00F7 {value}{power2Sup}\u00F7 {value}{power3Sup}\u003D"
    q.answerBase = f"{value}{power1Sup}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_raising_to15():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    
    power1, power2, power3, = randint(1,9), randint(1,9), randint(1,9)
    total = power1 * power2 

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    power1Sup, power2Sup, power3Sup, totalSup = f"{power1}".translate(SUP), f"{power2}".translate(SUP), f"{power3}".translate(SUP), f"{total}".translate(SUP) 
    q = Question(cf.currentFuncName())
    q.questionBase = f"({value}{power1Sup}){power2Sup}\u003D"
    q.answerBase = f"{value}{totalSup}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_raising_two_powers_to15():
    letterNumber = randint(0,1)
    if letterNumber == 0: value = letterGen()
    else: value = randint(1, 99)
    
    power1, power2, power3, = randint(1,9), randint(1,9), randint(1,9)
    total = (power1 + power2 ) * power3

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    power1Sup, power2Sup, power3Sup, totalSup = f"{power1}".translate(SUP), f"{power2}".translate(SUP), f"{power3}".translate(SUP), f"{total}".translate(SUP) 
    
    questionBase = f"({value}{power1Sup}\u00D7 {value}{power2Sup}){power3Sup}\u003D"
    answer = f"{value}{totalSup}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_with_fractions15():
    number1, number2 = randint(1,9), randint (1,9)
    power = randint(1, 4)

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)
    q = Question(cf.currentFuncName())
    q.questionBase = f"Evaluate: ({number1}\u2044{number2}){powerSUP}"    
    q.answerBase = f"{number1**power}\u2044{number2**power}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()


def bc_power_with_fractions_letters13():
    number1, number2 = letterGen(), letterGen()
    power = randint(1, 4)

    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)
    q = Question(cf.currentFuncName())
    q.questionBase = f"Evaluate: ({number1}\u2044{number2}){powerSUP}"
    q.answerBase = f"{number1}{powerSUP}\u2044{number2}{powerSUP}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_negative17():
    number1 = randint(1,9)
    power = randint(1, 4)
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)
    q = Question(cf.currentFuncName())
    q.questionBase = f"Evaluate: {number1}\u207b{powerSUP}"
    q.answerBase = f"1\u2044{number1**power}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_negative_letters17():
    number1 = letterGen()
    power = randint(1, 9)
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)
    q = Question(cf.currentFuncName())
    q.questionBase = f"Evaluate: {number1}\u207b{powerSUP}"
    q.answerBase = f"1\u2044{number1}{powerSUP}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bc_power_fractional17():
    power = randint(2, 3)
    ans = randint(1,10)
    number1 = ans**power
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    powerSUP = f"{power}".translate(SUP)
    q = Question(cf.currentFuncName())
    q.questionBase = f"Evaluate: {number1} \u00b9\u2e0d{powerSUP}"
    q.answerBase = f"{ans}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"power", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bd_surd_rule1_17():
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def bd_surd_rule2_17():
    char1, char2 = letterGen(), letterGen()
    questionBase = f"\u221A{char1} \u002b \u221A{char2}"
    if ord(char1)== ord(char2): answer = f"2\u221A{char2}"
    else: answer = questionBase
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def bd_surd_rule3_17():
    value1, value2 = randint(1, 15), randint(1, 15)
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()

def bd_surd_rule4_17():
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def bd_surd_rule5a_17():
    char1, char2 = letterGen(), letterGen()
    questionBase = f"({char1} + \u221A{char2})\u00b2"
    answer = f"{char1}\u00b2 + 2{char1}\u221a{char2} + {char2}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def bd_surd_rule5b_17():
    if randint(0,1) == 1: 
        char1, char2 = randint(1,100), letterGen()
        questionBase = f"({char1} \u002b \u221A{char2})\u00b2"
        answer = f"{char1**2} + {2*char1}\u221A{char2} + {char2}"
    else: 
        char1, char2 = letterGen(), randint(1,100)
        questionBase = f"({char1} \u002b \u221A{char2})\u00b2"
        answer = f"{char1}\u00b2 + 2{char1}\u221A{char2} + {char2}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def bd_surd_rule6a_17():
    char1, char2 = letterGen(), letterGen()
    questionBase = f"({char1} + \u221A{char2})({char1} - \u221A{char2})"
    answer = f"{char1}\u00b2 - {char2}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def surd_rule6b_17():
    if randint(0,1) == 1: 
        char1, char2 = randint(1,15), letterGen()
        questionBase = f"({char1} + \u221A{char2})({char1} - \u221A{char2})"
        answer = f"{char1**2} - {char2}"
    else: 
        char1, char2 = letterGen(), randint(1,100)
        questionBase = f"({char1} + \u221A{char2})({char1} - \u221A{char2})"
        answer = f"{char1}\u00b2 - {char2}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()

def bd_surd_rule7a_17():
    char1, char2 = letterGen(), letterGen()
    questionBase = f"simplify:"
    pre=f'''
     {char1}
    \u2500\u2500\u2500
    \u221A{char2}'''
    preans = f'''
    {char1}\u221A{char2}
    \u2500\u2500\u2500
     {char2}'''
    q = Question(cf.currentFuncName())
    q.questionCodeBase = pre if pre else None
    q.answerCodeBase = preans if preans else None
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def bd_surd_rule7b_17():
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
    q = Question(cf.currentFuncName())
    q.questionCodeBase = pre if pre else None
    q.answerCodeBase = preans if preans else None
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def bd_surd_simplify_additiona_38():
    surd, letter = randint(2, 9), letterGen()
    a1, a2, a3, a4 = randint(1,12),randint(1,12),randint(1,12),randint(1,12) 
    qu1, qu2, qu3, qu4 = (a1**2)*surd, (a2**2)*surd,(a3**2)*surd,(a4**2)*surd
    questionBase = f" Write \u221A{qu1} + \u221A{qu2} + \u221A{qu3} in the form {letter}\u221A{surd} where {letter} is an integer."
    answer = f"{a1+a2+a3}\u221A{surd}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()


def bd_surd_simplify_additionb_38():
    surd, letter = randint(2, 9), letterGen()
    a1, a2, a3, a4 = randint(1,12),randint(1,12),randint(1,12),randint(1,12) 
    qu1, qu2, qu3, qu4 = (a1**2)*surd, (a2**2)*surd,(a3**2)*surd,(a4**2)*surd
    questionBase = f" Write \u221A{qu1} + \u221A{qu2} - \u221A{qu3} in the form {letter}\u221A{surd} where {letter} is an integer."
    answer = f"{a1+a2-a3}\u221A{surd}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()

def bd_surd_simplify_additionc_38():
    surd, letter = randint(2, 9), letterGen()
    a1, a2, a3, a4 = randint(1,12),randint(1,12),randint(1,12),randint(1,12) 
    qu1, qu2, qu3, qu4 = (a1**2)*surd, (a2**2)*surd,(a3**2)*surd,(a4**2)*surd
    questionBase = f" Write \u221A{qu1} - \u221A{qu2} + \u221A{qu3} in the form {letter}\u221A{surd} where {letter} is an integer."
    answer = f"{a1-a2+a3}\u221A{surd}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()

def bd_surd_simplify_area_38():
    surds = [2,3,5,6,7,10,11]
    surd = surds[randint(0, len(surds)-1)]    
    multiplier,known,letter = randint(2, 7), randint(2, 7), letterGen()
    squared = surd * multiplier**2
    area = squared * known
    questionBase = f"A rectangle with length {known}{letter} cm and width {letter} cm has an area of {area} cm\u00b2. Find the exact value of {letter} giving your answer in its simplest form."
    answer = f"{multiplier}\u221A{surd}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()

def bd_surd_in_the_form_39():
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
    q = Question(cf.currentFuncName())
    q.questionCodeBase = pre if pre else None
    q.answerCodeBase = preans if preans else None
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"surd", 0, 4, cf.currentFuncName(), module_path())
    return q.returnAll()

def be_factorising_two_letters25():
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"factorising", 0, 11, cf.currentFuncName(), module_path())
    return q.returnAll()

def be_factorising_more_letters25():
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
    q = Question(cf.currentFuncName())
    questionBase = f'Factorise: {(finalTermGen(power(t12)))} {op} {(finalTermGen(power(t13)))}'
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"factorising", 0, 11, cf.currentFuncName(), module_path())
    return q.returnAll()


def bf_solve_divide25():
    x = randint(2,12)
    answer = (f"x = {x}")
    newx = randint(2, 5)
    newint = newx * x
    questionBase = (f"{newx}x = {newint}")
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()


def bf_solve_collectint_divide25():
    x = randint(2,12)
    answer = (f"x = {x}")
    newx = randint(2, 5)
    newint = newx * x
    questionBase = (f"{newx}x = {newint}")
    addmult, add = randint(2, 5), randint(1, 5)
    addnum = addmult * add
    newint += addnum
    questionBase = (f"{newx}x + {addnum} = {newint}")
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()


def bf_solve_collectx_collectint_divide25():
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()


def bf_solve_collectx_collectint_divide_brackets25():
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()


def bf_solve_collectx_collectint_divide_brackets_double35():
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()


def bf_solve_negative_collectx_collectint_divide_brackets35():
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bf_solve_posneg_collectx_collectint_divide_brackets35():
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
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bf_solve_posneg_collectx_collectint_divide_brackets_fractions35():
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
    q = Question(cf.currentFuncName())
    q.questionCodeBase = pre if pre else None
    q.answerCodeBase = preans if preans else None
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bf_solve_posneg_collectx_collectint_divide_brackets_first_fraction33():
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
    q = Question(cf.currentFuncName())
    q.questionCodeBase = pre if pre else None
    q.answerCodeBase = preans if preans else None
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()

def bf_solve_posneg_collectx_collectint_divide_brackets_second_fraction35():
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
    q = Question(cf.currentFuncName())
    q.questionCodeBase = pre if pre else None
    q.answerCodeBase = preans if preans else None
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"solve", 0, 5, cf.currentFuncName(), module_path())
    return q.returnAll()