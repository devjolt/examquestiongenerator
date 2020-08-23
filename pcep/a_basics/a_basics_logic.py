from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal
import math
import sys

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
    return f"/pcep/a_basics/{previous_q}", f"/pcep/a_basics/{next_q}"
'''
def e4_at_the_fairground_random():
    modList = moduleListGen("e4q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")
'''

def true_false_options_mangle(list1, list2): #generates a correct answer, a true or false indicator for the question, and 4 options, one of which is the correct answer
    options, num = [], randint(0,3)#place to put answers, and a random index value to put the correct answer
    if randint(0,1) == 0: # deciced whether correct answer will be a true or false statement
        tf = "true"
        answer = list1[randint(0, len(list1)-1)]# if true, we grab a correct answer from list1 (true list)
        while len(set(options)) != 3: #this turns options into a set to eliminate duplicates and throws in incorrect answers until we have enough to populate 4 possible answers
            options.append(list2[randint(0, len(list2)-1)])
    else:
        tf = "false" # same again if false
        answer = list2[randint(0, len(list2)-1)]
        while len(set(options)) != 3:
            options.append(list1[randint(0, len(list1)-1)])
    options.insert(num, answer) # inserts answer into a random place (num defined earlier)
    num2 = options.index(answer)
    answer = f"{num+1}. {answer}" #answer now includes number of correct answer to make like easier
    return answer, options[0], options[1], options[2], options[3], tf, num # num also returned because of use in correct_incorrect_sequence()

def correct_incorrect_sequence(num): # returns four ordered strings consisting of one "correct" and three "incorrect"s to be used as flags for js.
    listy = ["incorrect" for i in range(3)]
    listy.insert(num, "correct") #num used to place "correct" flag where it needs to be
    for thing in listy:
        yield thing # returned as four flags, one of which is correct, to be assigned to varables and passed into template as context


# Just me making sure everything works...
def e1qa_test():
    previousQ, nextQ = None, None
    diagram, piclink, questionBase, code, hint=None,None,None,None,None
    a1, a1code, a2, a2code, a3, a3code, a4, a4code=None,None,None,None,None,None,None,None
    answer, answercode=None,None
    weblink, video=None,None
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

# Individual question logic starts here
def a1qa_interpreting_the_interpreter():
    previousQ, nextQ = previousNext("a1q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = [
        'the interpreter translates source code into machine code every time the code is run',
        'the interpreter usually reads code from top to bottom and left to right',
        'the interpreter will inform you where the error is and what caused it',
        'the interpreter may detect errors at some distance from their real causes',
        'the interpreter will execute line by line seperately',
        'the interpreter checks if all lines are correct alphabetically, lexically, syntactically and semantically',
        'the interpreter will inform you where the error is and what caused it',
        'The interpreter may detect errors at some distance form their real causes',
        'an interpreter will execute line by line seperately',
        'the interpreter performs the \'read check execute\' cycle repeated many times',
        'the interpreter performs the \'read check execute\' cycle more times than lines in source file',
        'a significant part of the source code may be exectuted successflly before the interpreter finds an error',
        'the python interpreter is not a compiler',
        'interpreted source code cannot just be distributed as the end user also needs an interpreter to execute it',
    ]
    false = [
        'the interpreter translates source code into machine code only once and then never again',
        'the interpreter usually reads code from top to bottom and right to left',
        'the interpreter will inform you what caused an error but not which line it originated on',
        'the interpreter will inform you which line it originated on but not what caused an error ',
        'the interpreter will always detect errors at at the location of their exact cause',
        'the interpreter will execute all lines at the same time',
        'the interpreter checks if all lines are correct alphabetically, lexically and syntactically but not semantically',
        'the interpreter checks if all lines are correct alphabetically, lexically and semantically but not syntactically',
        'the interpreter checks if all lines are correct alphabetically, semantically and syntactically but not lexically',
        'the interpreter checks if all lines are correct semantically,syntactically and lexically but not  alphabetically',
        'the interpreter performs the \'read check execute\' cycle once',
        'the interpreter performs the \'read check execute\' cycle exactly once for every line in the source file',
        'a significant part of the source code may be exectuted successflly before the interpreter finds an error',
        'an interpreter doesn\'t execute any code until it has all been interpreted',
        'if there is an error in the code, the interpreter will not execute any of it',
        'the python interpreter is a compiler',
        'interpreted source code is ready to be distributed',
    ]
    code, hint = None, None
    answer, a1, a2, a3, a4, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    questionBase = f'Which of the following statements about the python interpreter is {q}:'
    a1code, a2code, a3code, a4code, answercode = None, None, None, None, None
    help, weblink, video = None, None, None    
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

