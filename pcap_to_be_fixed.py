#int object is not callable...
def c_positional_arguments():
    varGen = []
    for i in range(3):
        n = chr(randint(97,122))
        while n in varGen:
            n = chr(randint(97,122))
        varGen.append(n)
        continue

    numGen = []
    for i in range(2):
        n = randint(1,5)
        while n in numGen:
            n = randint(1,5)
        numGen.append(n)
        continue

    operators = ["+", "-", "*", "%", "//"]
    operator = operators[randint(0,4)]

    if randint(0,1) == 1 : first, second = varGen[0], varGen[1]
    else: first, second = varGen[1], varGen[0]
                    
    questionBase = ("What will be the output of the following snippet?\n")

    correct = 0

    print(f"{first}, {second}")

    line1 = f'''
    def {varGen[2]}({varGen[0]},{varGen[1]}):
    \treturn {first} {operator} {second}
    print({varGen[2]}({numGen[0]}, {second}= {numGen[1]}))'''
    linex = f"def {varGen[2]}({varGen[0]},{varGen[1]}):\n\treturn {first} {operator} {second}\n"
    liney = f"correct={varGen[2]}( {numGen[0]}, {second}=  {numGen[1]})"


    if first == varGen[1]: correct, incorrect1, incorrect2, incorrect3 = "the code is erroneous", numGen[0], numGen[1], eval(f"{numGen[0]}{operator}{numGen[1]}")
    else:
        exec(linex)
        correct = eval(f"{varGen[2]}( {numGen[0]}, {second}=  {numGen[1]})")
        correct, incorrect1, incorrect2, incorrect3 = eval(f"{numGen[0]}{operator}{numGen[1]}"), numGen[0], numGen[1] , "the code is erroneous"

    answers = [correct, incorrect1 , incorrect2, incorrect3]

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None



def delimiter_escape_characters():
    thing = ['''"''', "'", "\n"]
    letter = chr(randint(97, 122))
    first = thing[randint(0,len(letter))]
    second = thing[randint(0,len(letter))]
    number1 = randint(1,3)
    number2 = randint(1,5)

    questionBase = ("What is the output of the following code:\n")
    lin1 = f'''{letter} = {first*number1}{number2 * second}{first*number1}\nx=(len({letter}))'''

    linex = f'''try:\n\t{letter} = {first*number1}{number2 * second}{first*number1}\n\tcorrect=(len({letter}))\nexcept SyntaxError:\n\tcorrect = "Error"'''

    line1 = f"{letter} = {first*number1}{number2 * second}{first*number1}"
    line2 = f"x=(len({letter}))"

    try:
        exec(linex)
    except SyntaxError:
        correct = "Error"

    if correct == "Error": correct, incorrect1, incorrect2, incorrect3 = "Error", number2 , number2 + 1, number2-1
    else: correct, incorrect1, incorrect2, incorrect3 = correct, "Error" , correct + 1, correct - 1

    answers = [correct, incorrect1, incorrect2, incorrect3]

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None


'''

SHOWING INCORRECT ANSWERS AT THE MOMENT

def how_many_stars():
    rangeGen = []
    for i in range(2):
        n = randint(0,10)
        while n in rangeGen:
            n = randint(1,10)
        rangeGen.append(n)
        continue

    char = (chr(randint(42, 46)))

    choice = ["<", ">", "<=", ">="]
    smallerGreater = choice[randint(0,3)]

    questionBase = ("What will be the output of the following snippet?\n")

    count = 0

    lin1 = f"x = {rangeGen[0]*2}\nwhile x {smallerGreater}{rangeGen[1]//2}:\n\tprint('{char}',end='')\n\tx//=2\n"
    linex = f"x = {rangeGen[0]*2}\nwhile x {smallerGreater}{rangeGen[1]//2}:\n\tcount+=1\n\tx//=2"
    
    line1 = f"x = {rangeGen[0]*2}"
    line2 = f"while x {smallerGreater}{rangeGen[1]//2}:"
    line3 = "\tprint('"+char+"',end='')"
    line4 = "\tx//=2"



    if smallerGreater == "<" and rangeGen[0] == 0:correct, incorrect1, incorrect2, incorrect3 = "the code will enter an infinite loop", '', rangeGen[0] * char, rangeGen[0]//2 * char
    else:
        exec(linex)

        if count == 0:correct, incorrect1, incorrect2, incorrect3 = '', rangeGen[0] * char, rangeGen[0]//3 * char, "the code will enter an infinite loop"
        else: correct, incorrect1, incorrect2, incorrect3 = count*char, '', rangeGen[0]//3 * char, "the code will enter an infinite loop"

    answers = [correct, incorrect1 , incorrect2, incorrect3]

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, line2, line3, line4, None, None


'''


