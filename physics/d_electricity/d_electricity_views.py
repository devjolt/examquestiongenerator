from django.shortcuts import render
from random import randint
from . import daa_currentAndCharge,dab_pd_and_power,dac_resistance, dad_components_and_their_characteristics,dba_circuit_rules, dbb_more_about_resistance, dbc_emf_and_internal_resistance
import sys
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
    return ucf.moduleListGen(list_callable_functions(), 'd', 0, 1)

def current_module():
    return "d_electricity"

def electricity_home(request):
    daa, dab, dac, dad, dba, dbb, dbc = [], [], [], [], [], [], []
    for url in ucf.moduleListGen(list_callable_functions(), 'daa', 0, 3):
        name = url.replace("_", " ")[3:-5]
        daa.append({'url':url, 'name':name})
        print(daa)
    for url in ucf.moduleListGen(list_callable_functions(), 'dab', 0, 3):
        name = url.replace("_", " ")[3:-5]
        dab.append({'url':url, 'name':name})
    for url in ucf.moduleListGen(list_callable_functions(), 'dac', 0, 3):
        name = url.replace("_", " ")[3:-5]
        dac.append({'url':url, 'name':name})
    for url in ucf.moduleListGen(list_callable_functions(), 'dad', 0, 3):
        name = url.replace("_", " ")[3:-5]
        dad.append({'url':url, 'name':name})
    for url in ucf.moduleListGen(list_callable_functions(), 'dba', 0, 3):
        name = url.replace("_", " ")[3:-5]
        dba.append({'url':url, 'name':name})
    for url in ucf.moduleListGen(list_callable_functions(), 'dbb', 0, 3):
        name = url.replace("_", " ")[3:-5]
        dbb.append({'url':url, 'name':name})
    for url in ucf.moduleListGen(list_callable_functions(), 'dbc', 0, 3):
        name = url.replace("_", " ")[3:-5]
        dbc.append({'url':url, 'name':name})
    return render(request, 'physics/d_electricity.html', {'daa':daa, 'dab':dab, 'dac':dac, 'dad':dad, 'dba':dba, 'dbb':dbb, 'dbc':dbc})

def module_shortcut(selected):
    print(selected)
    if selected[0:3] == 'daa':
        context = ucf.view_builder('daa_currentAndCharge', selected)
    if selected[0:3] == 'dab':
        context = ucf.view_builder('dab_pd_and_power', selected)
    if selected[0:3] == 'dac':
        context = ucf.view_builder('dac_resistance', selected)
    if selected[0:3] == 'dad':
        context = ucf.view_builder('dad_components_and_their_characteristics', selected)
    if selected[0:3] == 'dba':
        context = ucf.view_builder('dba_circuit_rules', selected)
    if selected[0:3] == 'dbb':
        context = ucf.view_builder('dbb_more_about_resistance', selected)
    if selected[0:3] == 'dbc':
        context = ucf.view_builder('dbc_emf_and_internal_resistance', selected)
    return context

def random_printable_A_question(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-3] == 'a']
    selected = eligible[randint(0, len(eligible)-1)]
    return render(request, "physics/printablePaperMSRevealAB.html", module_shortcut(selected))

def random_printable_B_question(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-2] == 'b']
    selected = eligible[randint(0, len(eligible)-1)]
    return render(request, "physics/printablePaperMSRevealAB.html", module_shortcut(selected))
    
def random_printable_A_section(request):
    eligible = [i for i in modulesList() if i[-5] == 'p' and i[-3] == 'a']
    total_marks = 0
    target_marks = 60
    question_number = 1
    qlist = []
    while total_marks < target_marks:
        context = module_shortcut(eligible[randint(0, len(eligible)-1)])
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
        context = module_shortcut(eligible[randint(0, len(eligible)-1)])
        total_marks += int(context['marksBase'])
        context['questionNumber'] = question_number
        question_number += 1
        qlist.append(context)
        continue
    return render(request, "physics/printablePaperMSRevealAB.html", {'qlist':qlist, 'qtype':'multi'})

