from django.shortcuts import render
from random import randint, randrange
from random import randint
from fractions import Fraction
from decimal import Decimal
import math
import sys
from physics import universal_classes_functions as ucf
from physics import variety_lists as vl
from physics import physics_symbols_constants as sc

import matplotlib.pyplot as plt
import io
import urllib, base64

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
    return ucf.moduleListGen(list_callable_functions(), 'g', 0, 1)

def module_path():
    return '/physics/nuclear_physics/'



#values in the return tuple for each modules HAVE to be in this order: (code from allArguments2 in examquestiongenerator.helperfunctions) 
# template_strings= ["previousQ", "nextQ", "diagram", "constant", "questionBase", "answer", "pre", "preans", "marks", "level", "tip", "video", "website", "piclink", "question1", "answer1", "marks1", "question2", "answer2", "marks2", "question3", "answer3", "marks3", "question4", "answer4", "marks4"] 

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random():
    modList = moduleListGen("e", 0,1) # all other modules start with e, which is useful (including other random modules, which I'm not 100 happy about, but there you go!)
    selection = randint(0,len(modList)-1)
    template_fodder = eval(f"{modList[selection]}()")
    return template_fodder

#selects a view function at random from moduleList generated list and returns everything needed to generate a view


#constants
def electron():
    return 'e = 1.6 x 10\u207b\u00b9\u2079 C'

# Individual question logic starts here
def gxa_nuclear_reactor_decay_pxax3():
    original_atom = sc.generate_atom()
    extra_neutrons = randint(1,4)
    absorbing_atom = sc.make_atom(original_atom[1]+extra_neutrons, original_atom[2], original_atom[3])
    decayed_atom = sc.generate_atom(original_atom[3] + extra_neutrons)
    decayed_atom = sc.make_atom(absorbing_atom[1], decayed_atom[2], decayed_atom[3])
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(), ucf.currentFuncName()[:2], 0, 2, ucf.currentFuncName(),module_path())
    neutron_string = f'{sc.generate_atom(0)[0]}' if extra_neutrons == 1 else f'{extra_neutrons}({sc.generate_atom(0)[0]})'
    q.questionBase = f"In an unsual nuclear reactor, some {original_atom[0]} nuclei absorb neutrons to become {absorbing_atom[0]}. These nuclei decay in {extra_neutrons} stages to become nuclei of the isotope {decayed_atom[0]}." 
    sub_q1 = f'Write down an equation to represent the formation of a {absorbing_atom[0]} nucleus from a {original_atom[0]} nucleus.'
    sub_a1 = f'{original_atom[0]} + {neutron_string} \u2192 {absorbing_atom[0]}'
    sub_q2 = f'What types of particles are emmitted when {absorbing_atom[0]} decays to become {decayed_atom[0]}?'
    sub_a2 = f'{sc.beta()}- or electrons'
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': sub_q1, 'sub_answer': sub_a1, 'sub_mark': 2 }, 
       {'sub_number': 2, 'sub_question': sub_q2, 'sub_answer': sub_a2, 'sub_mark': 1 }, 
    ]
    return q.returnAll()

