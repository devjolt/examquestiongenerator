from random import randint, shuffle
import sys
from physics.a_particles_and_radiation import a1_matter_and_radiation_logic
from physics.d_electricity import daa_currentAndCharge, dab_pd_and_power, dac_resistance, dad_components_and_their_characteristics, dba_circuit_rules, dbb_more_about_resistance, dbc_emf_and_internal_resistance
from physics.e1_further_mechanics import e1a_motion_in_a_circle_logic, e1b_simple_harmonic_motion_logic

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

class Question():
    #variables for utility in template
    previousQ, nextQ = None, None
    diagram, piclink = None, None
    hint, workon, weblink, video = None, None, None, None
    qtype, correctRequired, answerReveal = None, None, None
    constantList = None # containing {name, value, units}
    constant = None
    
    #variables for main question
    questionNumber, questionBase, codeBase, answerBase, answerBase, marksBase = 1, None, None, None, None, None

    #variables for parts of a question for use with main question
    questionPartList = None # this list needs to dicts including items questionNumber, question, questionCode, answer, answerCode, answerValue, answerUnits, marks]
    
    #variables for multi choice or select and submit questions for use with main question
    a1, a1code, a2, a2code, a3, a3code, a4, a4code, a5, a5code, a6, a6code = None, None, None, None, None, None, None, None, None, None, None, None
    a7, a7code, a8, a8code, a9, a9code, a10, a10code, a11, a11code, a12, a12code = None, None, None, None, None, None, None, None, None, None, None, None
    a1ci, a2ci, a3ci, a4ci, a5ci, a6ci, a7ci, a8ci, a9ci, a10ci, a11ci, a12ci = None, None, None, None, None, None, None, None, None, None, None, None
    multi_correct = None

    #Variables for drag and drop questions for use with main question
    pair1a, pair1b, pair2a, pair2b, pair3a, pair3b, pair4a, pair4b, pair5a, pair5b, pair6a, pair6b = None, None, None, None, None, None, None, None, None, None, None, None
    pair7a, pair7b, pair8a, pair8b, pair9a, pair9b, pair10a, pair10b, pair11a, pair11b, pair12a, pair12b = None, None, None, None, None, None, None, None, None, None, None, None
    options = None

    marks = None#total marks the question is worth 

    num = randint(0,3)

    def __init__(self, function_name):
        self.function_name = function_name

        self.set_marks_and_level()

    def set_marks_and_level(self):
        self.marksBase = self.function_name[-1]

    def correct_incorrect_sequence(self): # returns four ordered strings consisting of one "correct" and three "incorrect"s to be used as flags for js.
        listy = ["incorrect" for i in range(3)]
        listy.insert(self.num, "correct") #num used to place "correct" flag where it needs to be
        self.a1ci, self.a2ci, self.a3ci, self.a4ci = listy[0], listy[1], listy[2], listy[3]

    def item(self, iterable):
        return iterable[randint(0, len(iterable)-1)]
 
    def returnAll(self):
        return{
        'currentQ': None, 'previousQ': self.previousQ, 'nextQ': self.nextQ, #previous and next question links
        'hint': self.hint, 'workon': self.workon, 'weblink': self.weblink, 'video': self.video, #string containing instruction, string describing skill demonstrated in question, link to useful resource, link to youtube video
        'diagram': self.diagram, 'piclink': self.piclink, #link to static file, url if image from web
        'qtype': self.qtype, 'correctRequired': self.correctRequired, 'answerReveal': self.answerReveal,
        'constantList':self.constantList,
        'constant':self.constant,

        'questionNumber':self.questionNumber, 'questionBase': self.questionBase, 'codeBase': self.codeBase, 'answerBase': self.answerBase, 'answerCodeBase': self.answerBase, 'marksBase': self.marksBase,

        'questionPartList': self.questionPartList,#list of dictionaries containing: sub_number, sub_question, sub_answer, sub_mark

        'a1':self.a1, 'a2':self.a2, 'a3':self.a3, 'a4':self.a4, 'a5':self.a5, 'a6':self.a6, 'a7':self.a7, 'a8':self.a8, 'a9':self.a9, 'a10':self.a10, 'a11':self.a11, 'a12':self.a12, #mc choices
        'a1code':self.a1code, 'a2code':self.a2code, 'a3code':self.a3code, 'a4code':self.a4code, 'a5code':self.a5code, 'a6code':self.a6code, 'a7code':self.a7code, 'a8code':self.a8code,'a9code':self.a9code,'a10code':self.a10code,'a11code':self.a11code,'a12code':self.a12code, #mc choices for pre formatting when code is used
        'a1ci': self.a1ci, 'a2ci':self.a2ci, 'a3ci': self.a3ci, 'a4ci': self.a4ci, 'a5ci': self.a5ci, 'a6ci': self.a6ci,'a7ci': self.a7ci,'a8ci': self.a8ci,'a9ci': self.a9ci,'a10ci': self.a10ci, 'a11ci': self.a11ci,'a12ci': self.a12ci, #correct/incorrect indicators for all options
        'multi_correct':self.multi_correct,

        'pair1a': self.pair1a, 'pair1b': self.pair1b, 'pair2a': self.pair2a, 'pair2b': self.pair2b, 'pair3a': self.pair3a, 'pair3b': self.pair3b, 'pair4a': self.pair4a, 'pair4b': self.pair4b, 'pair5a': self.pair5a, 'pair5b': self.pair5b, 
        'pair6a': self.pair6a, 'pair6b': self.pair6b, 'pair7a': self.pair7a, 'pair7b': self.pair7b, 'pair8a': self.pair8a, 'pair8b': self.pair8b, 'pair9a': self.pair9a, 'pair9b': self.pair9b, 'pair10a': self.pair10a, 'pair10b': self.pair10b, 
        'options': self.options#false option fillers
    }
            
