from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal
import math
import sys

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

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

def previousNext(qtype = None, low = 0, high = None, name=''):
    modList = moduleListGen(qtype, low, high)
    modDict = {}
    count = -1
    for thing in modList:
        count+=1
        modDict.update({str(thing):count})
    place = modDict[name]
    current = modList[place]
    try:
        next_q = modList[place+1]
    except IndexError:
        next_q = modList[0]
    try:
        previous_q = modList[place-1]
    except IndexError:
        previous_q = modList[-1]
    return f"/physics/further_mechanics_and_thermal_physics/{previous_q}", f"/physics/further_mechanics_and_thermal_physics/{next_q}"


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

def centAcSetup():
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

def roadSetup():
    pi = 3.1415926535898
    mass = randint(500, 4000)
    gravity = 9.8
    velocity = randint(5, 25)
    radius = randint(20, 100)
    circumference = 2 * pi * radius
    centAc = (velocity ** 2) / radius
    centForce = (mass *velocity ** 2) / radius
    return mass, gravity, velocity, radius, circumference, round(centAc, 2), round(centForce, 2)

def fairgroundSetup():
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

def clockPicGen():
    thing = ["https://i.imgflip.com/rkiba.jpg", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.makeameme.org%2Fcreated%2Fi-keep-watching-w1rr4y.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages3.memedroid.com%2Fimages%2FUPLOADED493%2F5ab290be65f63.jpeg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2F1it0g5.jpg&f=1&nofb=1"]
    return thing[randint(0,len(thing)-1)]

def motorPicGen():
    thing = ["https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.techtransfer.com%2Fwp-content%2Fuploads%2FACMotor-1024x789.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.ebayimg.com%2Fimages%2Fi%2F252051937719-0-1%2Fs-l1000.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FSmvEQftcGkk%2Fmaxresdefault.jpg&f=1&nofb=1"]
    return thing[randint(0,len(thing)-1)]

def planetPicGen():
    thing = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstupidbadmemes.files.wordpress.com%2F2013%2F09%2Fpluto-not-a-planet.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2F1ctny7.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.buzzfeed.com%2Fbuzzfeed-static%2Fstatic%2F2015-10%2F28%2F11%2Fcampaign_images%2Fwebdr10%2Fthe-sad-pluto-meme-is-making-the-internet-weep-2-17072-1446047759-0_dblbig.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpbs.twimg.com%2Ftweet_video_thumb%2FCJ59P0TVAAAi4fe.png&f=1&nofb=1"]
    return thing[randint(0,len(thing)-1)]

def satelitePicGen():
    thing = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages7.memedroid.com%2Fimages%2FUPLOADED154%2F5549b3a53d37e.jpeg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs3.amazonaws.com%2Fs3.timetoast.com%2Fpublic%2Fuploads%2Fphotos%2F5537921%2FSputnik_Meme.jpg%3F1476951033&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.memecdn.com%2Fsatellite_o_63768.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2F13gh9e.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Forbitingfrog.files.wordpress.com%2F2014%2F01%2F20140205-norway-earths-orbit-002.jpg&f=1&nofb=1"]
    return thing[randint(0,len(thing)-1)]

def wheelPicGen():
    thing = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.memecdn.com%2Fscumbag-wheel_o_777651.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.memecdn.com%2Fyoshi-steering-wheel-you-get-sucked-in-and-your-ability-gets-stolen_c_3776709.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2F28rbdf.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2F1ysj3o.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcraziestgadgets.com%2Fwp-content%2Fuploads%2F2013%2F08%2Fadult-big-wheels.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fbd%2Fce%2F31%2Fbdce314737376f00efdc06f2fcd34d6d.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.lovequotesmessages.com%2Fwp-content%2Fuploads%2F2018%2F04%2Fwheel_can_encouraging_meme1.jpg&f=1&nofb=1"]
    return thing[randint(0,len(thing)-1)]

def hammerPicGen():
    thing = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.memecdn.com%2Fscumbag-wheel_o_777651.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.memecdn.com%2Fyoshi-steering-wheel-you-get-sucked-in-and-your-ability-gets-stolen_c_3776709.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2F28rbdf.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2F1ysj3o.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcraziestgadgets.com%2Fwp-content%2Fuploads%2F2013%2F08%2Fadult-big-wheels.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fbd%2Fce%2F31%2Fbdce314737376f00efdc06f2fcd34d6d.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.lovequotesmessages.com%2Fwp-content%2Fuploads%2F2018%2F04%2Fwheel_can_encouraging_meme1.jpg&f=1&nofb=1"]
    return thing[randint(0,len(thing)-1)]

#values in the return tuple for each modules HAVE to be in this order: (code from allArguments2 in examquestiongenerator.helperfunctions) 
# template_strings= ["previousQ", "nextQ", "diagram", "constant", "questionBase", "answer", "pre", "preans", "marks", "level", "tip", "video", "website", "piclink", "question1", "answer1", "marks1", "question2", "answer2", "marks2", "question3", "answer3", "marks3", "question4", "answer4", "marks4"] 

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def select_random():
    modList = moduleListGen("e", 0,1) # all other modules start with e, which is useful (including other random modules, which I'm not 100 happy about, but there you go!)
    selection = randint(0,len(modList)-1)
    template_fodder = eval(f"{modList[selection]}()")
    return template_fodder

#selects a view function at random from moduleList generated list and returns everything needed to generate a view
def e1_uniform_circular_motion_random():
    modList = moduleListGen("e1q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def e2_centripetal_acceleration_random():
    modList = moduleListGen("e2q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def e3_on_the_road_random():
    modList = moduleListGen("e3q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def e4_at_the_fairground_random():
    modList = moduleListGen("e4q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

# Individual question logic starts here
def e1qa_minute_hand_of_clock():
    pi = 3.1415926535898
    questionBase = "Calculate the angular displacement in radians of the tip of the minute hand of a clock in:"
    seconds, minutes, hours = randint(1,60),randint(1,60), randint(1,24)
    q1,q2, q3 = f"{seconds} seconds", f"{minutes} minutes", f"{hours} hours"
    a1 = f"{round((2*pi*1*seconds)/(3600), 3)} radians"
    a2 = f"{round((2*pi*60*minutes)/(3600), 3)} radians"
    a3 = f"{round((2*pi*3600*hours)/(3600), 3)} radians"
    m1, m2, m3 = 1, 1, 1
    previousQ, nextQ = previousNext("e1q", 0, 3, currentFuncName())
    diagram, constant = None, "\u03c0 = 3.1415926535898"
    answer, marks = None, None
    pre, preans, level = None, None, None
    tip = "Angular displacement (radians) = 2\u03c0t/T = 2\u03c0ft, where T = time taken for one rotation, f = frequency (= 1/T) and t = time taken for displacement."
    video, website = None, None
    piclink = clockPicGen()
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2,q3,a3,m3)

def e1qb_time_pweriod_angle_electric_motor():
    pi, oneRad, radius, cir, bigT, time, freq, speedOfPoint, angDis, angSpe = circleStuffSetup()
    questionBase = f"An electric motor turns at a frequency of {freq}Hz. Calculate:"
    q1 = "its time period"
    q2 = f"the angle it turns through in radians in {time} seconds."
    a1 = f"{bigT} seconds"
    a2 = f"{angDis} radians"
    m1, m2, m3 = 1, 1, 1
    previousQ, nextQ = previousNext("e1q", 0, 3, currentFuncName())
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = "Angle turned though (radians) = 2\u03c0/T and Angular displacement (radians) = 2\u03c0t/T = 2\u03c0ftS, where T = time taken for one rotation, f = frequency (= 1/T) and t = time taken for displacement."
    video, website = None, None
    piclink = motorPicGen()
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2)

def e1qc_planet_rotation():
    planet = planetsGen()
    time = randint(1,10)
    #speed of rotation v=2pir/T
    speed = round((2 * 3.1415926535898 * (planet[2] *1000))/(planet[1]*60*60), 2)
    #angular (2*pi*time)/T
    angDis = round((2 * 3.1415926535898 * time)/(planet[1]*60*60), 6)
    angDisDeg = round(angDis*57.3, 7)
    questionBase = f"{planet[0]} takes exactly {planet[1]} h for one full rotation and has a radius of {planet[2]} km. The diagram above does not show this planet. Calculate:"
    q1 = "the speed of rotation at a point on the equator in m/s"
    q2 = f"the angle {planet[0]} turns through in {time}s in degrees."
    q3 = f"the angle {planet[0]} turns through in {time}s in radians."
    a1 = f"{speed} m/s"
    a2 = f"{angDisDeg} degrees"
    a3 = f"{angDis} radians"
    m1, m2, m3 = 1, 2, 2
    previousQ, nextQ = previousNext("e1q", 0, 3, currentFuncName())
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = "speed of rotation = 2\u03c0r/T, Angle turned though (radians) = 2\u03c0/T, Angular displacement (radians) = 2\u03c0t/T = 2\u03c0ftS, where T = time taken for one rotation, f = frequency (= 1/T) and t = time taken for displacement."
    video, website = None, None
    piclink = planetPicGen()
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2,q3,a3,m3)

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
    questionBase = f"A {thing} orbits {orbit} km above the surface of {planet[0]} (the diagram above is not accurate in any way), which has a radius of {planet[2]} km. It takes {timeOrbit} minutes per obit. Calculate:"
    q1 = f"the speed of the {thing}"
    q2 = f"the {thing}'s angular displacement in {time} s in degrees."
    q3 = f"the {thing}'s angular displacement in {time} s in radians."
    a1 = f"{speed} m/s"
    a2 = f"{angDisDeg} degrees"
    a3 = f"{angDis} radians"
    m1, m2, m3 = 1, 2, 2
    previousQ, nextQ = previousNext("e1q", 0, 3, currentFuncName())
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = satelitePicGen()
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2,q3,a3,m3)

def e2qa_the_wheel_of():
    time, radius, mass, circumference, speedOfPoint, centAc, centForce, wheel = centAcSetup()
    thing = objectGen()
    questionBase = f"A {wheel} (not pictured above) has a diameter of {radius *2}m and takes {time}s to make a full rotation. Calculate"
    q1 = f"the speed of a {thing} were it to be theoretically duct-taped to the {wheel}"
    q2 = f"the centripetal acceleration of the {thing}"
    q3 = f"the centripetal force of the {thing} if it had a mass of {mass}kg."
    a1 = f"{speedOfPoint}m/s"
    a2 = f"{centAc}m/s²"
    a3 = f"{centForce}N"
    m1, m2, m3 = 1, 2, 2
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = wheelPicGen()
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2,q3,a3,m3)

