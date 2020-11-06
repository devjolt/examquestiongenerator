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

def modulesList():#this list is used by views to automatically generate views!
    return ucf.moduleListGen(list_callable_functions(), 'd', 0, 1)

def module_path():
    return '/physics/electricity/'

def temp_res_setup():
    complist = ["hairdryer", "buzzer", "klaxon warning of immenent alien invasion", "stubborn android can", "disturbing animatronic lettuce", "retro arcade cabinet", "disco light", "subwoofer", "warning becon", "pair of hair straighteners", "robotic monkey", "electric pencil sharpener"]
    component = complist[randint(0, len(complist)-1)]
    option = randint(1,3)
    pd = randint(2,20)
    current = randint(5, 50)/10
    power= current * pd
    resistance = round(pd/current, 3)
    length = randint(5,200)/10
    return component, option, pd, current, power, resistance, length

def dad1_temperature_of_a_fillamentpxax3():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, pd, current, power, resistance, length= temp_res_setup()
    increase_decrease = "increase" if randint(1,2) == 1 else "decrease"
    current_pd = "current" if randint(1,2) == 1 else "potential difference"
    happen = ''
    if current_pd == current:
        if increase_decrease == "increase": happen = "increase"
        else: happen = "decrease"
    else:
        if increase_decrease == "increase": happen = "decrease"
        else: happen = "increase"
    q.constant = None
    q.questionBase = f"A filament bulb is labelled '{pd} V, {round(power, 1)} W'."
    question1 = f"Calculate its current and resistance at {pd} V."
    answer1 = f"Current = {current}A, resistance = {resistance} Ohms"
    question2 = f'What would happen to the temperature in the fillament bulb if the {current_pd} in the fillament were to {increase_decrease}?'
    answer2 = f'The resistance and temperature of the fillament would {happen}.'
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
    ]
    return q.returnAll()

def dad2_temperature_of_a_thermistorpxax4():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = '/diagrams/physics/circuit_ab_series.jpg'
    component, option, pd, current, power, resistance, length= temp_res_setup()
    cell = [["alkaline AA", 1.5],["of those square", 9],["Li-Mn", 3.7],["NiMh", 1.2],["lead acid car", 12],["Nuclear power cell belonging to an advanced robot assassin sent from the future", 15,000]]
    selection = randint(0,len(cell)-1)
    cell_type = cell[selection][0]
    cell_pd = cell[selection][1]
    temp1 = randint(0, 100)
    temp2 = randint(0, 100)
    res1 = randint(400, 5000)
    res2 = randint(400, 5000)
    number_of_cells = randint(2,6)
    current1 = round((number_of_cells*cell_pd)/res1, 4)
    current2 = round((number_of_cells*cell_pd)/res2, 4)
    q.constant = None

    q.questionBase = f"The circuit above is from a {component}. The thermistor at point a in the circuit has a resistance of {res1} \u03A9 at {temp1} \u00B0C and {res2} \u03A9 at {temp2} \u00B0C. It is connected in series with an ammeter at point b and {number_of_cells} {cell_type} batteries each delivering {cell_pd}V as shown above."
    question1 = f"Calculate the ammeter reading when the thermistor is at {temp1} \u00B0C"
    answer1 = f"{current1}A"
    question2 = f"Calculate the ammeter reading when the thermistor is at {temp2} \u00B0C"
    answer2 = f'{current2}A'
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
    ]
    return q.returnAll()

def dad3_variable_temperature_resistancepxax4():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram = None
    component, option, pd, current, power, resistance, length= temp_res_setup()
    q.constant = None
    temp1 = randint(1,20)
    temp2 = randint(21,100)
    tempDiff = temp2-temp1
    temp3 = randint(temp1, temp2)
    tempChange = temp2-temp3
    tempco = tempChange/tempDiff

    res1 = randint(5,25)
    res2 = randint(30,55)
    resDiff = res2-res1
    res3 = randint(res1, res2)
    resChange = res2 - res3
    resco = resChange/resDiff
    answer1 = round(res2 - (resDiff*tempco), 2)
    answer2 = round(temp2 - (tempDiff*resco), 2)

    q.questionBase = f"The resistance of a wire increased from {res1} to {res2} \u03A9 as the temperature increased from {temp1} to {temp2} \u00B0 C. Assuming that resistance varies linearly with temperature over this range, calculate:"
    question1 = f"The resistance when temperature is {temp3} \u00B0 C"
    answer1 = f"{answer1} \u03A9"
    question2 = f"The temperature at which resistance will be {res3} \u03A9"
    answer2 = f'{answer2} \u00B0 C'
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': question1, 'sub_answer': answer1, 'sub_mark': 2}, 
       {'sub_number': 2, 'sub_question': question2, 'sub_answer': answer2, 'sub_mark': 2}, 
    ]
    return q.returnAll()