def a1qb_compilation_and_the_compiler():
    previousQ, nextQ = previousNext("a1q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = [
        'the compiler translates source code into machine code before it is run',
        'the python interpreter is not a compiler',
        'compiled source code is translated once and can then be run multiple times',
        'source code must be compiled again each time source code is modified',
        'compiling source code creates a new executable file',
        'a program which translates source code in machine code is called a compiler or translator', 
        'if a compiler finds an error whilst compiling, it ends translation straight away and gives an error message',
        'python is not a compiled language'     
    ]
    false = [
        'the compiler executes source code whilst it is being translated into machine code',
        'the python interpreter is a compiler',
        'compiled source code is translated each time it is run',
        'modifications to source code automatically modify executed machine code',
        'compiled machine code is saved in the same file as its original source code',
        'a program which creates an executable file from source code is called an interpreter', 
        'if a compiler finds an error whilst compiling, it continues to the end of the file allowing partial execution',  
    ]
    code, hint = None, None
    answer, a1, a2, a3, a4, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    questionBase = f'Which of the following statements about interpreters and compilers is {q}:'
    a1code, a2code, a3code, a4code, answercode = None, None, None, None, None
    help, weblink, video = None, None, None
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

def a1qc_machine_higher_level_natural_languages():
    previousQ, nextQ = previousNext("a1q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = [
        'machine languages are developed by humans',
        'natural languages are spoken between humans',
        'the rudimentary language understood by computers is known as machine language',
        'a complete set of known commands in machine language is known as an instruction list',
        'machine language is different to native language',
        'a higher level coding language allows humans to use a language they can comprehend and that computers can understand',
        'higher level languages are more similar to natural languages than machine language',
        'they allow humans to express commands to computers that are much more complex than those offered by ILS',
        'a program written in a high-level language is called source code',
        'source code is different to machine code exectuted by computers',
        'a file containing the source code is called the source file',
        'ILS stands for Instruction List Set',
    ]
    false = [
        'ILS stands for Intuitive Language Source',
        'machine languages are developed by computers',
        'natural languages are spoken between machines',
        'the rudimentary language understood by computers is known as source code',
        'the rudimentary language understood by computers is known as natural language',
        'a complete set of known commands in machine language is known as source code',
        'a complete set of known commands in machine language is known as natural language',
        'machine language is the same as native language',
        'machine language is the same as source code',
        'a natural language allows humans to use a language they can comprehend and that computers can understand',
        'higher level languages are more different to natural languages than machine language',
        'machine language allows humans to express commands to computers that are much more complex than those offered by source code',
        'machine language is called source code',
        'source code is another name for machine code exectuted by computers',
        'a file containing the source code is called the ILS',
    ]
    code, hint = None, None
    answer, a1, a2, a3, a4, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    questionBase = f'Which of the following statements about machine language, natural language and higher level coding languages is {q}:'
    
    a1code, a2code, a3code, a4code, answercode = None, None, None, None, None
    help, weblink, video = None, None, None
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

def a1qd_language_elements():
    previousQ, nextQ = previousNext("a1q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = [
        'an alphabet is a set of symbols used to build words',
        'the instruction list is the alphabet of a machine language',
        'a lexis is a set of words which a language offers its users',
        'a syntax is a set of rules  used to determine if a certain string of words form a valid sentence',
        'semantics are a set of rules determining if a certain phrase makes sense',
        'alphabetically a program needs to be written in a recognisable script',
        'lexically, a programming language has its own vocabulary',
        'programiming dictionary is smaller than an natural language',
        'each language has rules syntactically',
        'a program has to make semantic sense',
    ]
    false = [
        'an alphabet is a set of words',
        'the instruction list is the alphabet of a machine language',
        'a syntax is a set of words which a language offers its users',
        'a lexis is a set of rules used to determine if a certain string of words form a valid sentence',
        'an instruction list is a set of rules determining if a certain phrase makes sense',
        'alphabetically a program needs to be written in lower case',
        'each programming language has its own alphabet',
        'the dictionary of a programming language is larger than an natural language',
        'each language has the same syntax',
        'as long as a program has correct lexis, it does not need to make semantic sense',
    ]
    code, hint = None, None
    answer, a1, a2, a3, a4, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    questionBase = f'Which of the following statements about the elements of a language is {q}:'
    a1code, a2code, a3code, a4code, answercode = None, None, None, None, None
    help, weblink, video = None, None, None
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

