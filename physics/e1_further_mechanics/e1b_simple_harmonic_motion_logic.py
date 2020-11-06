from django.shortcuts import render
from random import randint, randrange
from physics import universal_classes_functions as ucf
from physics import variety_lists as vl

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
    return ucf.moduleListGen(list_callable_functions(), 'e', 0, 1)

def module_path():
    return '/physics/further_mechanics/'

def e1baa_bungeepxax2():
    q = ucf.Question(ucf.currentFuncName())
    q.questionNumber = 1
    q.questionBase = "Describe how the velocity of a bungee jumper changes during a jump from the moment he jumps off the starting platform to the next time he reaches the highest point of his jump."
    q.marksBase = 2
    q.answerBase = "The velocity of the bungee jumper increases until they reach the point of equilibrium, after which tension in the cord starts to decrease their velocity. Half way through the time period of one oscilation, the bungee jumper will briefly experience zero velocity before their rate of negative velocity in the opposite direction increases until they pass through their point of equilibrium, at which point velocity decreases as they are slowed by gravity until they reach the highest point in their rebound"
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()
'''
def e1ba1_bungee_mc():
    correct = (
        'From their highest point, the velocity of the bungee jumper increases until they reach the point of equilibrium',
        'From the lowest point in their jump, they velocity of the  bungee jumper increases until they reach the point of equilibrium',
        'After passing through the point of equilibrium, the bungee jumper will always slow down',
        'The bungee jumper will briefly experience zero velocity at two points in their jump',
        'An entire oscillation is completed when the jumper reaches their highest point in the jump',
        'The jumper will experience maximum velocity at the point of equilibrium'
    )
    incorrect = (
        'From their highest point, the velocity of the bungee jumper increases until they reach the lowest point', 
        'From their highest point, the velocity of the bungee jumper increases until they are half way through their oscillation',
        'An entire oscillation is completed when the jumper reaches their lowest point in the jump', 
        'The bungee jumper will briefly experience zero velocity at one point in their jump',
        'After passing through the point of equilibrium, the bungee jumper will always speed up',    
    )
    fact = "true"
    if randint(0,1)==0:
        fact = "false"
        correct, incorrect = incorrect, correct
    q = ucf.SelectMcDrag('multi', correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"Which of the following statements about bungee jumpers are {fact}?"
    q.questionNumber = 1
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()
'''


def e1bab_free_vibrationspxax3():
    q = ucf.Question(ucf.currentFuncName())
    q.questionNumber = 1
    q.questionBase = "The following questions are about free vibrations."
    ruler = q.item(vl.rulers)
    thing = q.item(vl.objects)

    sub2 = f'A {randint(1,50)/10} metre {ruler} is clamped to a table so that part of its length projects at right angles from the edge of the table. {q.item(vl.comments)}. A {randint(10, 200)}g {thing} is attached to the free end of the {ruler}. When the free end of the {ruler} is depressed downwards then released, the {thing} oscillates. Describe how you would find out if the oscillations of the {thing} are free oscillations.'
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':'Define free vibrations (oscillations)', 'sub_answer':'Free vibrations are where the maximum displacement of an oscilating object from the point of equilibrium (amplitude) is contstant, and no frictional forces are present', 'sub_mark':2},
        {'sub_number': 2, 'sub_question':sub2, 'sub_answer':'Measure the amplitude of each oscilation. If the amplitude decreases, frictional forces are present and the oscillation is not a free vibration', 'sub_mark':2},
    ]
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()

def e1bac_calculate_period_frequencypxax2():
    cycles = randint(5, 30)
    time_for_cycles = randint(5, 20)
    frequency = round(cycles / time_for_cycles, 2)
    time_period = round(1 / frequency, 2)
    q = ucf.Question(ucf.currentFuncName())
    thing = q.item(vl.objects)
    q.questionNumber = 1
    q.questionBase = f"A {thing} is suspended from the lower end of a vertical spring, which is dsiplaced downwards from equilibrium. It takes {time_for_cycles} seconds for {cycles} complete cycles to be completed. Giving your answer to two decimal places, calculate:" 
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':"Its time period", 'sub_answer':f'{time_period} seconds', 'sub_mark':1},
        {'sub_number': 1, 'sub_question':"The frequency of the oscillations", 'sub_answer':f'{frequency}Hz', 'sub_mark':1},
    ]
    q.marksBase = 2
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()