class SelectMcDrag(Question):

    options = None#used 
    choice = None#used to change pairs into correct, incorrect lists for use in select questions, must be available for use in question
    filler_pairs = None

    #qtype = multi|select|drag, correct = [], incorrect = [], pairs = [[]], fillers = [], marks, correctRequired, numOptions
    def __init__(self, function_name, qtype = None, correct = None, incorrect = None, pairs = None, fillers = [], marks = 1, correctRequired = 1, numOptions = 4, ):
        self.qtype = qtype
        self.correct = correct
        self.incorrect = incorrect
        self.pairs = pairs
        self.fillers = fillers
        self.marks = marks
        self.correctRequired = correctRequired
        self.numOptions = numOptions
        

        self.make_nums()#needs to happen automatically, decide where correct responses will be inserted into list of mc/select/drag options
        self.select_qtype()#select question type based on combination of assets provided above

        self.function_name = function_name
        self.set_marks_and_level()

    def set_marks_and_level(self):
        self.marksBase = self.function_name[-1]
        

    def select_qtype(self):
        """based on what is inputted on instantiation, what sort of question will we be doing?
        'select', 'multi', 'drag'
        """
        choice = randint(0,1)
        if self.correct != None: #if a list of correct items is supplied
            self.populate_select_multi_using_correct_incorrect()#generate logic for select or mc question
            if self.qtype == None:#if qtype is not specified, choose randomly between valid types select and submit or multiple choice
                self.qtype = 'select' if choice == 0 else 'multi'#change flag for template
        elif self.pairs != None:#if a list of pairs is supplied, proceed with drag and drop/multi choice logic
            if self.qtype == 'drag':
                self.populate_drag_using_pairs()
            elif self.qtype == 'multi':
                self.populate_multi_using_pairs()
            elif self.qtype == 'select':
                self.populate_multi_using_pairs()
            elif self.qtype == None:
                self.qtype = 'select' if choice == 0 else 'multi'
                self.populate_multi_using_pairs()

    def populate_select_multi_using_correct_incorrect(self):
        self.answers_mangle()#insert correct responses into list of options using values generated above
        self.reveal_answer_generator()#create answerReveal for revealing answer. Must happen after answers mangle
        self.correct_incorrect_sequence()#create list containing indicators to show where answer at given index is correct or incorrect

    def populate_multi_using_pairs(self):
        self.make_correct_incorrect()
        self.answers_mangle()#insert correct responses into list of options using values generated above
        self.reveal_answer_generator()#create answerReveal for revealing answer. Must happen after answers mangle
        self.correct_incorrect_sequence()#create list containing indicators to show where answer at given index is correct or incorrect

    def make_nums(self):
        """Decide where correct responses should be inserted into list of mc options
        """
        self.nums = []
        for i in range(self.correctRequired):
            num = randint(0, self.numOptions - 1)
            while num in self.nums:
                num = randint(0, self.numOptions - 1)
            self.nums.append(num)
        self.nums = sorted(self.nums)

    def make_correct_incorrect(self):
        self.choice = randint(0, len(self.pairs)-1)
        self.correct = (self.pairs[self.choice][1],)
        self.incorrect = tuple([i[1] for i in self.pairs if self.pairs.index(i)!= self.choice]) + self.fillers
    
    def answers_mangle(self):
        """Assign self.ax mc option variables to correct and incorrect answers
        assign self.answerx correct answer variables with correct answers"""
        options = []
        for i in range(self.numOptions - self.correctRequired):#populate options with random but different incorrect answers from list, leaving space for correct answers
            option = tuple(self.incorrect)[randint(0, len(tuple(self.incorrect)) - 1)]
            while option in options:
                option = tuple(self.incorrect)[randint(0, len(tuple(self.incorrect)) - 1)]
            options.append(option)
        corList = []
        for i in range(self.correctRequired):
            cor = self.correct[randint(0, len(self.correct) - 1)]
            while cor in corList:
                cor = self.correct[randint(0, len(self.correct) - 1)]
            options.insert(self.nums[i], cor)#add correct items to options at locations in self.num
            corList.append(cor)#add correct items to corList so that they can be assigned to self.answerx variables
        self.multi_correct = corList[0]

        while len(options) != 10:#as we have a maximum of 10 self.ax multi choice option variables to assign using this list, 
            options.append(None)#list needs to be topped up to len(10) with None values to allow the following:
        self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.a10 = options[0], options[1], options[2], options[3], options[4], options[5], options[6], options[7], options[8], options[9]

        while len(corList) != 3:#as we have a maximum of 3 correct self.answerx variables to assign using this list, 
            corList.append(None)#list topped up to len(3) with None values to allow the following:
        self.answer1, self.answer2, self.answer3 = corList[0], corList[1], corList[2]

    def correct_incorrect_sequence(self):
        """assigns self.axci variables up to 10 ordered strings consisting of int(correctRequired) "correct" 
        and int(numOptions - correctRequired) "incorrect"s to be used as flags for js in template."""
        listy = ['incorrect' for i in range(self.numOptions - self.correctRequired)]#populates listy with incorrect flags
        for i in range(self.correctRequired):
            listy.insert(self.nums[i], 'correct')#adds 'correct' flags to listy at appropriate locations
        while len(listy) != 10:
            listy.append(None)#tops up len of listy to 10 to allow:
        self.a1ci, self.a2ci, self.a3ci, self.a4ci, self.a5ci = listy[0], listy[1], listy[2], listy[3], listy[4]
        self.a6ci, self.a7ci, self.a8ci, self.a9ci, self.a10ci = listy[5], listy[6], listy[7], listy[8], listy[9]

    def reveal_answer_generator(self):
        self.answerReveal = self.answer1
        if self.answer2 != None:
            self.answerReveal += f", {self.answer2}"
            if self.answer3 != None:
                self.answerReveal += f", {self.answer3}"

    

    def populate_drag_using_pairs(self):
        correct_pairs = []
        for i in range(self.correctRequired):
            pair = self.pairs[randint(0, len(self.pairs)-1)]
            while pair in correct_pairs:
                pair = self.pairs[randint(0, len(self.pairs)-1)]
            correct_pairs.append(pair)
        
        self.answerReveal = ''
        for item in correct_pairs:
            self.answerReveal += f"{item[0]} - {item[1]}; "
        self.answerReveal = self.answerReveal[:-2]

        while len(correct_pairs) < 10:
            correct_pairs.append((None, None))

        options_to_drag = []
        for i in range(self.correctRequired):
            options_to_drag.append(correct_pairs[i][1])

        if len(self.pairs) < self.numOptions:
            for i in range(self.numOptions-len(self.pairs)):
                filler = self.fillers[randint(0, len(self.fillers)-1)]
                while filler in options_to_drag:
                    filler = self.fillers[randint(0, len(self.fillers)-1)]
                options_to_drag.append(filler)
        else:
            while len(options_to_drag) != self.numOptions:
                filler = self.pairs[randint(0, len(self.pairs)-1)][1]
                while filler in options_to_drag:
                    filler = self.pairs[randint(0, len(self.pairs)-1)][1]
                options_to_drag.append(filler)


        shuffle(options_to_drag)
    
        self.pair1a, self.pair1b, self.pair2a, self.pair2b = correct_pairs[0][0], correct_pairs[0][1], correct_pairs[1][0], correct_pairs[1][1]
        self.pair3a, self.pair3b, self.pair4a, self.pair4b = correct_pairs[2][0], correct_pairs[2][1], correct_pairs[3][0], correct_pairs[3][1]
        self.pair5a, self.pair5b, self.pair6a, self.pair6b = correct_pairs[4][0], correct_pairs[4][1], correct_pairs[5][0], correct_pairs[5][1]
        self.pair7a, self.pair7b, self.pair8a, self.pair8b = correct_pairs[6][0], correct_pairs[6][1], correct_pairs[7][0], correct_pairs[7][1]
        self.pair9a, self.pair9b, self.pair10a, self.pair10b = correct_pairs[8][0], correct_pairs[8][1], correct_pairs[9][0], correct_pairs[9][1]
        
        #self.a1, self.a2, self.a3, self.a4, self.a5 = filler_pairs[0], filler_pairs[1], filler_pairs[2], filler_pairs[3], filler_pairs[4]
        #self.a6, self.a7, self.a8, self.a9, self.a10 = filler_pairs[5], filler_pairs[6], filler_pairs[7], filler_pairs[8], filler_pairs[9]

        self.options = list(options_to_drag)

    """
    After completing above functions, 
    next step here is making an html template to handle the data we feed it...

    Suggestion is two columns, one for things you're looking for and the other for options
    """

