

from django.shortcuts import render
from random import randint
import re

def makeModuleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[-1:]  #all modules not to be used for views kept at the front of the file are not added to the usable list. Currently[5:]
    return usableModuleList

def previousNext(place): #generates url segments for previous/next buttons.
    myList = makeModuleList()
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
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, option1 = None, option2 = None, option3 = None, option4 = None, line1=None, line2=None, line3=None, line4=None, line5=None, line6=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer,
            'option1':option1, 'option2':option2, 'option3':option3, 'option4':option4, 
            'line1':line1, 'line2':line2, 'line3':line3, 'line4':line4, 'line5':line5, 'line6':line6 
            }
#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def random_pcap(request):
    moduleList = makeModuleList()
    previousQ, nextQ, diagram, constant, questionBase, answer, option1, option2, option3, option4, line1, line2, line3, line4, line5, line6 = eval(f"{moduleList[randint(0,len(moduleList)-1)]}()")
    return render(request, "multiChoiceCodeButtons.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, option1, option2, option3, option4 , line1, line2, line3, line4, line5, line6))

def makeDict(answers):
    
    order = []
    for x in range(4):
        num = randint(1,4)
        while num in order:
            num = randint(1,4)
        order.append(num)

    answerDict = {num:answer for num, answer in sorted(zip(order, answers))}

    option1 = f"{answerDict[1]}"
    option2 = f"{answerDict[2]}"
    option3 = f"{answerDict[3]}"
    option4 = f"{answerDict[4]}"

    return option1, option2, option3, option4

def c_name_main():
    questionBase = ("What will be the output of the following single line of code in a module:\n")

    things = ["__name__", "__name__", "__main__", "main", "__moduleName__.py"]
    thing = things[randint(0,len(things)-1)]

    line1 = f"\nprint({thing})"

    if thing == '__name__': correct, incorrect1, incorrect2, incorrect3 = things[2], things[-1], things[-2], "Error"
    else: correct, incorrect1, incorrect2, incorrect3 = "Error", things[0], things[-1], things[-2] 

    answers = [correct, incorrect1, incorrect2, incorrect3]
    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None

def b_list_comprehension():
    questionBase = "What is the output of the following code:\n"
    x,y = 0,0
    while x >= y:
        x, y = randint(0, 19), randint(1, 20)
    values = [x,y]
    line0 = "print"
    line1 = f"(len([i for i in range({x},{y})]))\n"
    linex = f"\n{line0}{line1}"
    answers = []
    answers.append(eval(line1))
    correct = eval(line1)
    answers.append(values[0])
    answers.append(values[1])

    poop = randint(0,1)
    if poop == 0: answers.append(eval(line1)-1)
    elif poop == 1: answers.append(eval(line1)+1)

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    line1 = linex
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None

def b_dictionary_function_output():
    var1 = chr(randint(97,123))
    var2 = chr(randint(97,123))

    if randint(0,1) == 1: prnt = "print(d)"
    else: prnt = ''

    questionBase= "What is the output on the console of the following code:"

    def fun(d,k,v):
        d[k]=v
        return(d)
    dic = {}
    correct = fun(dic, var1, var2)

    line1=f'''
    \ndef fun(d,k,v):
        d[k]=v
        {prnt}'''
    line2='''\nd = {}'''
    line3=f'''\nfun(d, "{var1}", "{var2}")'''

    if prnt == '': correct, incorrect = "there is no output", '{'+f"'{var1}':'{var2}'" + '}'
    else:incorrect, correct = "there is no output", '{'+f"'{var1}':'{var2}'" + '}'
    answers = [correct, incorrect, '{'+f"'{var2}':'{var1}'" + '}', "ValueError"]

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, line2, line3, None, None, None

def a_variable_assignment():

    questionBase = ("What will the output of the following code?")
    letters = []
    for x in range(3):
        letter = chr(randint(97, 122))
        while letter in letters:
            letter = chr(randint(97, 122))
        letters.append(letter)

    numbers = []
    for x in range(3):
        number = randint(1, 10)
        while number in numbers:
            number = randint(1, 10)
        numbers.append(number)

    orders1 = []
    for x in range(3):
        order = randint(0, 2)
        while order in orders1:
            order = randint(0, 2)
        orders1.append(order)

    orders2 = []
    for x in range(3):
        order = randint(0, 2)
        while order in orders2:
            order = randint(0, 2)
        orders2.append(order)

    line1 = f"\n{letters[0]}, {letters[1]}, {letters[2]} = {numbers[0]}, {numbers[1]}, {numbers[2]}"
    line2 = f"\n{letters[orders1[0]]}, {letters[orders1[1]]}, {letters[orders1[2]]} = {letters[orders2[0]]}, {letters[orders2[1]]}, {letters[orders2[2]]}"
    lin3 = f"{letters[0]}, {letters[1]}, {letters[2]}"
    line3 = f"\nprint({lin3})"
    exec(line1)
    exec(line2)
    correct = str(eval(lin3))
    correct = re.sub('[(,)]', '', correct)

    answers = []
    answers.append(correct.strip(","))
    for x in range(2):
        answer = f"{numbers[randint(0,2)]} {numbers[randint(0,2)]} {numbers[randint(0,2)]}"
        while answer in answers:
            answer = f"{numbers[randint(0,2)]} {numbers[randint(0,2)]} {numbers[randint(0,2)]}"
        answers.append(answer)
    answers.append("Error")

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, line2, line3, None, None, None

def a_strings_print_sep():
    letGen = []
    for i in range(3):
        n = chr(randint(97,122))
        while n in letGen:
            n = chr(randint(97,122))
        letGen.append(n)
        continue

    things = ["=", "=", "=", "-", ",", ":", ""]
    thing = things[randint(0, (len(things)-1))]

    args = ["sep", "end"]
    arg = args[randint(0, (len(args))-1)]

    seperators = ["+", "-", "*", "%", "&", "!", "*", "@", ","]
    seperator = seperators[randint(0, (len(seperators))-1)]

    if thing != "=": correct, incorrect1, incorrect2, incorrect3 = "the code is erroneous", f"{letGen[0]}{letGen[1]}{letGen[2]}", f"{letGen[0]}{seperator}{letGen[1]}{seperator}{letGen[2]}", f"{letGen[0]}{letGen[1]}{letGen[2]}{seperator}"
    elif arg == "sep": correct, incorrect1, incorrect2, incorrect3 = f"{letGen[0]}{seperator}{letGen[1]}{seperator}{letGen[2]}", f"{letGen[0]}{letGen[1]}{letGen[2]}", f"{letGen[0]}{letGen[1]}{letGen[2]}{seperator}", "the code is erroneous"
    elif arg == "end": correct, incorrect1, incorrect2, incorrect3 = f"{letGen[0]}{letGen[1]}{letGen[2]}{seperator}", f"{letGen[0]}{letGen[1]}{letGen[2]}", f"{letGen[0]}{seperator}{letGen[1]}{seperator}{letGen[2]}", "the code is erroneous"

    questionBase = ("What will be the output of the following snippet?\n")

    line1 = f"\nprint('{letGen[0]}', '{letGen[1]}', '{letGen[2]}', {arg}{thing} '{seperator}')\n"

    answers = [correct, incorrect1 , incorrect2, incorrect3]

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None



def a_escape_character_output():
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    value = randint(1, 5)
    char = "\\"
    lin1 = f"x = '{value*char}'\nprint(len(x))"
    line1 = f'''
    x = '{value*char}'
    print(len(x))'''
    questionBase = ("What is the output of the following code:\n")
    answer = "error" if value % 2 != 0 else value//2
    answers = [answer , value, 0]
    if value//2 in answers:
        answers.append("3")
    else:
        answers.append(value - 1)
    option1, option2, option3, option4 = makeDict(answers)
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None


def b_bitWiseComplex():
    while True:
        try:
            previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"

            bitwiseOps = ["<<", ">>", "&", "|"]
            bitwiseOp1 = bitwiseOps[randint(0,(len(bitwiseOps)-1))]
            bitwiseOp2 = bitwiseOps[randint(0,(len(bitwiseOps)-1))]

            regularOps = ["+", "-"]
            regularOp = regularOps[randint(0,(len(regularOps)-1))]

            answers = []
            while len(answers) != 4:

                numbers = [x for x in range(1,4)]
                number1 = numbers[randint(0,(len(numbers)-1))]
                number2 = numbers[randint(0,(len(numbers)-1))]
                number3 = numbers[randint(0,(len(numbers)-1))]
                number4 = numbers[randint(0,(len(numbers)-1))]

                line = f"\n{number1} {bitwiseOp1} {number2} {regularOp} {number3} {bitwiseOp2} {number4}"

                questionBase = ("What is the output of the following code:\n")
                line1 = line

                try:
                    thing = eval(line)
                except BaseException:
                    thing = "Error"

                if thing == 0: correct, incorrect1, incorrect2, incorrect3 = thing, "Error", numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)], numbers[randint(0, len(numbers)-1)]-numbers[randint(0, len(numbers)-1)]
                elif thing == "Error": correct, incorrect1, incorrect2, incorrect3 = thing, numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)], 0, numbers[randint(0, len(numbers)-1)]-numbers[randint(0, len(numbers)-1)]
                else: correct, incorrect1, incorrect2, incorrect3 = thing, "Error", 10, numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)]
                
                answer = correct
                answers = [correct, incorrect1, incorrect2, incorrect3]

            option1, option2, option3, option4 = makeDict(answers)
            break
        except TypeError:
            continue

    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None
        

