from django.shortcuts import render
from random import randint, randrange
from fractions import Fraction
from decimal import Decimal
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
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def module_path():
    return '/gcsemaths/a_number/'

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

def aaa_ordering_numbers11():
    q = cf.Question(cf.currentFuncName())
    num1, num2, greaterSmaller = orderingSetup()
    q.questionBase = f"Which number is {greaterSmaller}: {num1} or {num2}?"
    if greaterSmaller == "greater":
        q.answerBase = num1 if num1>num2 else num2
    else:
        q.answerBase = num1 if num1<num2 else num2
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aab_in_order_of_size23():
    q = cf.Question(cf.currentFuncName())
    num1, num2, stringSeed = randint(1,4), randint(5,9), "0."
    numbers = [str(num1), str(num2), "0"]
    numberList = ['0.']
    for i in range(4):
        finalNumber = '0.'
        while finalNumber in numberList:
            digits = randint(0,1)
            for d in range(digits+1):
                selection = randint(0,2)
                finalNumber += numbers[selection] 
            for p in range(len(numberList)):
                if float(numberList[p]) == float(finalNumber):
                    finalNumber = "0."                  
        numberList.append(finalNumber)
    finalList = numberList[1:]
    selection, choice = randint(0,1), ["smallest", "largest"]
    if choice[selection] == "smallest": sortedFinalList = sorted(finalList)
    else: sortedFinalList =  sorted(finalList, reverse=True)
    finalListString = ''
    for n in finalList: finalListString += f"{n}, "
    finalListString = finalListString[:-2]
    
    sortedFinalListString = ''
    for ns in sortedFinalList: sortedFinalListString += f"{ns}, "
    sortedFinalListString = sortedFinalListString[:-2]
    
    q.questionBase = (f"Write the numbers above in order, starting with the {choice[selection]}: {finalListString}")
    q.answerBase = sortedFinalListString
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aac_ordering_decimals11():
    num1, num2, greaterSmaller = orderingSetup()
    num1, num2 = num1/10, num2/10
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"Which number is {greaterSmaller}: {num1} or {num2}?"
    if greaterSmaller == "greater":
        q.answerBase = num1 if num1>num2 else num2
    else:
        q.answerBase = num1 if num1<num2 else num2
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aad_ordering_fractions12():
    greaterSmaller = "greater" if randint(0,1) == 1 else "smaller"
    num1,num2 = fractionSetup(), fractionSetup()
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"Which is {greaterSmaller}: {num1} or {num2}?"
    if greaterSmaller == "greater":
        q.answerBase = num1 if num1>num2 else num2
    elif greaterSmaller == "smaller":
        q.answerBase = num1 if num1<num2 else num2
    else:
        q.answerBase = "Acutally, they're the same!"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aae_ordering_fractions_and_decimals13():
    greaterSmaller = "greater" if randint(0,1) == 1 else "smaller"
    num1,num2 = fractionSetup(), decimalSetup()
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"Which is {greaterSmaller}: {num1} or {num2}?"
    if greaterSmaller == "greater":
        q.answerBase = num1 if num1>num2 else num2
    elif greaterSmaller == "smaller":
        q.answerBase = num1 if num1<num2 else num2
    else:
        q.answerBase = "Acutally, they're the same!"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aaf_comparative_operators_with_integers13():
    op = ['<', '<=', '>', '>=']
    operator = op[randint(0,len(op)-1)]
    statement = f"{randint(1,20)}{operator}{randint(1,20)}"
    q = cf.Question(cf.currentFuncName())
    q.answerBase = eval(statement)
    q.questionBase = f"Is the following statement true or false: {statement}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aag_comparative_operators_with_fractions13():
    num1,num2 = fractionSetup(), fractionSetup()
    op = ['<', '<=', '>', '>=']
    operator = op[randint(0,len(op)-1)]
    statement = f"{num1}{operator}{num2}"
    q = cf.Question(cf.currentFuncName())
    q.answerBase = eval(statement)
    q.questionBase = f"Is the following statement true or false: {statement}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def aah_comparative_operators_with_fractions_and_decimals13():
    num1,num2 = fractionSetup(), decimalSetup()
    op = ['<', '<=', '>', '>=']
    operator = op[randint(0,len(op)-1)]
    statement = f"{num1}{operator}{num2}"
    q = cf.Question(cf.currentFuncName())
    q.answerBase = eval(statement)
    q.questionBase = f"Is the following statement true or false: {statement}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aai_xth_odd_number13():
    oddNumbers = [i for i in range(1,20,2)]
    xth = randint(1, len(oddNumbers))
    suffixList = ["st", "nd", "rd"]
    suffix = "th" if xth > 3 else suffixList[xth-1]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"Counting up from zero, what is the {xth}{suffix} odd number?"
    q.answerBase = f"{oddNumbers[xth-1]}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def aaj_xth_even_number13():
    evenNumbers = [i for i in range(2,20,2)]
    xth = randint(1, len(evenNumbers))
    suffixList = ["st", "nd", "rd"]
    suffix = "th" if xth > 3 else suffixList[xth-1]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"Counting up from two, what is the {xth}{suffix} even number?"
    q.answerBase = f"{evenNumbers[xth-1]}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def aak_xth_prime_number13():
    primeNumbers = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51,53]
    xth = randint(1, len(primeNumbers))
    suffixList = ["st", "nd", "rd"]
    suffix = "th" if xth > 3 else suffixList[xth-1]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"Counting up from 1, what is the {xth}{suffix} prime number?"
    q.answerBase = f"{primeNumbers[xth-1]}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aal_all_factors_of_x24():
    number = randint(1,100)
    factorList = ''
    for i in range(number):
        if number % (i+1) == 0: factorList += f"{str(i+1)},"
    factorList = factorList[:-1]
    q = cf.Question(cf.currentFuncName())
    q.questionBase = f"Write down all the factors of {number}"
    q.answerBase = f"{factorList}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