class MultipleChoice(Question):
    nums = None
    def __init__(self,function_name,  correct, incorrect, marks = 1, correctRequired = 1, numOptions = 4, qtype = 'rand'):
        self.correct = correct#list containing possible correct resonses
        self.incorrect = incorrect# list containing possible incorrect responses
        self.marks = marks
        self.correctRequired = correctRequired# number of correct choices needed for a mark to be awarded
        self.numOptions = numOptions# number of multiple choice options to choose from
        self.qtype = qtype

        self.qtype_selector()
        self.make_nums()#decide where correct responses will be inserted into list of mc options
        self.answers_mangle()#insert correct responses into list of options using values generated above
        self.reveal_answer_generator()#create answerReveal for revealing answer. Must happen after answers mangle
        self.correct_incorrect_sequence()#create list containing indicators to show where answer at given index is correct or incorrect

        self.function_name = function_name
        self.set_marks_and_level()

    def set_marks_and_level(self):
        self.marksBase = self.function_name[-1]

    def qtype_selector(self):
        if self.qtype != 'rand':
            return
        else:
            self.qtype = 'multi' if randint(0,1) == 1 else 'select'

    def make_nums(self):
        """Decide where correct responses should be inserted into list of mc options
        """
        self.nums = []
        for i in range(self.correctRequired):
            num = randint(0, self.numOptions - 1)
            while num in self.nums:
                num = randint(0, self.numOptions - 1)
            self.nums.append(num)
        self.nums = sorted(self.nums)
    
    def answers_mangle(self):
        """Assign self.ax mc option variables to correct and incorrect answers
        assign self.answerx correct answer variables with correct answers"""
        options = []
        for i in range(self.numOptions - self.correctRequired):#populate options with random but different incorrect answers from list, leaving space for correct answers
            option = tuple(self.incorrect)[randint(0, len(tuple(self.incorrect)) - 1)]
            while option in options:
                option = tuple(self.incorrect)[randint(0, len(tuple(self.incorrect)) - 1)]
            options.append(option)
        corList = []
        for i in range(self.correctRequired):
            cor = self.correct[randint(0, len(self.correct) - 1)]
            while cor in corList:
                cor = self.correct[randint(0, len(self.correct) - 1)]
            options.insert(self.nums[i], cor)#add correct items to options at locations in self.num
            corList.append(cor)#add correct items to corList so that they can be assigned to self.answerx variables

        while len(options) != 10:#as we have a maximum of 10 self.ax multi choice option variables to assign using this list, 
            options.append(None)#list needs to be topped up to len(10) with None values to allow the following:
        self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.a10 = options[0], options[1], options[2], options[3], options[4], options[5], options[6], options[7], options[8], options[9]

        while len(corList) != 3:#as we have a maximum of 3 correct self.answerx variables to assign using this list, 
            corList.append(None)#list topped up to len(3) with None values to allow the following:
        self.answer1, self.answer2, self.answer3 = corList[0], corList[1], corList[2]

    def correct_incorrect_sequence(self):
        """assigns self.axci variables up to 10 ordered strings consisting of int(correctRequired) "correct" 
        and int(numOptions - correctRequired) "incorrect"s to be used as flags for js in template."""
        listy = ['incorrect' for i in range(self.numOptions - self.correctRequired)]#populates listy with incorrect flags
        for i in range(self.correctRequired):
            listy.insert(self.nums[i], 'correct')#adds 'correct' flags to listy at appropriate locations
        while len(listy) != 10:
            listy.append(None)#tops up len of listy to 10 to allow:
        self.a1ci, self.a2ci, self.a3ci, self.a4ci, self.a5ci = listy[0], listy[1], listy[2], listy[3], listy[4]
        self.a6ci, self.a7ci, self.a8ci, self.a9ci, self.a10ci = listy[5], listy[6], listy[7], listy[8], listy[9]

    def reveal_answer_generator(self):
        self.answerReveal = self.answer1
        if self.answer2 != None:
            self.answerReveal += f", {self.answer2}"
            if self.answer3 != None:
                self.answerReveal += f", {self.answer3}"

