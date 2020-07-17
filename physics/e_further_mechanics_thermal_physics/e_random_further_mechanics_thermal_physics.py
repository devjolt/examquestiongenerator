from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal
import math

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[22:]  #all modules not to be used for views kept at the front of the file are not added to the usable list. Usually 14
    return usableModuleList

def moduleListGen(qtype = None, low = 0, high = None): 
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key)
    if qtype == None: return entireModuleList[low:high] # use qtype = None to use low high to select slice of list returned in relation to total modules in THIS file, low = -1 for last module only
    else:
        poop = []
        for thing in entireModuleList:
            if str(thing)[low:high] == qtype: # use qtype ='anystring', low = int representing start of string, high = int representing end of string for modules selected by name
                poop.append(thing)
        return poop

def previousNext(place):
    myList = moduleList()
    current = myList[place]
    try:
        next_q = myList[place+1]
    except IndexError:
        next_q = myList[0]
    try:
        previous_q = myList[place-1]
    except IndexError:
        previous_q = myList[-1]
    return f"/gcsemaths/number/{previous_q}", f"/gcsemaths/number/{next_q}"

#allArguments makes it less messy to return dictionary values to templates
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None, question4=None, answer4=None, marks4=None, pre=None, preans = None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            'question4':question4, 'answer4': answer4, 'marks4':marks4,
            'pre':pre, 'preans':preans
            }

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random(request):
    modList = moduleList()
    selection = randint(0,len(modList)-1)
    print(selection)
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = eval(f"{modList[selection]}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def e1_uniform_circular_motion_random(request):
    modList = moduleListGen("e1q", 0, 3)
    selection = randint(0,len(modList)-1)
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = eval(f"{modList[selection]}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

def e2_centripetal_acceleration_random(request):
    modList = moduleListGen("e2q", 0, 3)
    selection = randint(0,len(modList)-1)
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = eval(f"{modList[selection]}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

def e3_on_the_road_random(request):
    modList = moduleListGen("e3q", 0, 3)
    selection = randint(0,len(modList)-1)
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = eval(f"{modList[selection]}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))

def e4_at_the_fairground_random(request):
    modList = moduleListGen("e4q", 0, 3)
    selection = randint(0,len(modList)-1)
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans  = eval(f"{modList[selection]}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, question1, answer1, marks1,  question2, answer2, marks2,  question3, answer3, marks3,  question4, answer4, marks4, pre, preans ))


def posNeg(num):
    selection = randint(0,1)
    if selection == 0:
        num *=-1
    return num

def circleStuffSetup():
    pi = 3.1415826535898
    oneRad = 57.3
    radius = randint(2,99)
    bigT = round(randint(10,1000)/1000,2)
    time = randint(1,10)
    circumference = 2 * pi * radius
    freq = round(1  / bigT, 2)
    speedOfPoint = circumference / time
    angDis = (2*pi*time)/bigT
    angSpe = angDis/time
    return pi, oneRad, radius, circumference, bigT, time, freq, speedOfPoint, round(angDis, 2), angSpe

def e2CentAcSetup():
    pi = 3.1415826535898
    time = randint(1,10)
    radius = randint(2,99)
    mass = randint(1, 99)
    circumference = 2 * pi * radius
    speedOfPoint = circumference / time
    centAc = (speedOfPoint ** 2) / radius
    centForce = (mass *speedOfPoint ** 2) / radius
    wheels = ("model of the London Eye", "rather unusual bicycle wheel", "dangerously inappropriate astonaut training centrifuge", "spinny thing")
    return time, radius, mass, circumference, round(speedOfPoint, 2), round(centAc, 2), round(centForce, 2), str(wheels[randint(0,len(wheels)-1)])

def e3roadSetup():
    pi = 3.1415926535898
    mass = randint(500, 4000)
    gravity = 9.8
    velocity = randint(5, 25)
    radius = randint(20, 100)
    circumference = 2 * pi * radius
    centAc = (velocity ** 2) / radius
    centForce = (mass *velocity ** 2) / radius
    return mass, gravity, velocity, radius, circumference, round(centAc, 2), round(centForce, 2)

def e4fairgroundSetup():
    pi = 3.1415826535898
    gravity = 9.8
    mass = randint(300, 800)/gravity
    radius =  randint(10,50)
    height = randint(5, 30)
    time = randint(10, 20)
    circumference = 2 * pi * radius
    speedOfPoint = circumference / time
    velocity = ((mass * gravity * height)/0.5/mass)**0.5
    centAc = (velocity ** 2) / radius
    centForce = (mass *velocity ** 2) / radius
    support =  mass * gravity + (mass * velocity **2)/ radius
    extraSupport = (mass * velocity **2) / radius
    reaction = ((mass*velocity**2)/radius) - mass * gravity
    return gravity, round(mass, 2), radius, height, time, circumference, round(speedOfPoint,2), round(velocity, 2), round(centAc,2), centForce, support, round(extraSupport,2), reaction

def planetsGen():#name, time for rotation(hours), radius(km)
    planets = (("The Earth", 24, 6400),("Mars", 24,3389.5),("Jupiter", 10, 69911),("Uranus", 17,25362),("Endor", 18, 5200),("Corusant", 24, 8854),("Naboo", 26, 6060 ) , ("Planet Zerg", randint(3,30), randint(3, 10000)))
    return planets[randint(0,len(planets)-1)]

def objectGen():
    objects = ("large Easter Island head","wallet belonging to Elon Musk","well respected Kebab van","brick from Donald Trump's wall", "cosmic llama", "piece of pure adamantium", "confused whale", "brave goosberry bush", "beginner's French dictionary", "lock of Borris Johnson's wonderfully blonde hair", "small asteroid about to be blown up by Bruce Willis",  "spy satellite", "cube of space garbage", "superhero", "supervillain", "blue police phone box", "strawberry cheesecake", "small angry potato", "space cabbage", "Volvo estate")
    return objects[randint(0,len(objects)-1)]

def adverbGen():
    adverbs = ("a bizzarely", "an interestingly", "a uniquely", "a curiously", "an innapropriately", "an unprecedentedly", "a strangely", "an attractively")
    return adverbs[randint(0,len(adverbs)-1)]

def adjectiveGen():
    adjectives = ("liberal", "conservative", "highly environmentally aware", "morally defficient", "euro-skeptic", "left-wing", "dubious", "passionate", "progressive", "highly adventurous", "slightly innaproprate", "macho", "slightly effeminate", "short-sighted", "genetically engineered")
    return adjectives[randint(0,len(adjectives)-1)]

def vehicleGen():
    vehicle = ("decrepit soviet tank", "giant dalek", "large skateboard", "military grade segway", "highly modified Ford Fiesta", "souped up Volvo estate", "rocket powered Micra", "golf cart belonging to Donald Trump", "Humvee belonging to Greta Thunberg", "solar powered tractor", "tesla tank", "Batmobile Delux", "My Little Pony carnival float", "chariot being pulled by psychodelic unicorn monkeys", "radio controlled Narwhal")
    return vehicle[randint(0,len(vehicle)-1)]

def humpGen():
    hump = ("bridge", "hump back bridge", "speed bump", "sleeping police-man", "suspension-wrecking traffic-calming measure", "teletubby dwelling", "robust mole-hill", "hobbit dwelling", "VW Beetle sculture", "piece of modern art resembling Jeremy Corbyn")
    return hump[randint(0,len(hump)-1)]
    
    #Stop counting here
def e1qa_minute_hand_of_clock():
    pi = 3.1415826535898
    questionBase = "Calculate the angular displacement in radians of the tip of the minute hand of a clock in:"
    seconds, minutes, hours = randint(1,60),randint(1,60), randint(1,24)
    question1,question2, question3 = f"{seconds} seconds", f"{minutes} minutes", f"{hours} hours"
    answer1 = f"{round((2*pi*1*seconds)/(3600), 3)} radians"
    answer2 = f"{round((2*pi*60*minutes)/(3600), 3)} radians"
    answer3 = f"{round((2*pi*3600*hours)/(3600), 3)} radians"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2,  question3, answer3,2, None, None, None, None, None

def e1qb_time_pweriod_angle_electric_motor():
    pi, oneRad, radius, cir, bigT, time, freq, speedOfPoint, angDis, angSpe = circleStuffSetup()
    questionBase = f"An electric motor turns at a frequency of {freq}Hz. Calculate:"
    question1 = "its time period"
    question2 = f"the angle it turns through in radians in {time} seconds."
    answer1 = f"{bigT} seconds"
    answer2 = f"{angDis} radians"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 1,  question2, answer2,2,  None, None,None, None, None, None, None, None

def e1qc_planet_rotation():
    planet = planetsGen()
    time = randint(1,10)
    #speed of rotation v=2pir/T
    speed = round((2 * 3.1415926535898 * (planet[2] *1000))/(planet[1]*60*60), 2)
    #angular (2*pi*time)/T
    angDis = round((2 * 3.1415926535898 * time)/(planet[1]*60*60), 6)
    angDisDeg = round(angDis*57.3, 7)
    questionBase = f"{planet[0]} takes exactly {planet[1]} h for one full rotation and has a radius of {planet[2]} km. Calculate:"
    question1 = "the speed of rotation at a point on the equator"
    question2 = f"the angle {planet[0]} turns through in {time}s in degrees."
    question3 = f"the angle {planet[0]} turns through in {time}s in radians."
    answer1 = f"{speed} m/s"
    answer2 = f"{angDisDeg} degrees"
    answer3 = f"{angDis} radians"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 1,  question2, answer2,2,  question3, answer3,2, None, None, None, None, None

def e1qd_satalite_orbit():
    planet, thing = planetsGen(), objectGen()
    time = randint(1,10)
    timeOrbit = randint(10,300)
    orbit = randint(20, 2000)
    #speed of rotation v=2pir/T
    speed = round((2 * 3.1415926535898 * ((planet[2]+orbit)*1000)) / (timeOrbit*60), 2)
    #angular (2*pi*time)/T
    angDis = round((2 * 3.1415926535898 * time) / (timeOrbit*60), 6)
    angDisDeg = round(angDis*57.3, 7)
    questionBase = f"A {thing} orbits {orbit} km above the surface of {planet[0]}, which has a radius of {planet[2]} km. It takes {timeOrbit} minutes per obit. Calculate:"
    question1 = f"the speed of the {thing}"
    question2 = f"the {thing}'s angular displacement in {time} s in degrees."
    question3 = f"the {thing}'s angular displacement in {time} s in radians."
    answer1 = f"{speed} m/s"
    answer2 = f"{angDisDeg} degrees"
    answer3 = f"{angDis} radians"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 1,  question2, answer2,2,  question3, answer3,2, None, None, None, None, None

def e2qa_the_wheel_of():
    time, radius, mass, circumference, speedOfPoint, centAc, centForce, wheel = e2CentAcSetup()
    thing = objectGen()
    questionBase = f"A {wheel} has a diameter of {radius *2}m and takes {time}s to make a full rotation. Calculate"
    question1 = f"the speed of a {thing} were it to be theoretically duct-taped to the {wheel}"
    question2 = f"the centripetal acceleration of the {thing}"
    question3 = f"the centripetal force of the {thing} if it had a mass of {mass}kg."
    answer1 = f"{speedOfPoint}m/s"
    answer2 = f"{centAc}m/s²"
    answer3 = f"{centForce}N"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 1,  question2, answer2,2,  question3, answer3,2, None, None, None, None, None

def e2qb_object_circular_path():
    time, radius, mass, circumference, speedOfPoint, centAc, centForce, wheel = e2CentAcSetup()
    thing = objectGen()
    questionBase = f"A {thing} with a mass of {mass} kg moves around {adverbGen()} circular path of radius {radius}m at {adverbGen()} steady rate once every {time}s. Calculate:"
    question1 = f"the speed and acceleration of the {thing}"
    question2 = f"the centripetal force on the the {thing}"
    answer1 = f"{speedOfPoint} m/s, {centAc} m/s²"
    answer2 = f"{centForce} N"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2, None, None, None, None, None, None, None, None

def e2qc_earth_around_sun():
    planets = (("Mercury", 36800000, 90), ("Venus", 67200000, 210), ("The Earth", 93_000_000, 365.25), ("Mars", 141_600_000, 690), ("Jupiter", 483_600_000, 7320), ("Saturn", 886_500_000, 10620),("Uranus", 1_783_700_000, 30270),("Neptune", 2_795_200_000, 59370), ("Pluto", 3_670_100_000, 89310))
    choice = randint(0, len(planets)-1)
    planet = planets[choice][0]
    radMiles = planets[choice][1]
    pi = 3.1415826535898
    time = planets[choice][2]*24*60*60
    radius = radMiles * 1609
    circumference = 2 * pi * radius
    speedOfPoint = circumference / time
    centAc = round((speedOfPoint ** 2) / radius, 9)

    questionBase = f"{planet} moves around the sun on a roughly circular orbit of radius {radMiles} miles, taking {planets[choice][2]} days for each complete orbit. Assuming that 1 mile = 1609m, calculate:"
    question1 = f"the speed of {planet} in m/s"
    question2 = f"the centripetal acceleration of {planet} on its orbit around the Sun in m/s²."
    answer1 = f"{round(speedOfPoint, 2)} m/s"
    answer2 = f"{centAc} m/s²"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2, None, None, None, None, None, None, None, None

def e2qd_hammer_thrower():
    pi = 3.1415826535898
    time = randint(1,10)/10
    radius = randint(5,30)/10
    mass = randint(1, 10)
    circumference = 2 * pi * radius
    speedOfPoint = circumference / time
    centAc = (speedOfPoint ** 2) / radius
    centForce = (mass *speedOfPoint ** 2) / radius
    thing = objectGen()
    released = ("released", "hurled into oblivion", "splatted against a wall", "launched at a low flying pidgeon", "thrown into a crowd of unfortunate joggers", "eaten by Thanos")
    questionBase = f"A {adjectiveGen()} hammer thrower spins a {mass} kg {thing} round on the end of a rope in a circle of radius {radius} m. The {thing} took {time} s to make one full rotation just before it was {released[randint(0, len(released)-1)]}. Calculate: "
    question1 = f"the speed of the {thing} just before it was released"
    question2 = f"its centripetal acceleration"
    question3 = f"the centripetal force on the {thing} just before release."
    answer1 = f"{round(speedOfPoint, 2)} m/s"
    answer2 = f"{round(centAc, 2)} m/s²"
    answer3 = f"{round(centForce, 2)} N"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2, question3, answer3, 3, None, None, None, None, None

def e3qa_bridge():
    mass, gravity, velocity, radius, circumference, centAc, centForce = e3roadSetup()
    support = round(((mass * velocity ** 2) / radius) -(mass * gravity), 2)*-1
    hump, vehicle = humpGen(), vehicleGen()
    questionBase = f"A {vehicle} of mass {mass} kg passes over a {hump} of radius of curvature {radius} m  at a speed of {velocity} m/s. Calculate:"
    question1 = f"the centripetal acceleration of the {vehicle} on the bridge"
    question2 = f"the support force on the {vehicle} when it was at the top."
    answer1 = f"{centAc} m/s²"
    answer2 = f"{support} N"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2, None, None, None, None, None, None, None, None

def e3qb_roundabout():
    mass, gravity, velocity, radius, circumference, centAc, centForce = e3roadSetup()
    vehicle = vehicleGen()
    questionBase = f"The maximum speed for no skidding of a {vehicle} of mass {mass} kg on a roundabout of radius {radius} m is {velocity} m/s. Calculate:"
    question1 = f"the centripetal acceleration at this point"
    question2 = f"the centripetal force on the vehicle when moving at this speed"
    question3 = f"the friction coefficient in this scenario."
    answer1 = f"{centAc} m/s²"
    answer2 = f"{centForce} N"
    answer3 = f"{round((velocity**2)/(gravity*radius), 4)}"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2, question3, answer3, 3, None, None, None, None, None

def e3qc_racingtrack():
    mass, gravity, velocity, radius, circumference, centAc, centForce = e3roadSetup()
    angle = randint(10, 30)
    velocity = round((gravity * radius * math.tan(angle/57.2958))**0.5, 2)
    questionBase = f"At a racing snail circuit, the track is banked at an angle of {angle}° to the horizontal on a bend that has a radius of curvature of {radius} m. Use the equation v² =grtan\u03B8 to calculate the speed of a vehicle on the bend if there is to be no sideways friction."
    answer = f"{velocity}m/s"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, answer, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None
    
def e4qa_rollercoaster():
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = e4fairgroundSetup()
    name = ("Trump's Wall", "Corbyn's Gulag Line", "Brexit Express", "The Smasher")
    questionBase = f"A train on a ride named {name[randint(0, len(name)-1)]} is initially stationary before it descends through a height of {height} m into a dip that has a radius of curvature of {radius} m."
    question1 = f"Calculate the speed of the train at the bottom of the dip, assuming air resistance and friction don't exist because this is physics"
    question2 = f"Calculate the centripetal acceleration at the bottom of the dip"
    question3 = f"Calcuate the extra support force on a person of weight {round(mass*9.8, 2)} N assuming that g is 9.8m/s²"
    answer1 = f"{velocity} m/s"
    answer2 = f"{centAc} m/s²"
    answer3 = f"{extraSupport} N"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2, question3, answer3, 3, None, None, None, None, None
    
def e4qb_swing():
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = e4fairgroundSetup()
    velocity = round(((mass * gravity * height)/0.5/mass)**0.5, 2)
    centAc = (velocity ** 2) / height
    extraSupprt = (2 * mass * gravity * height) / height
    name = ("Trump's Beautiful Wall World", "Corbyn's Soviet Dreamworld", "Boris' Brexitland", "Greta's Dare Park", "Merkl's Magical Happy Euroland", "Assad's No Nulcear Activity Here Land")
    questionBase = f"An innapropriately named swing at {name[randint(0, len(name)-1)]} is {height} m in length. A pleb of mass {mass} kg descends from a position where the swing is horizontal. Calculate:"
    question1 = f"the speed of the pleb at the lowest point, assuming air resistance and friction don't exist because science,"
    question2 = f"the centripetal acceleration at the bottom of the dip,"
    question3 = f"the extra support force on a person at the lowest point."
    answer1 = f"{velocity} m/s"
    answer2 = f"{centAc} m/s²"
    answer3 = f"{extraSupport} N"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2, question3, answer3, 3, None, None, None, None, None

def e4qc_wheel():
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = e4fairgroundSetup()
    centAc = round((speedOfPoint ** 2) / radius, 2)
    extraSupport = round(((mass * speedOfPoint ** 2) / radius) - mass * gravity, 2)
    name = ("Trump's Beautiful Wall World", "Corbyn's Soviet Dreamworld", "Boris' Brexitland", "Greta's Dare Park", "Merkl's Magical Happy Euroland", "Assad's No Nulcear Activity Here Land")
    questionBase = f"The 'Big Wheel' at {name[randint(0, len(name)-1)]} has a radius of {radius} m and rotates once every {time} seconds. Calculate:"
    question1 = f"the speed of rotation of the perimeter of the wheel,"
    question2 = f"the centripetal acceleration of a person at the perimeter,"
    question3 = f"the support force on a person  of mass {mass} kg at the highest point."
    answer1 = f"{speedOfPoint} m/s"
    answer2 = f"{centAc} m/s²"
    answer3 = f"{extraSupport} N"
    previousQ, nextQ, diagram, constant = None, None, None, None
    return previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2,  question2, answer2,2, question3, answer3, 3, None, None, None, None, None

