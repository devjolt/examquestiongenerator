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


def e1bab_bungeexixb1():
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
    q.questionBase = f"A {q.item(vl.objects)} is suspended from the lower end of a vertical spring, which is dsiplaced downwards from equilibrium. It takes {time_for_cycles} seconds for {cycles} complete cycles to be completed. Giving your answer to two decimal places, calculate:" 
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':"Its time period", 'sub_answer':f'{time_period} seconds', 'sub_mark':1},
        {'sub_number': 1, 'sub_question':"The frequency of the oscillations", 'sub_answer':f'{frequency}Hz', 'sub_mark':1},
    ]
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()

def e1bad_phase_differencepxax3():
    cycles = randrange(10, 30, 2)
    in_time = randrange(8, 24, 2)
    time = cycles / in_time
    difference_in_time = round(time / randrange(2,9,2), 2)
    phase_difference_radians = round(((2 * 3.1415925635899 * difference_in_time)/time)/ 3.1415925635899, 2)
    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = f"Two identical pendulums x and y each consist of a {q.item(vl.objects)} attached to a thread of a certain length. Each pendulum makes {cycles} complete cycles of oscillation in {in_time}s. State the phase difference, in radians, between the motion of x and that of y if:"
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':f"x passes through equilibrium {difference_in_time}s after y passes through equilibrium in the same direction", 'sub_answer':f'{phase_difference_radians}\u03c0 radians', 'sub_mark':2},
        {'sub_number': 2, 'sub_question':"x reaches maximum displacement at the same time as y reaches maximum displacement in the opposite direction.", 'sub_answer':f'\u03c0 radians', 'sub_mark':1},
    ]
    q.diagram = f'/diagrams/physics/{ucf.currentFuncName()}.jpg'
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()

def e1bba_displacement_and_direction_of_oscilating_objectpxax4():
    amplitude = randint(20, 30)
    time_period = randrange(14, 27, 2)/10
    if randint(0,1) == 0:
        direction = 'upwards'
        dis1,dis2,dis3,dis4 = amplitude, 0, -amplitude, 0
        dir1, dir2, dir3, dir4 = 'changing from up to down', 'downwards', 'changing from down to up', 'upwards'
    else:
        direction = 'downwards'
        dis1,dis2,dis3,dis4 = -amplitude, 0, amplitude, 0
        dir1, dir2, dir3, dir4 = 'changing from down to up', 'upwards', 'changing from up to down', 'downwards'
    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = f"A small {q.item(vl.objects)} attached to the end of a vertical spring oscillates with an amplitude of {amplitude}mm and a time period of {time_period}s. The object passes through equilibrium moving upwards at timer = 0. What is the displacement and direction of motion of the object:"
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':f"1\u20444 cycle later", 'sub_answer':f'{dis1}mm, {dir1}', 'sub_mark':1},
        {'sub_number': 2, 'sub_question':f"1\u20442 cycle later", 'sub_answer':f'{dis2}mm, {dir2}', 'sub_mark':1},
        {'sub_number': 3, 'sub_question':f"3\u20444 cycle later", 'sub_answer':f'{dis3}mm, {dir3}', 'sub_mark':1},
        {'sub_number': 4, 'sub_question':f"1 cycle later", 'sub_answer':f'{dis4}mm, {dir4}', 'sub_mark':1},
    ]
    q.diagram = f'/diagrams/physics/{ucf.currentFuncName()}.jpg'
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()
    
def e1bbb_acceleration_and_frequency_of_oscillating_objectpxax4():
    amplitude = randint(20, 30)
    time_period = randrange(6, 13, 2)
    direction = 'downwards'
    frequency = round(1/time_period,2)
    angular_frequency = 2*3.14159265358 / time_period
    plus = round(-(2*3.14159265359*frequency)**2 *amplitude/1000, 2)
    zero = 0
    minus = round((2*3.14159265359*frequency)**2 *amplitude/1000, 2)
    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = f"A small {q.item(vl.objects)} attached to the end of a vertical spring oscillates with an amplitude of {amplitude}mm and a time period of {time_period}s. Calculate:"
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':f"the frequency", 'sub_answer':f'{frequency}Hz', 'sub_mark':1},
        {'sub_number': 2, 'sub_question':f"the acceleration of the object when the displacement is {amplitude}mm, 0 and {-amplitude}mm", 'sub_answer':f'{plus}, {zero} and {minus}m/s\u00b2', 'sub_mark':2},
    ]    
    q.diagram = f'/diagrams/physics/e1bba_displacement_and_direction_of_oscilating_objectpxax4.jpg'
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()