def c_howManyLines():
    answers = []
    while len(answers) != 4:
        try:
            previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"

            rangeGen = []
            for i in range(3):
                n = randint(1,10)
                while n in rangeGen:
                    n = randint(1,10)
                rangeGen.append(n)
                continue

            smallerGreater = ["<", ">", "<=", ">="]
            questionBase = ("How many lines will be sent by the following snippet?\n")
            count = 0

            lin1 = f"ls = [[c for c in range({rangeGen[0]})] for r in range({rangeGen[1]})]"
            lin2 = f"for x in ls:\n\tif len(x) {smallerGreater[randint(0,3)]} {rangeGen[2]}:\n\t\t"
            ans = "count+=1"
            exec(lin1)
            exec(lin2+ans)

            line1 = f'''
            ls = [[c for c in range({rangeGen[0]})] for r in range({rangeGen[1]})]"
            for x in ls:"
            \tif len(x) {smallerGreater[randint(0,3)]} {rangeGen[2]}:"
            \t\tprint('')'''

            if count == 0: correct, incorrect1, incorrect2, incorrect3 = count, rangeGen[0], rangeGen[1], rangeGen[2]
            else: correct, incorrect1, incorrect2, incorrect3 = count, rangeGen[0], rangeGen[2], 0
            answers = [correct, incorrect1 , incorrect2, incorrect3]
            answer = correct

            option1, option2, option3, option4 = makeDict(answers)
            break
        except TypeError:
            continue

    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None


