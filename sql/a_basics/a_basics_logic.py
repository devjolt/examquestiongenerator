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
    return f"/sql/basics/{previous_q}", f"/sql/basics/{next_q}"
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
def test():
    previousQ, nextQ = None, None
    diagram, piclink, questionBase, code, hint=None,None,None,None,None
    a1, a1code, a2, a2code, a3, a3code, a4, a4code=None,None,None,None,None,None,None,None
    answer, answercode=None,None
    weblink, video=None,None
    a1ci, a2ci, a3ci, a4ci = None, None, None, None
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)

'''
SQL Basics
what is sql
sql databases
crud
keywords for creating
keywords for reading
keywords for updating
keywords for deleting
syntax
sql syntax
'''

def a1qa_what_is_sql():
    previousQ, nextQ = previousNext("a1q", 0, 3, currentFuncName())
    diagram, piclink = None, None
    true = [
        'SQL stands for structured query language',
        'SQL is used to manage data in relational database management systems',
        'SQL is a domain specific programming language',
        'SQL is not a general purpose programming language'
        'RDBMS stands for relational database management system',
        'SQL arguably consists of a data query language (DQL), a data definition language (DDL), a data control language (DCL) and a data manipulation language (DML)',
        'SQL is a declarative language with proceedural elements',
        'SQL includes a data query language (DQL)',
        'SQL includes a data definition language (DDL)',
        'SQL includes a data control language (DCL)',
        'SQL includes a data manipulation language (DML)',
    ]
    false = [
        'SQL stands for standary query language',
        'SQL stands for structured query literal',
        'SQL stands for structured question language',
        'SQL is a general purpose programming language', 
        'SQL is an functional language',
        'SQL is an object oriented language',
        'SQL does not include a data query language',
        'SQL does not include a data definition language (DDL)',
        'SQL does not include a data control language (DCL)',
        'SQL does not include a data manipulation language (DML)',
        ]
    code, hint = None, None
    answer, a1, a2, a3, a4, q, num = true_false_options_mangle(true, false)
    a1ci, a2ci, a3ci, a4ci = correct_incorrect_sequence(num)
    questionBase = f'Which of the following statements about SQL is {q}:'
    a1code, a2code, a3code, a4code, answercode = None, None, None, None, None
    help, weblink, video = None, None, None    
    return (previousQ, nextQ, diagram, piclink, questionBase, code, hint, weblink, video, a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode, a1ci, a2ci, a3ci, a4ci)