class DragAndDrop(Question):
    """
    Select num_correct pairs
    Select num_options - num_correct pairs to make up to total needed options
    pass these into the template how do these need to go into the template

    a1

    b2
    a2    
    """
    pair1a, pair1b, pair2a, pair2b, pair3a, pair3b, pair4a, pair4b, pair5a, pair5b, pair6a, pair6b = None, None, None, None, None, None, None, None, None, None, None, None
    pair7a, pair7b, pair8a, pair8b, pair9a, pair9b, pair10a, pair10b, pair11a, pair11b, pair12a, pair12b = None, None, None, None, None, None, None, None, None, None, None, None

    filler_pairs = None
    qtype = 'drag'
    options = None

    def __init__(self, function_name, pairs, fillers, marks = 1, correctRequired = 1, numOptions = 4):
        self.pairs = pairs
        self.fillers = fillers
        self.marks = marks
        self.correctRequired = correctRequired
        self.numOptions = numOptions

        self.make_nums()
        self.select_and_assign_correct_pairs_and_options()

        self.function_name = function_name

        self.set_marks_and_level()

    def set_marks_and_level(self):
        self.marksBase = self.function_name[-1]

    def make_nums(self):
        """Decide where correct responses should be inserted into list of mc options
        """
        self.nums = []
        for i in range(self.correctRequired):
            num = randint(0, self.numOptions - 1)
            while num in self.nums:
                num = randint(0, self.numOptions - 1)
            self.nums.append(num)
        self.nums = sorted(self.nums)

    def select_and_assign_correct_pairs_and_options(self):
        correct_pairs = []
        for i in range(self.correctRequired):
            pair = self.pairs[randint(0, len(self.pairs)-1)]
            while pair in correct_pairs:
                pair = self.pairs[randint(0, len(self.pairs)-1)]
            correct_pairs.append(pair)
        

        self.answerReveal = ''
        for item in correct_pairs:
            self.answerReveal += f"{item[0]} - {item[1]}; "
        self.answerReveal = self.answerReveal[:-2]

        while len(correct_pairs) < 10:
            correct_pairs.append((None, None))

        options_to_drag = []
        for i in range(self.correctRequired):
            options_to_drag.append(correct_pairs[i][1])

        if len(self.pairs) < self.numOptions:
            for i in range(self.numOptions-len(self.pairs)):
                filler = self.fillers[randint(0, len(self.fillers)-1)]
                while filler in options_to_drag:
                    filler = self.fillers[randint(0, len(self.fillers)-1)]
                options_to_drag.append(filler)
        else:
            while len(options_to_drag) != self.numOptions:
                filler = self.pairs[randint(0, len(self.pairs)-1)][1]
                while filler in options_to_drag:
                    filler = self.pairs[randint(0, len(self.pairs)-1)][1]
                options_to_drag.append(filler)


        shuffle(options_to_drag)
    
        self.pair1a, self.pair1b, self.pair2a, self.pair2b = correct_pairs[0][0], correct_pairs[0][1], correct_pairs[1][0], correct_pairs[1][1]
        self.pair3a, self.pair3b, self.pair4a, self.pair4b = correct_pairs[2][0], correct_pairs[2][1], correct_pairs[3][0], correct_pairs[3][1]
        self.pair5a, self.pair5b, self.pair6a, self.pair6b = correct_pairs[4][0], correct_pairs[4][1], correct_pairs[5][0], correct_pairs[5][1]
        self.pair7a, self.pair7b, self.pair8a, self.pair8b = correct_pairs[6][0], correct_pairs[6][1], correct_pairs[7][0], correct_pairs[7][1]
        self.pair9a, self.pair9b, self.pair10a, self.pair10b = correct_pairs[8][0], correct_pairs[8][1], correct_pairs[9][0], correct_pairs[9][1]
        
        #self.a1, self.a2, self.a3, self.a4, self.a5 = filler_pairs[0], filler_pairs[1], filler_pairs[2], filler_pairs[3], filler_pairs[4]
        #self.a6, self.a7, self.a8, self.a9, self.a10 = filler_pairs[5], filler_pairs[6], filler_pairs[7], filler_pairs[8], filler_pairs[9]

        self.options = list(options_to_drag)

    """
    After completing above functions, 
    next step here is making an html template to handle the data we feed it...

    Suggestion is two columns, one for things you're looking for and the other for options
    """

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

