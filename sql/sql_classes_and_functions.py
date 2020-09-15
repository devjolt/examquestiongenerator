from random import randint
import sys

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

class question():
    previousQ, nextQ = None, None
    diagram, piclink, questionBase, code, hint, weblink, video = None, None, None, None, None, None, None
    a1, a1code, a2, a2code, a3, a3code, a4, a4code, answer, answercode = None, None, None, None, None, None, None, None, None, None
    a1ci, a2ci, a3ci, a4ci, workOn = None, None, None, None, None

    num = randint(0,3)

    def correct_incorrect_sequence(self): # returns four ordered strings consisting of one "correct" and three "incorrect"s to be used as flags for js.
        listy = ["incorrect" for i in range(3)]
        listy.insert(self.num, "correct") #num used to place "correct" flag where it needs to be
        self.a1ci, self.a2ci, self.a3ci, self.a4ci = listy[0], listy[1], listy[2], listy[3]

    def returnAll(self):
        return(self.previousQ, self.nextQ, self.diagram, self.piclink, self.questionBase, self.code, self.hint, self.weblink, self.video, 
                    self.a1, self.a1code, self.a2, self.a2code, self.a3, self.a3code, self.a4, self.a4code, self.answer, self.answercode, self.a1ci, self.a2ci, self.a3ci, self.a4ci, self.workOn)     
    
class trueFalse(question):
    tf = None
    
    def __init__(self, true, false):
        self.true = true
        self.false = false

        self.getAnswersAndIndicators()

    def true_false_options_mangle(self): #generates a correct answer, a true or false indicator for the question, and 4 options, one of which is the correct answer
        options = [] #place to put answers
        if randint(0,1) == 0: # deciced whether correct answer will be a true or false statement
            self.tf = "true"
            self.answer = self.true[randint(0, len(self.true)-1)]# if true, we grab a correct answer from list1 (true list)
            while len(set(options)) != 3: #this turns options into a set to eliminate duplicates and throws in incorrect answers until we have enough to populate 4 possible answers
                options.append(self.false[randint(0, len(self.false)-1)])
        else:
            self.tf = "false" # same again if false
            self.answer = self.false[randint(0, len(self.false)-1)]
            while len(set(options)) != 3:
                options.append(self.true[randint(0, len(self.true)-1)])
        options.insert(self.num, self.answer) # inserts answer into a random place (num defined earlier)
        num2 = options.index(self.answer)#can be printed as a check
        self.answer = f"{self.num+1}. {self.answer}" #answer now includes number of correct answer to make like easier
        self.a1, self.a2, self.a3, self.a4 = options[0],options[1],options[2],options[3]

    def getAnswersAndIndicators(self):
        self.true_false_options_mangle()
        self.correct_incorrect_sequence()

class trueFalseCode(trueFalse):
    def true_false_options_mangle(self): #generates a correct answer, a true or false indicator for the question, and 4 options, one of which is the correct answer
        options = [] #place to put answers
        if randint(0,1) == 0: # deciced whether correct answer will be a true or false statement
            self.tf = "true"
            self.answer = self.true[randint(0, len(self.true)-1)]# if true, we grab a correct answer from list1 (true list)
            while len(set(options)) != 3: #this turns options into a set to eliminate duplicates and throws in incorrect answers until we have enough to populate 4 possible answers
                options.append(self.false[randint(0, len(self.false)-1)])
        else:
            self.tf = "false" # same again if false
            self.answer = self.false[randint(0, len(self.false)-1)]
            while len(set(options)) != 3:
                options.append(self.true[randint(0, len(self.true)-1)])
        options.insert(self.num, self.answer) # inserts answer into a random place (num defined earlier)
        num2 = options.index(self.answer)#can be printed as a check
        self.answer = f"{self.num+1}. {self.answer}" #answer now includes number of correct answer to make like easier
        self.a1code, self.a2code, self.a3code, self.a4code = options[0],options[1],options[2],options[3]

class selectCorrect(question):
    def __init__(self, correct, incorrect):
        self.correct = correct
        self.incorrect = incorrect
    
    def answers_mangle(self):#mangle for use with one known correct answer, and three known incorrect answers in a list
        options = self.incorrect
        options.insert(self.num, self.correct)
        self.a1, self.a2, self.a3, self.a4 = options[0],options[1],options[2],options[3]

    def getAnswersAndIndicators(self):
        self.answers_mangle()
        self.correct_incorrect_sequence()

class selectCorrectCode(selectCorrect):
    def answers_mangle(self):#mangle for use with one known correct answer, and three known incorrect answers in a list
        options = self.incorrect
        options.insert(self.num, self.correct)
        self.a1code, self.a2code, self.a3code, self.a4code = options[0],options[1],options[2],options[3]

def moduleListGen(entireModuleList, qtype = None, low = 0, high = None): #generates a list of all functions with a certain pattern in their name
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
    template_strings = ('previousQ', 'nextQ', 'diagram', 'piclink', 'questionBase', 'code', 'hint', 'weblink', 'video', 'a1', 'a1code', 'a2', 'a2code', 'a3', 'a3code', 'a4', 'a4code', 'answer', 'answercode', 'a1ci', 'a2ci', 'a3ci', 'a4ci', 'workOn')
    template_dict = {}
    for i in range(len(passed)):
        template_dict.update({template_strings[i] : passed[i]})
    return template_dict

#allows generation of a sections worth of questions to be passed to a mega template!
def allArgumentsSection(passed):
    template_strings = ["previousQ", "nextQ","diagram", "constant", "questionBase", "answer", "pre", "preans", "marks", "level", "tip", "video", "website", "piclink", "question1", "answer1", "marks1", "question2", "answer2", "marks2", "question3", "answer3", "marks3", "question4", "answer4", "marks4"] 
    template_dict = {}
    
    for thing in passed:
        for i in range(len(passed)):
            template_dict.update({template_strings[i] + f"{i}" : thing[i]})
    print(template_dict)
    return template_dict

'''
for each iterable in passed(up to 6?)
remove previousq and nextq from starts of each li
'''