def e2qb_object_circular_path():
    time, radius, mass, circumference, speedOfPoint, centAc, centForce, wheel = centAcSetup()
    thing = objectGen()
    questionBase = f"A {thing} (not pictured above) with a mass of {mass} kg moves around {adverbGen()} circular path of radius {radius}m at {adverbGen()} steady rate once every {time}s. Calculate:"
    q1 = f"the speed and acceleration of the {thing}"
    q2 = f"the centripetal force on the the {thing}"
    a1 = f"{speedOfPoint} m/s, {centAc} m/s²"
    a2 = f"{centForce} N"
    m1, m2 = 1, 2
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = wheelPicGen()
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2)

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
    q1 = f"the speed of {planet} in m/s"
    q2 = f"the centripetal acceleration of {planet} on its orbit around the Sun in m/s²."
    a1 = f"{round(speedOfPoint, 2)} m/s"
    a2 = f"{centAc} m/s²"
    m1, m2 = 1, 2
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = None
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2)

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
    q1 = f"the speed of the {thing} just before it was released"
    q2 = f"its centripetal acceleration"
    q3 = f"the centripetal force on the {thing} just before release."
    a1 = f"{round(speedOfPoint, 2)} m/s"
    a2 = f"{round(centAc, 2)} m/s²"
    a3 = f"{round(centForce, 2)} N"
    m1, m2, m3 = 1, 2, 2
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = None
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2,q3,a3,m3)

