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

def allArguments2(passed):
    template_strings= ["previousQ", "nextQ", "diagram", "constant", "questionBase", "answer", "pre", "preans", "marks", "level", "tip", "video", "website", "piclink", "question1", "answer1", "marks1", "question2", "answer2", "marks2", "question3", "answer3", "marks3", "question4", "answer4", "marks4"] 
    template_dict = {}
    for i in range(len(passed)):
        template_dict.update({template_strings[i] : passed[i]})
    return template_dict

