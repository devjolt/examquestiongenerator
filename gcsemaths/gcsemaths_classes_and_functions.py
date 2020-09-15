from random import randint
import sys
from fractions import Fraction

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

def moduleListGen(entireModuleList, qtype = None, low = 0, high = None): 
    """Returns a list of all functions with a certain pattern in their name
    qtype - string to be matched in module name to be added to list
    low, high - integers showing where string should appear in module name
    """
    count = -1
    poop = []
    if qtype == None: # use qtype = None to use low high to select slice of list returned in relation to total modules in THIS file, low = -1 for last module only
        for thing in entireModuleList[low:high]:
            count += 1
            poop.append(thing)
    else:
        for thing in entireModuleList:
            if str(thing)[low:high] == qtype: # use qtype ='anystring', low = int representing start of string, high = int representing end of string for modules selected by name
                count += 1
                poop.append(thing)
    print(poop)
    return poop

def allArguments2(passed):
    """Returns dictionary to be passed to html template containing all items in 'template strings'
    
    Arguments must be passed in as alist or tuple in the order show in 'template strings'
    An incomplete list can be passed in as long as all previous items are in the specified order
    """
    template_strings = (
        'previousQ', 'nextQ', 'diagram', 'picLink', 'hint', 'workOn', 'webLink', 'video','marks', 
        'questionBase', 'code', 'answer', 'answercode', #question text, text requiring code formatting for question, answer text, answer text requiring code formatting
        'a1', 'a2', 'a3','a4',#4 answer options for multiple choice questions
        'a1code', 'a2code','a3code','a4code',#4 answers options in code formatting
        'a1ci','a2ci','a3ci','a4ci')#indicators stating whether numbered answer is correct or incorrect for use in template
    template_dict = {}
    for i in range(len(passed)):
        template_dict.update({template_strings[i] : passed[i]})
    return template_dict

class Question():
    previousQ, nextQ, diagram, picLink, hint, workOn, webLink, video, marks = None, None, None, None, None, None, None, None, None
    questionBase, code, answer, answercode = None, None, None, None #question text, text requiring code formatting for question, answer text, answer text requiring code formatting
    a1, a2, a3, a4 = None, None, None, None#4 answer options for multiple choice questions
    a1code, a2code, a3code, a4code = None, None, None, None#4 answers options in code formatting
    a1ci, a2ci, a3ci, a4ci = None, None, None, None#indicators stating whether numbered answer is correct or incorrect for use in template

    num = randint(0,3)

    def __init__(self, answer, incorrect):
        self.answer = answer#a string containing a correct answer
        self.incorrect = incorrect# a list containing three incorrect answers

        self.getAnswersAndIndicators()
    
    def answers_mangle(self):#mangle for use with one known correct answer, and three known incorrect answers in a list
        options = self.incorrect
        options.insert(self.num, self.answer)
        self.a1, self.a2, self.a3, self.a4 = options[0],options[1],options[2],options[3]

    def correct_incorrect_sequence(self): # returns four ordered strings consisting of one "correct" and three "incorrect"s to be used as flags for js.
        listy = ["incorrect" for i in range(3)]
        listy.insert(self.num, "correct") #num used to place "correct" flag where it needs to be
        self.a1ci, self.a2ci, self.a3ci, self.a4ci = listy[0], listy[1], listy[2], listy[3]
    
    def getAnswersAndIndicators(self):
        self.answers_mangle()
        self.correct_incorrect_sequence()

    def returnAll(self):
        return(
            self.previousQ, self.nextQ, self.diagram, self.picLink, self.hint, self.workOn, self.webLink, self.video, self.marks,
            self.questionBase, self.code, self.answer, self.answercode,#question text, text requiring code formatting for question, answer text, answer text requiring code formatting
            self.a1, self.a2, self.a3, self.a4,#4 answer options for multiple choice questions
            self.a1code, self.a2code, self.a3code, self.a4code,#4 answers options in code formatting
            self.a1ci, self.a2ci, self.a3ci, self.a4ci)#indicators stating whether numbered answer is correct or incorrect for use in template




class QuestionInteger(Question):
    x, y = None, None

    def __init__(self, low1 = None, high1 = None, low2 = None, high2 = None, op = None, marks = None):
        self.low1 = low1
        self.high1 = high1
        self.low2 = low2
        self.high2 = high2
        self.op = op
        self.marks = marks

        try:
            self.xySetup()
            self.makeQuestionAnswer()
        except:
            pass

    def xySetup(self):
        self.x = randint(self.low1, self.high1)
        self.y = randint(self.low2, self.high2)

    def makeQuestionAnswer(self):
        self.questionBase = f"{self.x} {self.op} {self.y}"
        self.answer = eval(self.questionBase)

    def opSetup(self, low=0,high=3):
        ops = ['+','-','*','/']
        op = ops[randint(low,high)]
        return op
    
    def posNeg(self, num):
        if randint(1,2) == 1: num*=-1
        return num

class QuestionDecimal(QuestionInteger):
    def __init__(self, low1, high1, low2, high2, op, marks):
        self.low1 = low1
        self.high1 = high1
        self.low2 = low2
        self.high2 = high2
        self.op = op
        self.marks = marks

        self.xySetup()
        self.makeQuestionAnswer()

    def xySetup(self):
        self.x = randint(-100, 100)/10
        self.y = randint(-100, 100)/10

class QuestionFraction(QuestionInteger):
    n1, d1, n2, d2 = None, None, None, None
    
    def __init__(self, low1, high1, low2, high2, op, marks):
        self.low1 = low1
        self.high1 = high1
        self.low2 = low2
        self.high2 = high2
        self.op = op
        self.marks = marks

        self.xySetup()
        self.makeQuestionAnswer()
        self.divideFractionSetup()

    def xySetup(self):
        den = [2,3,4,5,6,8,9,10,12,15,16,20,25]
        d1 = den[randint(0,len(den)-1)]
        d2 = den[randint(0,len(den)-1)]
        self.x = self.posNeg(Fraction(randint(1,d1-1), d1))
        self.y = self.posNeg(Fraction(randint(1,d2-1), d1))

    def divideFractionSetup(self):
        den = [2,3,4,5,6,7,8,9,10,12,15,16,20,25]
        self.d1 = den[randint(0,len(den)-1)]
        self.d2 = den[randint(0,len(den)-1)]
        self.n1 = randint(1,self.d1-1)
        self.n2 = randint(1,self.d2-1)

    def divideQuestionAnswer(self):
        self.questionBase = f"{self.n1}/{self.d1} {self.op} {self.n2}/{self.d2} "
        self.answer = f"{self.n1 * self.d2}/{self.n2 * self.d1} unsimplified (don't forget to simplify)!"

class QuestionMixedFraction(QuestionInteger):
    def __init__(self, low1, high1, low2, high2, op, marks):
        self.low1 = low1
        self.high1 = high1
        self.low2 = low2
        self.high2 = high2
        self.op = op
        self.marks = marks

        self.xySetup()
        self.makeQuestionAnswer()

    def xySetup(self):
        den = [2,3,4,5,6,8,9,10,12,15,16,20,25]
        self.x = self.posNeg(Fraction(randint(1,50), den[randint(0,len(den)-1)]))
        self.y = self.posNeg(Fraction(randint(1,50), den[randint(0,len(den)-1)]))