def d_output_of_following_code():
    questionBase = ("What will the output of the following code:\n")

    value = randint(97, 122)
    letter = chr(value)
    LETTER = chr(value-32)

    stuff = [letter, LETTER]

    first = stuff[randint(0,1)]
    second = stuff[randint(0,1)]

    nums = []
    for x in range(2):
        n = randint(1,4)
        while n in nums:
            n = randint(1,4)
        nums.append(n)

    line1 = f'''
    class {LETTER}:
    \t{LETTER} = {nums[0]}
    \tdef __init(self):
    \t\tself.{stuff[randint(0,1)]}={nums[1]}
    print(hasattr({first},'{second}'))'''

    linex = f"class {LETTER}:\n\t{LETTER} = {nums[0]}\n\tdef __init(self):\n\t\tself.{stuff[randint(0,1)]}={nums[1]}\nstuff=(hasattr({first},'{second}'))"

    try:
        exec(linex)
    except BaseException:
        stuff = "Error"

    if stuff == True: correct, incorrect1, incorrect2, incorrect3 = "True", "False", "Error", "None"
    elif stuff == False: correct, incorrect1, incorrect2, incorrect3 = "False", "True", "Error", "None"
    elif stuff == "Error": correct, incorrect1, incorrect2, incorrect3 = "Error", "False", "True", "None"
    else: correct, incorrect1, incorrect2, incorrect3 = "Error", "False", "True", "None"

    answers = [correct, incorrect1, incorrect2, incorrect3]

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None

def c_invoke_function():
    function = chr(randint(97,123))
    module = chr(randint(97,123))

    if randint(0,1) == 1: first, second, correct, incorrect = function, module, "it cannot be called", f"{function}()"
    else: second, first, correct, incorrect = function, module, f"{function} ()", "it cannot be called"

    questionBase = f"Knowing that the function knowing that the function named {function} () resides in the module named {module} and the code contains the following import statement, choose the right way to invoke the function:" 
    line1 = f'''
    from {first} import {second}
    '''
    if first == second: correct, incorrect = "it cannot be called", f"{function}()"
    answers = [correct, incorrect, f"{module}.{function}()", f"{function}"]
    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None