def e3qa_bridge():
    mass, gravity, velocity, radius, circumference, centAc, centForce = roadSetup()
    support = round(((mass * velocity ** 2) / radius) -(mass * gravity), 2)*-1
    hump, vehicle = humpGen(), vehicleGen()
    questionBase = f"A {vehicle} of mass {mass} kg passes over a {hump} of radius of curvature {radius} m  at a speed of {velocity} m/s. Calculate:"
    q1 = f"the centripetal acceleration of the {vehicle} on the bridge"
    q2 = f"the support force on the {vehicle} when it was at the top."
    a1 = f"{centAc} m/s²"
    a2 = f"{support} N"
    diagram, constant, answer, marks = None, None, None, None
    m1, m2 = 2, 2
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = None
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2)

def e3qb_roundabout():
    mass, gravity, velocity, radius, circumference, centAc, centForce = roadSetup()
    vehicle = vehicleGen()
    questionBase = f"The maximum speed for no skidding of a {vehicle} of mass {mass} kg on a roundabout of radius {radius} m is {velocity} m/s. Calculate:"
    q1 = f"the centripetal acceleration at this point"
    q2 = f"the centripetal force on the vehicle when moving at this speed"
    q3 = f"the friction coefficient in this scenario."
    a1 = f"{centAc} m/s²"
    a2 = f"{centForce} N"
    a3 = f"{round((velocity**2)/(gravity*radius), 4)}"
    m1, m2, m3 = 2, 2, 3
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = None
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2)

def e3qc_racingtrack():
    mass, gravity, velocity, radius, circumference, centAc, centForce = roadSetup()
    angle = randint(10, 30)
    velocity = round((gravity * radius * math.tan(angle/57.2958))**0.5, 2)
    questionBase = f"At a racing snail circuit, the track is banked at an angle of {angle}° to the horizontal on a bend that has a radius of curvature of {radius} m. Use the equation v² =grtan\u03B8 to calculate the speed of a vehicle on the bend if there is to be no sideways friction."
    answer = f"{velocity}m/s"
    marks = 2
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer = None, "\u03c0 = 3.1415926535898", None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = None
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink)