def e1bbc_frequency_and_initial_accelerationpxax4():
    cycles = randrange(10, 30, 2)
    in_time = randrange(8, 24, 2)
    amplitude = randint(20, 30)
    #cycles, in_time, amplitude = 10, 20, 32
    frequency = round(cycles/in_time,2)
    angular_frequency = round(2*3.14159265358 / (1/frequency), 2)
    acceleration = round(-(2*3.14159265359*frequency)**2 *amplitude/1000, 2)
    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = f"A simple pendulum consists of a small {q.item(vl.objects)} attached to the end of a thread. {q.item(vl.comments)}. The aforementioned object is displaced from equilibrium and released. It oscillates with an amplitude of {amplitude}mm, taking {in_time}s to execute {cycles} oscillations. Calculate:"
    q.questionPartList = [
        {'sub_number': 1, 'sub_question':f"its frequency", 'sub_answer':f'{frequency}Hz', 'sub_mark':1},
        {'sub_number': 2, 'sub_question':f"its initial acceleration", 'sub_answer':f'{acceleration} m/s\u00b2', 'sub_mark':2},
    ]    
    q.piclink = q.item(vl.pendulum_links)
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()

def e1bbd_displacement_and_accelerationpxax4():
    cycles = randrange(10, 30, 2)
    in_time = randrange(8, 24, 2)
    amplitude = randint(20, 30)
    #cycles, in_time, amplitude = 10, 20, 32
    frequency = round(cycles/in_time,2)
    time = 1/frequency
    time_quarter, time_half, time_three_quarters = round(time *0.25,3), round(time*0.5, 2), round(time*0.75, 3)
    displacement_quarter = 0
    displacement_half = -amplitude 
    displacement_three_quarters = 0
    angular_frequency = round(2*3.14159265358 / (1/frequency), 2)
    acceleration = round((-angular_frequency **2)*amplitude/1000, 3)
    acceleration_quarter = 0
    acceleration_half = -acceleration
    acceleration_three_quarters = 0

    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = f"A simple pendulum consists of a small {q.item(vl.objects)} attached to the end of a thread. {q.item(vl.comments)}. The aforementioned object is displaced from equilibrium and released at t = 0 with an amplitude of {amplitude}mm, taking {in_time}s to execute {cycles} oscillations. State the displacement and calculate the acceleration when:"
    
    if randint(0,1) == 0:
        q.questionPartList = [
            {'sub_number': 1, 'sub_question':f"t = {time_quarter}s", 'sub_answer':f'Displacement = {displacement_quarter}mm, accleration ={acceleration_quarter}m/s\u00b2', 'sub_mark':2},
            {'sub_number': 2, 'sub_question':f"t = {time_half}s", 'sub_answer':f'Displacement = {displacement_half}mm, accleration ={acceleration_half}m/s\u00b2', 'sub_mark':2},
            ]  
    else:
        q.questionPartList = [
            {'sub_number': 1, 'sub_question':f"t = {time_half}s", 'sub_answer':f'Displacement = {displacement_half}mm, accleration ={acceleration_half}m/s\u00b2', 'sub_mark':2},
            {'sub_number': 2, 'sub_question':f"t = {time_three_quarters}s", 'sub_answer':f'Displacement = {displacement_three_quarters}mm, accleration ={acceleration_three_quarters}m/s\u00b2', 'sub_mark':2},
            ]    
    q.piclink = q.item(vl.pendulum_links)
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()

def e1bca_frequency_and_accelerationpxax4():
    time_period = randint(2,6)
    amplitude = randint(45, 70)
    frequency = round(1/time_period, 2)
    angular_frequency = round(2*3.14159265358 / (1/frequency), 2)
    maximum_acceleration = round((-angular_frequency **2)*amplitude/1000, 2)
    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = f"A {q.item(vl.objects)} attached to a thread oscillates in simple harmonic motion with a time period of {time_period}s and an amplitude of {amplitude}mm.  Calculate:"
    q.questionPartList = [
            {'sub_number': 1, 'sub_question':f"its frequency", 'sub_answer':f'{frequency}Hz', 'sub_mark':2},
            {'sub_number': 2, 'sub_question':f"its maximum acceleration", 'sub_answer':f'{maximum_acceleration}m/s\u00b2', 'sub_mark':2},
            ]    
    q.piclink = q.item(vl.pendulum_links)
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()
'''
def e1bcb_time_period_at_x_secondspxax6():
    
    displacement_varies = pass
    time_period = randint(2,6)
    amplitude = randint(45, 70)
    frequency = round(1/time_period, 2)
    angular_frequency = round(2*3.14159265358 / (1/frequency), 2)
    maximum_acceleration = round((-angular_frequency **2)*amplitude/1000, 2)
    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = f"A {q.item(vl.objects)} attached to a thread oscillates in simple harmonic motion with a time period of {time_period}s and an amplitude of {amplitude}mm.  Calculate:"
    q.questionPartList = [
            {'sub_number': 1, 'sub_question':f"the amplitude", 'sub_answer':f'{frequency}Hz', 'sub_mark':2},
            {'sub_number': 2, 'sub_question':f"its maximum acceleration", 'sub_answer':f'{maximum_acceleration}m/s\u00b2', 'sub_mark':2},
            {'sub_number': 3, 'sub_question':f"its maximum acceleration", 'sub_answer':f'{maximum_acceleration}m/s\u00b2', 'sub_mark':2},

            ]    
    q.piclink = q.item(vl.pendulum_links)
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),"e1", 0, 2, ucf.currentFuncName(), module_path())
    return q.returnAll()
'''
