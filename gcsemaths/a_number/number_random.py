from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[4:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
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

#allArguments makes it less messy to return dictionary values to templates
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None, question4=None, answer4=None, marks4=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            'question4':question4, 'answer4': answer4, 'marks4':marks4
            }

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    modList = moduleList()
    selection = randint(0,len(modList)-1)
    print(selection)
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4  = eval(f"{modList[selection]}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4 ))

#rounding to significant figures
#order positive and negative values

def in_order_of_size():
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
    
    questionBase = (f"Write the numbers above in order, starting with the {choice[selection]}: {finalListString}")
    answer = (sortedFinalListString)

    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None

def decimal_as_fraction():
    denOptions = [2,4,5,6,8,10,12,15,20]
    den = denOptions[randint(0,len(denOptions)-1)]
    num = randint(1,den-1)
    decimal = round(num/den, 5)
    questionBase = (f"Write {decimal} as a fraction")
    answer = (Fraction(f"{num}/{den}"))
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None

def fraction_as_decimal():
    denOptions = [2,4,5,6,8,10,12,15,20]
    den = denOptions[randint(0,len(denOptions)-1)]
    num = randint(1,den-1)
    decimal = round(num/den, 5)
    frac = Fraction(f"{num}/{den}")
    questionBase = (f"Write {frac} as a decimal")
    answer = f"{decimal}"
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None

def xth_odd_number():
    oddNumbers = [i for i in range(1,20,2)]
    xth = randint(1, len(oddNumbers))
    suffixList = ["st", "nd", "rd"]
    suffix = "th" if xth > 3 else suffixList[xth-1]
    questionBase = f"Counting up from zero, what is the {xth}{suffix} odd number?"
    answer = f"{oddNumbers[xth-1]}"
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None

def xth_even_number():
    evenNumbers = [i for i in range(2,20,2)]
    xth = randint(1, len(evenNumbers))
    suffixList = ["st", "nd", "rd"]
    suffix = "th" if xth > 3 else suffixList[xth-1]
    questionBase = f"Counting up from two, what is the {xth}{suffix} even number?"
    answer = f"{evenNumbers[xth-1]}"
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None

def xth_prime_number():
    primeNumbers = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51,53]
    xth = randint(1, len(primeNumbers))
    suffixList = ["st", "nd", "rd"]
    suffix = "th" if xth > 3 else suffixList[xth-1]
    questionBase = f"Counting up from 1, what is the {xth}{suffix} prime number?"
    answer = f"{primeNumbers[xth-1]}"
    return None, None, None, None, questionBase, answer, 1, None, None, None, None, None, None,None, None, None,None, None, None


def all_factors_of_x():
    number = randint(1,100)
    factorList = ''
    for i in range(number):
        if number % (i+1) == 0: factorList += f"{str(i+1)},"
    factorList = factorList[:-1]
    questionBase = f"Write down all the factors of {number}"
    answer = f"{factorList}"
    return None, None, None, None, questionBase, answer, 2, None, None, None, None, None, None,None, None, None,None, None, None
    




    #xxxx needs to buy chocolate bars for all the children in year x each of the xx children get a there are 8 in each packet least numberof packets to buy
    #probability of dice landing on odd number
    #probability of  number less than/more than x
    # https://qualifications.pearson.com/content/dam/pdf/GCSE/mathematics/2015/specification-and-sample-assesment/GCSE-Mathematics-2015-SAM.pdf