def e4qa_rollercoaster():
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = fairgroundSetup()
    name = ("Trump's Wall", "Corbyn's Gulag Line", "Brexit Express", "The Smasher")
    questionBase = f"A train on a ride named {name[randint(0, len(name)-1)]} is initially stationary before it descends through a height of {height} m into a dip that has a radius of curvature of {radius} m."
    q1 = f"Calculate the speed of the train at the bottom of the dip, assuming air resistance and friction don't exist because this is physics"
    q2 = f"Calculate the centripetal acceleration at the bottom of the dip"
    q3 = f"Calcuate the extra support force on a person of weight {round(mass*9.8, 2)} N assuming that g is 9.8m/s²"
    a1 = f"{velocity} m/s"
    a2 = f"{centAc} m/s²"
    a3 = f"{extraSupport} N"
    m1, m2, m3 = 2, 2, 3
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = None
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2,q3,a3,m3)

def e4qb_swing():
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = fairgroundSetup()
    velocity = round(((mass * gravity * height)/0.5/mass)**0.5, 2)
    centAc = (velocity ** 2) / height
    extraSupprt = (2 * mass * gravity * height) / height
    name = ("Trump's Beautiful Wall World", "Corbyn's Soviet Dreamworld", "Boris' Brexitland", "Greta's Dare Park", "Merkl's Magical Happy Euroland", "Assad's No Nulcear Activity Here Land")
    questionBase = f"An innapropriately named swing at {name[randint(0, len(name)-1)]} is {height} m in length. A pleb of mass {mass} kg descends from a position where the swing is horizontal. Calculate:"
    q1 = f"the speed of the pleb at the lowest point, assuming air resistance and friction don't exist because science,"
    q2 = f"the centripetal acceleration at the bottom of the dip,"
    q3 = f"the extra support force on a person at the lowest point."
    a1 = f"{velocity} m/s"
    a2 = f"{centAc} m/s²"
    a3 = f"{extraSupport} N"
    m1, m2, m3 = 2, 2, 3
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = None
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2,q3,a3,m3)

def e4qc_wheel():
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = fairgroundSetup()
    centAc = round((speedOfPoint ** 2) / radius, 2)
    extraSupport = round(((mass * speedOfPoint ** 2) / radius) - mass * gravity, 2)
    name = ("Trump's Beautiful Wall World", "Corbyn's Soviet Dreamworld", "Boris' Brexitland", "Greta's Dare Park", "Merkl's Magical Happy Euroland", "Assad's No Nulcear Activity Here Land")
    questionBase = f"The 'Big Wheel' at {name[randint(0, len(name)-1)]} has a radius of {radius} m and rotates once every {time} seconds. Calculate:"
    q1 = f"the speed of rotation of the perimeter of the wheel,"
    q2 = f"the centripetal acceleration of a person at the perimeter,"
    q3 = f"the support force on a person  of mass {mass} kg at the highest point."
    a1 = f"{speedOfPoint} m/s"
    a2 = f"{centAc} m/s²"
    a3 = f"{extraSupport} N"
    m1, m2, m3 = 2, 2, 3
    name = currentFuncName()
    previousQ, nextQ = previousNext(name[:3], 0, 3, name)
    diagram, constant, answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    pre, preans, level = None, None, None
    tip = None
    video, website = None, None
    piclink = None
    return (previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video, website, piclink, q1,a1,m1,q2,a2,m2,q3,a3,m3)

#selects 15 marks worth of questions and returns it!
def section_generator():
    func_list = moduleListGen("e", 0, 1)

    section_marks = 0
    returned_list = []

    while section_marks < 15:
        selection = randint(0, len(func_list)-1)
        returned_things = eval(f"{func_list[selection]}()")
        print(func_list[selection])

        if len(returned_things) == 23:
            question_marks = returned_things[-1] + returned_things[-4] + returned_things[-7]
            print("3qus")
        elif len(returned_things) == 20:
            question_marks = returned_things[-1] + returned_things[-4]
            print("2qus")
        elif len(returned_things) <= 14:
            question_marks = returned_things[8]
            print("1qus")

        while question_marks + section_marks > 16:
            selection = randint(0, len(func_list)-1)
            returned_things = eval(f"{func_list[selection]}()")
            print(func_list[selection])

            if len(returned_things) == 23:
                question_marks = returned_things[-1] + returned_things[-4] + returned_things[-7]
            elif len(returned_things) == 20:
                question_marks = returned_things[-1] + returned_things[-4]
            elif len(returned_things) == 14:
                question_marks = returned_things[8]
            
        
        returned_list.append(returned_things)

        section_marks += question_marks
        print(question_marks)

    print(returned_list)
    print(section_marks)
    return returned_list