#allArguments makes it less messy to return dictionary values to templates
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer=None, pre=None, preans=None, marks=None, level=None, tip=None, video=None, website=None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None, question4=None, answer4=None, marks4=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'pre':pre, 'preans':preans,
            'marks':marks, 'level':level, 'tip':tip, 'video':video, 'website':website,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            'question4':question4, 'answer4': answer4, 'marks4':marks4,
            }

#makes it even less messy and less dependent on the length of the tuple passed in, although all arguments still have to be in the order below!
def allArguments2(passed):
    template_strings = ["previousQ", "nextQ", "diagram", "constant", "questionBase", "answer", "pre", "preans", "marks", "level", "tip", "video", "website", "piclink", "question1", "answer1", "marks1", "question2", "answer2", "marks2", "question3", "answer3", "marks3", "question4", "answer4", "marks4"] 
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



"""
New modules to introduce
"""


def moduleListGen2(entireModuleList, qtype = None, start = 0, end = None): #generates a list of all functions with a certain pattern in their name
    count = -1
    required_module_list = []
    if qtype == None: # use qtype = None to use low high to select slice of list returned in relation to total modules in THIS file, low = -1 for last module only
        for thing in entireModuleList[start:end]:
            count += 1
            required_module_list.append(thing)
    else:
        for thing in entireModuleList:
            if str(thing)[start:end] == qtype: # use qtype ='anystring', low = int representing start of string, high = int representing end of string for modules selected by name
                count += 1
                required_module_list.append(thing)
    return required_module_list

def previousNext2(modList, qtype = None, start = 0, end = None, name='', module_path=''):#uses list of all functions to return previous and next modules in list
    modList = moduleListGen2(modList, qtype, start, end)#list of all possible functions in a file created here using 
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
    return f"{module_path}{previous_q}", f"{module_path}{next_q}" # e.g.:/comptia_a_plus/core_1_220_1001/aea1_ram_cmos_issue_symptom_mc

def view_builder2(module, name):
    """returns template dictionary for a named function containing everything a view needs to populate a template and display
    module = string containing name of given module
    name = string containing name of a given function
    Dependency with AllArguments2 function above
    """ 
    passed = eval(f"{module}.{name}()")#gets tuple from named function in logic file
    return passed