'''
THIS JUST DOESN'T WORK

def and_or():
    answers = []
    while len(answers) != 4:
        previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
        values = []
        for x in range(3):
            values.append(randint(1,5))
        symbols,andOr = ["<", ">", "==",], ["and", "or"]

        letters = []
        for x in range(3):
            letter = chr(randint(97, 122))
            while letter in letters:
                letter = chr(randint(97, 122))
            letters.append(letter)

        questionBase = (f"What value is assigned to {letters[0]}:")
            
        lin1 = f"{letters[0]} = {values[0]}\n{letters[1]} = {values[1]}\n{letters[2]} = {values[2]}"
        lin2 = f"{letters[1]} {symbols[randint(0,1)]} {letters[2]} or {letters[2]} {symbols[randint(0,1)]} {letters[1]} and {letters[1]} {symbols[randint(0,1)]} {letters[2]} or {letters[2]} {symbols[randint(0,1)]} {letters[1]}"

        line1 = f"{letters[0]} = {values[0]}"
        line2 = f"{letters[1]} = {values[1]}"
        line3 = f"{letters[2]} = {values[2]}"
        line4 = f"{letters[0]} = {letters[1]} {symbols[randint(0,1)]} {letters[2]} or {letters[2]} {symbols[randint(0,1)]} {letters[1]} and {letters[1]} {symbols[randint(0,1)]} {letters[2]} or {letters[2]} {symbols[randint(0,1)]} {letters[1]}"

        exec(lin1)
        correct = exec(lin2)
        answer = correct
        if correct == True: correct, incorrect1, incorrect2, incorrect3 = correct, "False" , 0, values[0]
        else: correct, incorrect1, incorrect2, incorrect3 = "False", "True" , 0, values[0]

        answers = [correct, incorrect1, incorrect2, incorrect3]

    option1, option2, option3, option4 = makeDict(answers)

    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, line2, line3, line4, None, None
'''


def function_output():                     
    varGen = []
    for i in range(3):
        n = chr(randint(97,122))
        while n in varGen:
            n = chr(randint(97,122))
        varGen.append(n)
        continue

    numGen = []
    for i in range(3):
        n = randint(1,5)
        while n in numGen:
            n = randint(1,5)
        numGen.append(n)
        continue

    operators = ["+", "-", "*", "%", "//"]
    operator = operators[randint(0,4)]

    if randint(0,1) == 1 : first, second = varGen[0], varGen[1]
    else: first, second = varGen[1], varGen[0]
                    
    questionBase = "What will be the output of the following snippet?\n"

    correct = 0

    line1 = f'''def {varGen[2]}({varGen[0]},{varGen[1]}):
        return {first} {operator} {second}
    print({varGen[2]}({first}={numGen[0]}, {numGen[1]}))\n'''
    
    if first == varGen[1]: correct, incorrect1, incorrect2, incorrect3 = "the code is erroneous", numGen[0], numGen[1], eval(f"{numGen[0]}{operator}{numGen[1]}")
    else:
        linex = f"def {varGen[2]}({varGen[0]},{varGen[1]}):\n\treturn {first} {operator} {second}\ncorrect={varGen[2]}({first}={numGen[0]}, {numGen[1]})"
        exec(linex)
        correct, incorrect1, incorrect2, incorrect3 = correct, numGen[randint(0,1)], eval(f"{numGen[0]}{operator}{numGen[1]}"), "the code is erroneous"

    answers = [correct, incorrect1 , incorrect2, incorrect3]

    option1, option2, option3, option4 = makeDict(answers)
    answer = correct
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"
    line1 = linex
    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, None, None, None, None, None

def arithmatic():
    previousQ, nextQ = "pcap/random_pcap", "pcap/random_pcap"

    questionBase = "What is the output of the following code:\n"
    values = [randint(1,2) for x in range(6)]
    opperators = ["/", "//", "%"]
    letter = chr(randint(97, 122))
        
    line1 = f"{letter} = {values[0]} + {values[1]} {opperators[randint(0,(len(opperators)) - 1)]} {values[2]} + {values[3]} {opperators[randint(0,(len(opperators)) - 1)]} {values[4]} + {values[5]}"
    line2 = f"print({letter})"
    linex = f"{values[0]} + {values[1]} {opperators[randint(0,(len(opperators)) - 1)]} {values[2]} + {values[3]} {opperators[randint(0,(len(opperators)) - 1)]} {values[4]} + {values[5]}"
    
    line1 = line1
    line2 = line2
    
    thing = eval(linex)

    if type(thing) == int: correct, incorrect1, incorrect2, incorrect3 = thing/1, thing+values[0], thing-values[0], thing/2
    else: correct, incorrect1, incorrect2, incorrect3 = thing/1, thing+values[0], thing-values[0], thing/2
    
    answers = [correct, incorrect1, incorrect2, incorrect3]
    answer = correct
    option1, option2, option3, option4 = makeDict(answers)

    return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, line2, None, None, None, None



'''
    def tester(request):
        previousQ = None
        nextQ = None
        diagram = None
        constant = None
        questionBase = 'Hello'
        answer = 'Nope'
        option1 = 1
        option2 = 2
        option3 = 3
        option4 = 4
        line1 = "this"
        line2 = "that"
        line3 = None
        line4 = None
        line5 = None
        line6 = None
        return previousQ, nextQ, None, None, questionBase, answer, option1, option2, option3, option4, line1, line2, None, None, None, None
'''