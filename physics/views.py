from django.shortcuts import render
from .a_particles_and_radiation import a_particles_and_radiation_views
from .d_electricity import d_electricity_views
from .e1_further_mechanics import e1_further_mechanics_views
from physics import universal_classes_functions as ucf

def home(request):
    return render(request,"physics/home.html")

def home_e_further_mechanics_and_thermal_physics(request):
    return render(request, "physics/home_e_further_mechanics_and_thermal_physics.html")

def e1_further_mechanics(request):
    return render(request, "physics/e1_further_mechanics.html")

def section_a_printable(request):
    eligible = [i for i in a_particles_and_radiation_views.modulesList() if i[-5] == 'p' and i[-3] == 'a']
    #collect list from all of the sections
    #choose one of the files and return it with context
    #add that to a list
    pass

def section_b_printable(request):
    pass

def section_a_interactive(request):
    pass
    
def section_b_interactive(request):
    pass

def paper_1_section_1(request):
    context = {}
    context['populate'] = []
    target_marks = 0
    question_dirs = ('a_particles_and_radiation', 'd_electricity', 'e_further_mechanics_thermal_physics')
    while target_marks < 60:
        dir = question_dirs[0, randint(0, len(question_dirs)-1)]
        '''
        select a logic file from within that directory. 
        select a question function from within logic file.
        '''
        #question_dict = random module from Particles and radiation, waves and optics, mechanics and materials, electricity, further mechanics (periodic motion)
        #context['populate'].append(question_dict)
        #target_marks += question_dict['marksBase']
        pass
    #return render(request, "section_template.html", context)