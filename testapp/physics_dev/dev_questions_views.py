from django.shortcuts import render
from random import randint
from . import dev_questions_logic
import sys
from testapp import testapp_classes_functions as cf

def list_callable_functions():
    """returns list of all modules in this file
    This function MUST remain in this file to work correctly!
    Used by:
    modulesList
    previousNext
    """
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    return entireModuleList

def modulesList():#this list is used by views to automatically generate views!
    return cf.moduleListGen(list_callable_functions(), 'd', 0, 1)

def auto_list_page(request):
    urls = []
    for url in modulesList():
        name = url.replace("_", " ")
        #VVV Enable this if you've got levels at the end of your function names! VVV
        name = name[2:-6]# + f" (level {thingName[-1]})"
        urls.append({'url':url, 'name':name})
    return render(request, 'testapp/autoList.html', {'urls':urls})

#def (printable -5)(interactive -4)(section a -3)(section b -2)(marks -1)
def random_printable_A_question(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-3] == 'a']
    context = cf.view_builder('dev_questions_logic', eligible[randint(0, len(eligible)-1)])
    print(eligible)
    return render(request, "testapp/printablePaperMSRevealAB.html", context)

def random_printable_B_question(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-2] == 'b']
    context = cf.view_builder('dev_questions_logic', eligible[randint(0, len(eligible)-1)])
    print(eligible)
    return render(request, "testapp/printablePaperMSRevealAB.html", context)#

def random_printable_A_section(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-3] == 'a']
    total_marks = 0
    target_marks = 60
    question_number = 1
    qlist = []
    while total_marks < 60:
        context = cf.view_builder('dev_questions_logic', eligible[randint(0, len(eligible)-1)])
        total_marks += int(context['marksBase'])
        context['questionNumber'] = question_number
        question_number += 1
        qlist.append(context)
        continue
    return render(request, "testapp/printablePaperMSRevealAB.html", {'qlist':qlist})
    

def random_printable_B_section(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-2] == 'b']
    total_marks = 0
    target_marks = 30
    question_number = 1
    qlist = []
    while total_marks < 30:
        context = cf.view_builder('dev_questions_logic', eligible[randint(0, len(eligible)-1)])
        total_marks += int(context['marksBase'])
        context['questionNumber'] = question_number
        question_number += 1
        qlist.append(context)
        continue
    return render(request, "testapp/printablePaperMSRevealAB.html", {'qlist':qlist, 'qtype':'multi'})

def random_interactive_A_question(request):
    eligible = [i for i in modulesList() if i[-4] == 'i' and i[-3] == 'a']
    context = cf.view_builder('dev_questions_logic', eligible[randint(0, len(eligible)-1)])
    print(eligible)
    return render(request, "testapp/interactiveTypeDragSelectMultiReveal.html", context)

def random_interactive_B_question(request):
    eligible = [i for i in modulesList() if i[-4] == 'i' and i[-2] == 'b']
    context = cf.view_builder('dev_questions_logic', eligible[randint(0, len(eligible)-1)])
    print(eligible)
    return render(request, "testapp/interactiveTypeDragSelectMultiReveal.html", context)

def type_dev(request):
    return render(request, "testapp/type.html", cf.view_builder('dev_questions_logic', cf.currentFuncName()))

for module in dev_questions_logic.modulesList():#generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'testapp/comptiaSelectMultiDrag.html', cf.view_builder('dev_questions_logic', cf.currentFuncName()))")



'''
What the old views looked like, just in case you ever need them, you silly goose!
def a1qa_what_is_sql(request):
    return render(request, template(), view_builder(cf.currentFuncName()))

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
'''