def random_interactive_A_question(request):
    eligible = [i for i in modulesList() if i[-4] == 'i' and i[-3] == 'a']
    selected = eligible[randint(0, len(eligible)-1)]
    return render(request, "physics/interactiveTypeDragSelectMultiReveal.html", module_shortcut(selected))

def random_interactive_B_question(request):
    eligible = [i for i in modulesList() if i[-4] == 'i' and i[-2] == 'b']
    selected = eligible[randint(0, len(eligible)-1)]
    return render(request, "physics/interactiveTypeDragSelectMultiReveal.html", module_shortcut(selected))

files = (
    (daa_currentAndCharge, 'daa_currentAndCharge'),
    (dab_pd_and_power,'dab_pd_and_power'), 
    (dac_resistance,'dac_resistance'),
    (dad_components_and_their_characteristics,'dad_components_and_their_characteristics'),
    (dba_circuit_rules, 'dba_circuit_rules'), 
    (dbb_more_about_resistance, 'dbb_more_about_resistance'), 
    (dbc_emf_and_internal_resistance, 'dbc_emf_and_internal_resistance')
)


for module in daa_currentAndCharge.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/printablePaperMSRevealAB.html', ucf.view_builder('daa_currentAndCharge', ucf.currentFuncName()))")

for module in dab_pd_and_power.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/printablePaperMSRevealAB.html', ucf.view_builder('dab_pd_and_power', ucf.currentFuncName()))")

for module in dac_resistance.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/printablePaperMSRevealAB.html', ucf.view_builder('dac_resistance', ucf.currentFuncName()))")

for module in dad_components_and_their_characteristics.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/printablePaperMSRevealAB.html', ucf.view_builder('dad_components_and_their_characteristics', ucf.currentFuncName()))")

for module in dba_circuit_rules.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/printablePaperMSRevealAB.html', ucf.view_builder('dba_circuit_rules', ucf.currentFuncName()))")

for module in dbb_more_about_resistance.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/printablePaperMSRevealAB.html', ucf.view_builder('dbb_more_about_resistance', ucf.currentFuncName()))")

for module in dbc_emf_and_internal_resistance.modulesList(): #generates every logic function as a view, depending on their required template
    exec(f"def {module}(request):\n\treturn render(request, 'physics/printablePaperMSRevealAB.html', ucf.view_builder('dbc_emf_and_internal_resistance', ucf.currentFuncName()))")



#for module in e1b_simple_harmonic_motion_logic.modulesList(): #generates every logic function as a view, depending on their required template
#    exec(f"def {module}(request):\n\treturn render(request, 'physics/physicsSectionABReveal.html', ucf.view_builder2('e1b_simple_harmonic_motion_logic', ucf.currentFuncName()))")





'''

def x_short_long_section(request):
    target = 60
    count = 0
    context = {"qlist":[]}
    func = try_modulesList()
    questionNumber = 1
    while count < target:
        #would usually get a random func, but we're using the same one all the time
        print(func)
        selected_func = func[0]
        print(selected_func)
        funcDict = ucf.view_builder2(current_module(), selected_func)
        count += funcDict['marksBase']
        funcDict['questionNumber'] = questionNumber
        context['qlist'].append(funcDict)
        questionNumber += 1
        print(context)
    return render(request, 'physics/physicsSectionABReveal.html', context)

def x_multi_section(request):
    target = 32
    count = 7
    context = {"qlist":[]}
    context['qtype'] = 'multi'
    func = try_modulesList()
    while count < target:
        #would usually get a random func, but we're using the same one all the time
        print(func)
        selected_func = 'x_multi_display'
        print(selected_func)
        funcDict = ucf.view_builder2('a1_matter_and_radiation_logic', selected_func)
        funcDict['questionNumber'] = count
        funcDict['marksBase'] = 1
        count += funcDict['marksBase']
        context['qlist'].append(funcDict)
        print(context)
    #return render(request, 'physics/physicsSectionBPrintableComplete.html', context)
    return render(request, 'physics/physicsSectionABReveal.html', context)

import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def x_short_long_pdf(request):
    template_path = 'physics/physicsSectionApdf.html'
    context = ucf.view_builder2('a1_matter_and_radiation_logic', ucf.currentFuncName())
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

'''