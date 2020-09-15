from django.shortcuts import render
from random import randint
from gcsemaths import gcsemaths_classes_and_functions as cf

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
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

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
    return f"/gcsemaths/number/{previous_q}", f"/gcsemaths/number/{next_q}"

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[10:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
    return usableModuleList

def module_path():
    return '/gcsemaths/number/'

def ab_add_unit(request):
    q = cf.QuestionInteger(2,9,10,99,'+',1)
    a1qa.previousQ, a1qa.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_add_sub_integers(request):
    q = cf.QuestionInteger(10,99,110,999,'-',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.op = q.opSetup(0,1)
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_sub_integers(request):
    q = cf.QuestionInteger(10,99,110,999,'-',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_multiply_unit(request):
    q = cf.QuestionInteger(2,9,10,99,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_subtract_unit(request):
    q = cf.QuestionInteger(2,9,10,99,'-',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_add_tens_hundreds(request):
    q = cf.QuestionInteger(10,99,100,999,'+',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_subtract_tens_hundreds(request):
    q = cf.QuestionInteger(10,99,100,999,'-',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_multiply_tens_hundreds(request):
    q = cf.QuestionInteger(100,999,10,99,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_divide_unit(request):
    q = cf.QuestionInteger(10,99,2,9,'/',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.answer = f"{q.x//q.y} remainder {q.x % q.y}"
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_divide_tens_hundreds(request):
    q = cf.QuestionInteger(100,999,10,30,'/',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.answer = f"{q.x//q.y} remainder {q.x % q.y}"
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_add_unit(request):
    q = cf.QuestionInteger(-9,-1,10,100,'+',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_add_tens_hundreds(request):
    q = cf.QuestionInteger(100,999,-99,10,'+',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_subtract_unit(request):
    q = cf.QuestionInteger(10,100,-9,-2,'-',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_subtract_tens_hundreds(request):
    q = cf.QuestionInteger(100,999,-99,-10,'-',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_add_sub_integers(request): 
    q = cf.QuestionInteger(-999,999,-99,99,'-',1)
    q.op = q.opSetup(0,1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_multiply_unit(request):
    q = cf.QuestionInteger(2,9,-99,-10,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_multiply_tens_hundreds(request):
    q = cf.QuestionInteger(10,99,-999,-10,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_divide_unit(request):
    q = cf.QuestionInteger(-99,-10,2,9,'/',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.answer = f"{q.x//q.y} remainder {q.x % q.y}"
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_negative_divide_tens_hundreds(request):
    q = cf.QuestionInteger(-999,-100,10,99,'/',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.answer = f"{q.x//q.y} remainder {q.x % q.y}"
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_multiply_divide_random(request):
    q = cf.QuestionInteger(10,99,100,999,'-',1)
    q.op = q.opSetup(2,3)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    if q.op == '/': q.answer = f"{q.x//q.y} remainder {q.x % q.y}"
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_multiply_integers(request):
    q = cf.QuestionInteger(-999,-100,10,99,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_divide_integers(request):
    q = cf.QuestionInteger(10,100,10,100,'/',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.answer = f"{q.x//q.y} remainder {q.x % q.y}"
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_random_integers(request):
    q = cf.QuestionInteger(10,100,10,100,'/',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.op = q.opSetup(0,3)
    if q.op == '/': q.answer = f"{round(eval(q.questionBase))} remainder {q.x % q.y}"
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_add_sub_decimals(request):
    q = cf.QuestionDecimal(0,0,0,0,'-',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.op = q.opSetup(0,1)
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_multiply_decimals(request):
    q = cf.QuestionDecimal(0,0,0,0,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.answer = str(round(float(q.answer), 2))
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_divide_decimals(request):
    q = cf.QuestionDecimal(0,0,0,0,'/',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.answer = str(round(float(q.answer), 2))
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_random_decimals(request):
    q = cf.QuestionDecimal(0,0,0,0,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.opSetup(0,3)
    q.answer = str(round(float(q.answer), 2))
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_add_sub_fractions(request):
    q = cf.QuestionFraction(0,0,0,0,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answer = str(round(float(q.answer), 2))
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_multiply_fractions(request):
    q = cf.QuestionFraction(0,0,0,0,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.questionBase += " (Give your answer in decimal form)"
    q.answer = str(round(float(q.answer), 2))
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_divide_fractions(request):
    q = cf.QuestionFraction(0,0,0,0,'/',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.divideQuestionAnswer()
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_random_fractions(request):
    q = cf.QuestionFraction(0,0,0,0,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.opSetup(0,3)
    if q.op =='/': q.divideQuestionAnswer()
    q.questionBase += " (Give your answer in decimal form)"
    q.answer = str(round(float(q.answer), 2))
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))


def ab_add_sub_mixed_fractions(request):
    q = cf.QuestionMixedFraction(0,0,0,0,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answer = str(round(float(q.answer), 2))
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))

def ab_multiply_mixed_fractions(request):
    q = cf.QuestionMixedFraction(0,0,0,0,'*',1)
    q.previousQ, q.nextQ = previousNext("ab", 0, 2, cf.currentFuncName(), module_path())
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answer = str(round(float(q.answer), 2))
    return render(request, "questionAnswerButtons2.html", cf.allArguments2(q.returnAll()))