def a1qe_python():
    previousQ, nextQ = previousNext("a1q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = [
        'Python is a widely-used, interpreted, object-oriented, and high-level programming language',
        'python has dynamic semantics',
        'python is used for general-purpose programming.',
        'the name of the Python programming language comes from an old BBC television comedy sketch series called Monty Python\'s Flying Circus', 
        'Python is an interpreted language',
        'Python is an object-oriented language',
        'Python is a high-level programming language',
        'Python files have the extension .py'
    ]
    false = [
        'Python is a not a widely-used, interpreted, object-oriented, and high-level programming language',
        'python does not have dynamic semantics',
        'python is used only for web development',
        'python is used only for data science',
        'python is used only in machine learning',
        'python is used only for teaching programming',
        'the name of the Python programming language comes from the snake', 
        'the Python programming language is named after the snake', 
        'Python is a compiled language',
        'Python is not an object-oriented language',
        'Python is a machine language',
        'Python files have the extension .txt'
    ]
    code, hint = None, None
    answer, a1, a2, a3, a4, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    questionBase = f'Which of the following statements about the Python programming language is {q}:'
    a1code, a2code, a3code, a4code, answercode = None, None, None, None, None
    help, weblink, video = None, None, None
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

def a1qf_python_keywords():
    previousQ, nextQ = previousNext("a1q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = [
        'False', 'await', 'else', 'import', 'pass','None', 'break', 'except', 'in', 'raise','True',
        'class', 'finally', 'is', 'return','and', 'continue', 'for', 'lambda', 'try','as', 'def',
        'from', 'nonlocal', 'while','assert', 'del', 'global', 'not', 'with','async', 'elif', 'if', 'or', 'yield'
    ]
    false = [
        'Incorrect', 'hold tight', 'but', 'findme', 'Nothing','Negative', 'stop', 'Maybe', 'Put', 'lift','Correct',
        'thing', 'eventually', 'could', 'dothis','plus', 'keepgoing', 'silly', 'beta', 'attempt','whilst', 'func',
        'apart', 'there', 'during','assume', 'delete', 'worldwide', 'never', 'ifandonlyif', 'assuming', 'alternatively', 'use'
    ]
    code, hint = None, 'Keywords are the reserved words in Python. We cannot use a keyword as variable name, function name or any other identifier.'
    answer, a1, a2, a3, a4 = None, None, None, None, None
    answercode, a1code, a2code, a3code, a4code, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    areNot = "is" if q == "true" else "is not"
    questionBase = f'Which of the following {areNot} a python keyword:'
    
    help, weblink, video = hint, 'https://www.programiz.com/python-programming/keyword-list', None
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

def a1qg_indentation_and_spacing():
    previousQ, nextQ = previousNext("a1q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = [
        'if a line ends with a colon (:), the following line must be indented',
        'all lines in a block must have the same indentation',
        'if indentation level is not correct, the interpreter will highlight the indentation error and stop',
        'usually, tab is used for indentation',
        'indentation in a block is mandatory in python'
    ]
    false = [
        'if a line ends with a semi colon (;), the following line must be indented',
        'if a line ends with a colon (:), the following line must be at the same level of indentation',
        'a block must have the same indentation as the previous block',
        'if indentation level is not correct, the interpreter will highlight the indentation error and continue to execute',
        'indentation can only be done by pressing space the right number of times',
        ]
    code, hint = None, None
    answer, a1, a2, a3, a4, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    questionBase = f'Which of the following statements about the Python programming language is {q}:'
    a1code, a2code, a3code, a4code, answercode = None, None, None, None, None
    help, weblink, video = None, None, None    
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

'''
literals: Boolean, integer, floating-point numbers, scientific notation, strings
definitions of all literals and literal
focus on boolean
integer
floating-point
scientific notiation
strings
code results (types, outputs, errors)

comments
#
Doctstrings
commenting out

the print() function
the input() function

numeral systems (binary, octal, decimal, hexadecimal)

numeric operators: ** * / % // + –

string operators: * +

assignments and shortcut operators
'''