def gxb_investigating_atomic_structurepxax8():
    name = ucf.currentFuncName()
    q = ucf.Question(name)
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(), name[:2], 0, 2, name,module_path())
    q.questionBase = f"Figure 1 above shows the apparatus in which {sc.alpha()} particles are directed at a metal foil in order to investigate the structure of the atom.." 
    sub_q1 = 'Give two reasons why the metal foil should be thin.'
    sub_a1 = 'The alpha particles must be able to penetrate and pass through the foil to be detected.'
    sub_q2 = f'Explain why the incident beam of {sc.alpha()} particles should be narrow.'
    sub_a2 = ''
    sub_q3 = f'Describe and explain one feature of the distribution of the scattered {sc.alpha()} particles that suggests the nucleus contains most of the mass of an atom.'
    sub_a3 = ''
    sub_q4 = f"Figure 2 shows three {sc.alpha()} particles a,b and c, with the same constant velocity incident on an atom in the metal foil. They all approach the nucleus close enough to be deflected by at least 10°. Draw the paths followed by the three {sc.alpha()} particles whose initial directions are shown by the arrows."
    sub_a4 = ''
    q.diagram = f"/diagrams/physics/{name}.jpg"
    q.questionPartList = [
        {'sub_number': 1, 'sub_question': sub_q1, 'sub_answer': sub_a1, 'sub_mark': 1 }, 
        {'sub_number': 2, 'sub_question': sub_q2, 'sub_answer': sub_a2, 'sub_mark': 2 }, 
        {'sub_number': 3, 'sub_question': sub_q3, 'sub_answer': sub_a3, 'sub_mark': 2 }, 
        {'sub_number': 4, 'sub_question': sub_q4, 'sub_answer': sub_a4, 'sub_mark': 3 }, 
    ]
    return q.returnAll()

def gxc_radioactive_nucleus_alpha_decaypxax3():
    name = ucf.currentFuncName()
    q = ucf.Question(name)
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(), name[:2], 0, 2, name,module_path())
    q.questionBase = f"A radioactive nucleus decays with the emission of an alpha partcile and a gamma-ray photon." 
    sub_q1: 'Describe the changes that occur in the proton number and nucleon number of the nucleus.'
    sub_a1: 'The proton number will decrease by two, and the nucleon number will decrease by four'
    sub_q2: 'Comment on the relative penetrating powers of the two types of ionising radiation'
    sub_a2: 'Alpha particles are relatively large and slow, and have less penetrating power than faster gamma-ray protons  because gamma protons are less likely to interact with atomic structures'
    q.questionPartList = [
        {'sub_number': 1, 'sub_question': sub_q1, 'sub_answer': sub_a1, 'sub_mark': 1 }, 
        {'sub_number': 2, 'sub_question': sub_q2, 'sub_answer': sub_a2, 'sub_mark': 2 }, 
    ]
    return q.returnAll()
'''
def gxd_radioactive_source_count():
    name = ucf.currentFuncName()
    initial, minutes, after, background = 110, 10, 84, 3
    number_decay = initial - after - background
    time = minutes * 60
    decay_constant = round((number_decay / initial) / time, 5)
    number_in_initial_sample = 
    
    q = ucf.Question(name)
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(), name[:2], 0, 2, name,module_path())
    q.questionBase = f"A radioactive source gives an initial count rate of {initial} counts per second. After {minutes} minutes the count rate is {after} counts per second. Background radiation  = {background} counts per second."
    sub_q1 = "Give three origins of the radiation that contributes to this background radiation."
    sub_a1 = "Cosmic background radiation, naturally occuring radioactive materials, medical X-rays, fallout from nuclear weapons testing and accidents"
    sub_q2 = "Calculate the decay constant of the radioactive source in s"
    sub_a2 = f"{decay_constant}s"
    sub_q3 = "Calculate the number of radioactive nuclei in the initial sample assuming that the detector counts all the radiation emitted from the source"
    sub_a3 = ""
'''
'''
def gxb_neutron_proton_model():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(), ucf.currentFuncName()[:2], 0, 2, ucf.currentFuncName(),module_path())
    q.questionBase = "The neutron-proton model of the nucleus was first put forward by Rutherford to explain the general composition of the nucleus. The existence of the neutron was not proved experimentally umil some years later."
    sub_q1 = "Give two reasons why Rutherford's neutron-proton model was considered more than an unested hypothesis when it was first put forward."
    sub_a1 = ""
p484
'''
'''
def gxb_graphpxax():
    plt.plot([1,2,3,4], [1,2,3,5], 'ro')
    plt.ylabel('numbers')
    plt.xlabel('more numbers')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    q = ucf.Question(ucf.currentFuncName())
    q.chart = urllib.parse.quote(string)
    return q.returnAll()
    '''