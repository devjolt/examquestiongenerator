from django.shortcuts import render
from random import randint
from . import a1_matter_and_radiation_logic
import sys
from physics import physics_classes_functions as cf
from physics import universal_classes_functions as ucf

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

def modulesList():#this list is used by urls to automatically generate paths based on what's in this file
    return ucf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def current_module():
    return "a_particles_and_radiation"

def particles_and_radiation_home(request):
    urls = []
    for url in modulesList():
        name = url.replace("_", " ")
        #VVV Enable this if you've got levels at the end of your function names! VVV
        name = name[2:-5]# + f" (level {thingName[-1]})"
        urls.append({'url':url, 'name':name})
    return render(request, 'physics/a_matter_and_radiation.html', {'urls':urls})

def random_printable_A_question(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-3] == 'a']
    context = ucf.view_builder('a1_matter_and_radiation_logic', eligible[randint(0, len(eligible)-1)])
    return render(request, "physics/printablePaperMSRevealAB.html", context)

def random_printable_B_question(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-2] == 'b']
    context = ucf.view_builder('a1_matter_and_radiation_logic', eligible[randint(0, len(eligible)-1)])
    return render(request, "physics/printablePaperMSRevealAB.html", context)

def random_printable_A_section(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-3] == 'a']
    total_marks = 0
    target_marks = 60
    question_number = 1
    qlist = []
    while total_marks < target_marks:
        context = ucf.view_builder('a1_matter_and_radiation_logic', eligible[randint(0, len(eligible)-1)])
        total_marks += int(context['marksBase'])
        context['questionNumber'] = question_number
        question_number += 1
        qlist.append(context)
        continue
    return render(request, "physics/printablePaperMSRevealAB.html", {'qlist':qlist})

def random_printable_B_section(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-2] == 'b']
    total_marks = 0
    target_marks = 25
    question_number = 7
    qlist = []
    while total_marks < target_marks:
        context = ucf.view_builder('a1_matter_and_radiation_logic', eligible[randint(0, len(eligible)-1)])
        total_marks += int(context['marksBase'])
        context['questionNumber'] = question_number
        question_number += 1
        qlist.append(context)
        continue
    return render(request, "physics/printablePaperMSRevealAB.html", {'qlist':qlist, 'qtype':'multi'})

def random_interactive_A_question(request):
    eligible = [i for i in modulesList() if i[-4] == 'i' and i[-3] == 'a']
    context = ucf.view_builder('a1_matter_and_radiation_logic', eligible[randint(0, len(eligible)-1)])
    return render(request, "physics/interactiveTypeDragSelectMultiReveal.html", context)

def random_interactive_B_question(request):
    eligible = [i for i in modulesList() if i[-4] == 'i' and i[-2] == 'b']
    context = ucf.view_builder('a1_matter_and_radiation_logic', eligible[randint(0, len(eligible)-1)])
    print(eligible)
    return render(request, "physics/interactiveTypeDragSelectMultiReveal.html", context)



files = (
    (a1_matter_and_radiation_logic, 'a1_matter_and_radiation_logic'),
)

for module in a1_matter_and_radiation_logic.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/physicsSectionABReveal.html', ucf.view_builder('a1_matter_and_radiation_logic', ucf.currentFuncName()))")
    

#for module in e1b_simple_harmonic_motion_logic.modulesList(): #generates every logic function as a view, depending on their required template
#    exec(f"def {module}(request):\n\treturn render(request, 'physics/physicsSectionABReveal.html', cf.view_builder2('e1b_simple_harmonic_motion_logic', cf.currentFuncName()))")
