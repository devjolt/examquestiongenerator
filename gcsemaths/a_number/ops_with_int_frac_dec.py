from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[10:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
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

def posNeg(num):
    if randint(1,2) == 1: num*=-1
    return num

def integerSetup(low1=10, high1=100, low2=10, high2=100):
    int1 = randint(low1, high1)
    int2 = randint(low2, high2)
    return int1, int2

def decimalSetup():
    dec1 = randint(-100, 100)/10
    dec2 = randint(-100, 100)/10
    return dec1, dec2

def mixedFractionsSetup():
    den = [2,3,4,5,6,8,9,10,12,15,16,20,25]
    frac1 = posNeg(Fraction(randint(1,50), den[randint(0,len(den)-1)]))
    frac2 = posNeg(Fraction(randint(1,50), den[randint(0,len(den)-1)]))
    return frac1, frac2

def fractionSetup():
    den = [2,3,4,5,6,8,9,10,12,15,16,20,25]
    d1 = den[randint(0,len(den)-1)]
    d2 = den[randint(0,len(den)-1)]
    frac1 = posNeg(Fraction(randint(1,d1-1), d1))
    frac2 = posNeg(Fraction(randint(1,d2-1), d1))
    return frac1, frac2

def opSetup(low=0,high=3):
    ops = ['+','-','*','/']
    op = ops[randint(low,high)]
    return op

def divideFractionSetup():
    den = [2,3,4,5,6,7,8,9,10,12,15,16,20,25]
    d1 = den[randint(0,len(den)-1)]
    d2 = den[randint(0,len(den)-1)]
    n1 = randint(1,d1-1)
    n2 = randint(1,d2-1)
    return n1, d1, n2, d2



def add_unit(request):
    y,x = integerSetup(2,9,10,100)
    op = "+"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    place, previousQ, nextQ, diagram, constant = placePrevNextDiagramConstant(0)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def add_tens_hundreds(request):
    place = 1
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    y,x = integerSetup(10,99,100,999)
    op = "+"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def subtract_unit(request):
    place = 2
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    y,x = integerSetup(2,9,10,100)
    op = "-"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def subtract_tens_hundreds(request):
    place = 3
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    y,x = integerSetup(10,99,100,999)
    op = "-"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def add_sub_integers(request):
    place = 4
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    x, y = integerSetup(10,999,10,999)
    op = opSetup(0,1)
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def multiply_unit(request):
    place = 5
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    y,x = integerSetup(2,9,10,99)
    op = "*"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def multiply_tens_hundreds(request):
    place = 6
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    y,x = integerSetup(10,99,100,999)
    op = "*"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def divide_unit(request):
    place = 6
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    y,x = integerSetup(2,9,10,99)
    op = "/"
    questionBase = f"{x} {op} {y}"
    answer = f"{x//y} remainder {x % y}"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def divide_tens_hundreds(request):
    place = 7
    previousQ, nextQ=previousNext(place)
    diagram = None
    constant = ''
    y,x = integerSetup(10,30,100,9999)
    op = "/"
    questionBase = f"{x} {op} {y}"
    answer = f"{x//y} remainder {x % y}"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))





def negative_add_unit(request):
    y,x = integerSetup(-9,-1,10,100)
    op = "+"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(8)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))


def negative_add_tens_hundreds(request):
    x, y = integerSetup(100,999,-99,-10)
    op = "+"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(9)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def negative_subtract_unit(request):
    x, y = integerSetup(10,100,-9,-2)
    op = "-"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(10)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def negative_subtract_tens_hundreds(request):
    x, y = integerSetup(100,999,-99,-10)
    op = "-"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(11)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def negative_add_sub_integers(request):
    x, y = integerSetup(-999,999,-99,99)
    op = opSetup(0,1)
    questionBase= f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(12)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def negative_multiply_unit(request):
    x, y = integerSetup(2,9,-99,-10)
    op = "*"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(13)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def negative_multiply_tens_hundreds(request):
    x, y = integerSetup(10,99,-999,-10)
    op = "*"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(14)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def negative_divide_unit(request):
    x, y = integerSetup(-99,-10,2,9)
    op = "/"
    questionBase = f"{x} {op} {y}"
    answer = f"{x//y} remainder {x % y}"
    previousQ, nextQ=previousNext(15)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def negative_divide_tens_hundreds(request):
    x, y = integerSetup(-999,-100,10,99)
    op = "/"
    questionBase = f"{x} {op} {y}"
    answer = f"{x//y} remainder {x % y}"
    previousQ, nextQ=previousNext(16)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))




def multiply_divide_random(request):
    x, y = integerSetup(10,99,100,999)
    op = opSetup(3,4)
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(17)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def multiply_integers(request):
    x, y = integerSetup()
    op = "*"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(18)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def divide_integers(request):
    x, y = integerSetup()
    y = posNeg(randint(2,20))
    op = "/"
    questionBase = f"{x} {op} {y}"
    answer = f"{round(eval(question))} remainder {x % y}"
    previousQ, nextQ=previousNext(19)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def random_integers(request):
    x, y = integerSetup()
    op = opSetup()
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(20)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def add_sub_fractions(request):
    x, y = fractionSetup()
    op = opSetup(0,1)
    question = f"{x} {op} {y}"
    answer = eval(question)
    questionBase += " (Give your answer in decimal form)"
    previousQ, nextQ=previousNext(21)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def multiply_fractions(request):
    x, y = fractionSetup()
    op = "*"
    questionBase = f"{x} {op} {y} (Give your answer in decimal form)"
    answer = eval(question)
    previousQ, nextQ=previousNext(22)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))



def divide_fractions(request):
    n1, d1, n2, d2 = divideFractionSetup()
    op = '/'
    questionBase = f"{n1}/{d1} {op} {n2}/{d2} (Give your answer in decimal form)"
    answer = f"{n1 * d2}/{n2 * d1} don't forget to simplify!"
    previousQ, nextQ=previousNext(23)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def random_fractions(request):
    x, y = integerSetup()
    op = opSetup(2)
    questionBase = f"{x} {op} {y}  (Give your answer in decimal form)"
    answer = eval(question)
    previousQ, nextQ=previousNext(24)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def add_sub_mixed_fractions(request):
    x, y = mixedFractionSetup()
    op = opSetup(1)
    questionBase = f"{x} {op} {y}  (Give your answer in decimal form)"
    answer = eval(question)
    previousQ, nextQ=previousNext(25)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))
def multiply_mixed_fractions(request):
    x, y = mixedFractionSetup()
    op = "*"
    questionBase = f"{x} {op} {y}  (Give your answer in decimal form)"
    answer = eval(question)
    previousQ, nextQ=previousNext(26)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def add_sub_decimals(request):
    x, y = decimalSetup()
    op = opSetup(1)
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(27)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def multiply_decimals(request):
    x, y = decimalSetup()
    op = "*"
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(28)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def divide_decimals(request):
    x, y = decimalSetup()
    y = posNeg(randint(2,20))
    op = "/"
    questionBase = f"{x} {op} {y}"
    answer = f"{round(eval(question))} remainder {x % y}"
    previousQ, nextQ=previousNext(29)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def random_decimals(request):
    x, y = decimalSetup()
    op = opSetup()
    questionBase = f"{x} {op} {y}"
    answer = eval(question)
    previousQ, nextQ=previousNext(30)
    diagram = None
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

