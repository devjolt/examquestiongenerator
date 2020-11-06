from django.shortcuts import render
from random import randint, randrange
from random import randint
from fractions import Fraction
from decimal import Decimal
import math
import sys
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
    return ucf.moduleListGen(list_callable_functions(), 'e', 0, 1)

def module_path():
    return '/physics/further_mechanics/'

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
    thing = ['https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimgix.ranker.com%2Fuser_node_img%2F50058%2F1001144758%2Foriginal%2Fd-photo-u1%3Fw%3D650%26q%3D50%26fm%3Dpjpg%26fit%3Dcrop%26crop%3Dfaces&f=1&nofb=1',
         'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimgix.ranker.com%2Fuser_node_img%2F50058%2F1001144740%2Foriginal%2Fd-photo-u1%3Fw%3D1000%26fm%3Djpg%26fit%3Dcrop%26q%3D60&f=1&nofb=1',
         'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fjpegy.com%2Fimages%2Fuploads%2F2012%2F04%2Fepic-meme-clock.jpg&f=1&nofb=1',
         "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.makeameme.org%2Fcreated%2Fi-keep-watching-w1rr4y.jpg&f=1&nofb=1",
         "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages3.memedroid.com%2Fimages%2FUPLOADED493%2F5ab290be65f63.jpeg&f=1&nofb=1",
         "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2F1it0g5.jpg&f=1&nofb=1"]
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
def re1_uniform_circular_motion_random():
    modList = moduleListGen("e1q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def re2_centripetal_acceleration_random():
    modList = moduleListGen("e2q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def re3_on_the_road_random():
    modList = moduleListGen("e3q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def re4_at_the_fairground_random():
    modList = moduleListGen("e4q", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

# Individual question logic starts here
def e1aaa_minute_hand_of_clockpxax3():
    q = ucf.Question(ucf.currentFuncName())
    pi = 3.1415926535898
    q.questionBase = "Calculate the angular displacement in radians of the minute hand of a clock in:"
    seconds, minutes, hours = randint(1,60),randint(1,60), randint(1,24)
    q1,q2, q3 = f"{seconds} seconds", f"{minutes} minutes", f"{hours} hours"
    a1 = f"{round((2*pi*1*seconds)/(3600), 3)} radians"
    a2 = f"{round((2*pi*60*minutes)/(3600), 3)} radians"
    a3 = f"{round((2*pi*3600*hours)/(3600), 3)} radians"
    m1, m2, m3 = 1, 1, 1
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant = None, "\u03c0 = 3.1415926535898"
    q.answer, marks = None, None
    q.hint = "Angular displacement (radians) = 2\u03c0t/T = 2\u03c0ft, where T = time taken for one rotation, f = frequency (= 1/T) and t = time taken for displacement."
    q.video, q.weblink = None, None
    q.piclink = clockPicGen()
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

def e1aab_time_pweriod_angle_electric_motorpaxa3():
    q = ucf.Question(ucf.currentFuncName())
    pi, oneRad, radius, cir, bigT, time, freq, speedOfPoint, angDis, angSpe = circleStuffSetup()
    q.questionBase = f"An electric motor turns at a frequency of {freq}Hz. Calculate:"
    q1 = "its time period"
    q2 = f"the angle it turns through in radians in {time} seconds."
    a1 = f"{bigT} seconds"
    a2 = f"{angDis} radians"
    m1, m2, m3 = 1, 1, 1
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = "Angle turned though (radians) = 2\u03c0/T and Angular displacement (radians) = 2\u03c0t/T = 2\u03c0ftS, where T = time taken for one rotation, f = frequency (= 1/T) and t = time taken for displacement."
    q.video, q.weblink = None, None
    q.piclink = motorPicGen()
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
    ]
    return q.returnAll()

def e1aac_planet_rotationpxax5():
    q = ucf.Question(ucf.currentFuncName())
    planet = planetsGen()
    time = randint(1,10)
    #speed of rotation v=2pir/T
    speed = round((2 * 3.1415926535898 * (planet[2] *1000))/(planet[1]*60*60), 2)
    #angular (2*pi*time)/T
    angDis = round((2 * 3.1415926535898 * time)/(planet[1]*60*60), 6)
    angDisDeg = round(angDis*57.3, 7)
    q.questionBase = f"{planet[0]} takes exactly {planet[1]} h for one full rotation and has a radius of {planet[2]} km. The diagram above does not show this planet. Calculate:"
    q1 = "the speed of rotation at a point on the equator in m/s"
    q2 = f"the angle {planet[0]} turns through in {time}s in degrees."
    q3 = f"the angle {planet[0]} turns through in {time}s in radians."
    a1 = f"{speed} m/s"
    a2 = f"{angDisDeg} degrees"
    a3 = f"{angDis} radians"
    m1, m2, m3 = 1, 2, 2
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = "speed of rotation = 2\u03c0r/T, Angle turned though (radians) = 2\u03c0/T, Angular displacement (radians) = 2\u03c0t/T = 2\u03c0ftS, where T = time taken for one rotation, f = frequency (= 1/T) and t = time taken for displacement."
    q.video, q.weblink = None, None
    q.piclink = planetPicGen()
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

def e1aad_satalite_orbitpxax5():
    q = ucf.Question(ucf.currentFuncName())
    planet, thing = planetsGen(), objectGen()
    time = randint(1,10)
    timeOrbit = randint(10,300)
    orbit = randint(20, 2000)
    #speed of rotation v=2pir/T
    speed = round((2 * 3.1415926535898 * ((planet[2]+orbit)*1000)) / (timeOrbit*60), 2)
    #angular (2*pi*time)/T
    angDis = round((2 * 3.1415926535898 * time) / (timeOrbit*60), 6)
    angDisDeg = round(angDis*57.3, 7)
    q.questionBase = f"A {thing} orbits {orbit} km above the surface of {planet[0]} (the diagram above is not accurate in any way), which has a radius of {planet[2]} km. It takes {timeOrbit} minutes per obit. Calculate:"
    q1 = f"the speed of the {thing}"
    q2 = f"the {thing}'s angular displacement in {time} s in degrees."
    q3 = f"the {thing}'s angular displacement in {time} s in radians."
    a1 = f"{speed} m/s"
    a2 = f"{angDisDeg} degrees"
    a3 = f"{angDis} radians"
    m1, m2, m3 = 1, 2, 2
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = satelitePicGen()
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

def e1aba_the_wheel_ofpxax5():
    q = ucf.Question(ucf.currentFuncName())
    time, radius, mass, circumference, speedOfPoint, centAc, centForce, wheel = centAcSetup()
    thing = objectGen()
    q.questionBase = f"A {wheel} (not pictured above) has a diameter of {radius *2}m and takes {time}s to make a full rotation. Calculate"
    q1 = f"the speed of a {thing} were it to be theoretically duct-taped to the {wheel}"
    q2 = f"the centripetal acceleration of the {thing}"
    q3 = f"the centripetal force of the {thing} if it had a mass of {mass}kg."
    a1 = f"{speedOfPoint}m/s"
    a2 = f"{centAc}m/s²"
    a3 = f"{centForce}N"
    m1, m2, m3 = 1, 2, 2
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = wheelPicGen()
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

def e1abb_object_circular_pathpxax3():
    q = ucf.Question(ucf.currentFuncName())
    time, radius, mass, circumference, speedOfPoint, centAc, centForce, wheel = centAcSetup()
    thing = objectGen()
    q.questionBase = f"A {thing} (not pictured above) with a mass of {mass} kg moves around {adverbGen()} circular path of radius {radius}m at {adverbGen()} steady rate once every {time}s. Calculate:"
    q1 = f"the speed and acceleration of the {thing}"
    q2 = f"the centripetal force on the the {thing}"
    a1 = f"{speedOfPoint} m/s, {centAc} m/s²"
    a2 = f"{centForce} N"
    m1, m2 = 1, 2
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = wheelPicGen()
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
    ]
    return q.returnAll()

def e1abc_earth_around_sun3pxax():
    q = ucf.Question(ucf.currentFuncName())
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
    q.questionBase = f"{planet} moves around the sun on a roughly circular orbit of radius {radMiles} miles, taking {planets[choice][2]} days for each complete orbit. Assuming that 1 mile = 1609m, calculate:"
    q1 = f"the speed of {planet} in m/s"
    q2 = f"the centripetal acceleration of {planet} on its orbit around the Sun in m/s²."
    a1 = f"{round(speedOfPoint, 2)} m/s"
    a2 = f"{centAc} m/s²"
    m1, m2 = 1, 2
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = None
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
    ]
    return q.returnAll()

def e1abd_hammer_throwerpxax5():
    q = ucf.Question(ucf.currentFuncName())
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
    q.questionBase = f"A {adjectiveGen()} hammer thrower spins a {mass} kg {thing} round on the end of a rope in a circle of radius {radius} m. The {thing} took {time} s to make one full rotation just before it was {released[randint(0, len(released)-1)]}. Calculate: "
    q1 = f"the speed of the {thing} just before it was released"
    q2 = f"its centripetal acceleration"
    q3 = f"the centripetal force on the {thing} just before release."
    a1 = f"{round(speedOfPoint, 2)} m/s"
    a2 = f"{round(centAc, 2)} m/s²"
    a3 = f"{round(centForce, 2)} N"
    m1, m2, m3 = 1, 2, 2
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = None
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

def e1aca_bridgepxax4():
    q = ucf.Question(ucf.currentFuncName())
    mass, gravity, velocity, radius, circumference, centAc, centForce = roadSetup()
    support = round(((mass * velocity ** 2) / radius) -(mass * gravity), 2)*-1
    hump, vehicle = humpGen(), vehicleGen()
    q.questionBase = f"A {vehicle} of mass {mass} kg passes over a {hump} of radius of curvature {radius} m  at a speed of {velocity} m/s. Calculate:"
    q1 = f"the centripetal acceleration of the {vehicle} on the bridge"
    q2 = f"the support force on the {vehicle} when it was at the top."
    a1 = f"{centAc} m/s²"
    a2 = f"{support} N"
    q.diagram, q.constant, q.answer, marks = None, None, None, None
    m1, m2 = 2, 2
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = None
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
    ]
    return q.returnAll()

def e1acb_roundaboutpxax7():
    q = ucf.Question(ucf.currentFuncName())
    mass, gravity, velocity, radius, circumference, centAc, centForce = roadSetup()
    vehicle = vehicleGen()
    q.questionBase = f"The maximum speed for no skidding of a {vehicle} of mass {mass} kg on a roundabout of radius {radius} m is {velocity} m/s. Calculate:"
    q1 = f"the centripetal acceleration at this point"
    q2 = f"the centripetal force on the vehicle when moving at this speed"
    q3 = f"the friction coefficient in this scenario."
    a1 = f"{centAc} m/s²"
    a2 = f"{centForce} N"
    a3 = f"{round((velocity**2)/(gravity*radius), 4)}"
    m1, m2, m3 = 2, 2, 3
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = None
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

def e1acc_racingtrackpiax2():
    q = ucf.Question(ucf.currentFuncName())
    mass, gravity, velocity, radius, circumference, centAc, centForce = roadSetup()
    angle = randint(10, 30)
    velocity = round((gravity * radius * math.tan(angle/57.2958))**0.5, 2)
    q.questionBase = f"At a racing snail circuit, the track is banked at an angle of {angle}° to the horizontal on a bend that has a radius of curvature of {radius} m. Use the equation v² =grtan\u03B8 to calculate the speed of a vehicle on the bend if there is to be no sideways friction."
    q.answerBase = f"{velocity}"
    q.answerUnits = 'm/s'
    q.marksBase = 2
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer = None, "\u03c0 = 3.1415926535898", None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = None
    q.qtype = 'type'
    return q.returnAll()

def e1ada_rollercoasterpxax7():
    q = ucf.Question(ucf.currentFuncName())
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = fairgroundSetup()
    name = ("Trump's Wall", "Corbyn's Gulag Line", "Brexit Express", "The Smasher")
    q.questionBase = f"A train on a ride named {name[randint(0, len(name)-1)]} is initially stationary before it descends through a height of {height} m into a dip that has a radius of curvature of {radius} m."
    q1 = f"Calculate the speed of the train at the bottom of the dip, assuming air resistance and friction don't exist because this is physics"
    q2 = f"Calculate the centripetal acceleration at the bottom of the dip"
    q3 = f"Calcuate the extra support force on a person of weight {round(mass*9.8, 2)} N assuming that g is 9.8m/s²"
    a1 = f"{velocity} m/s"
    a2 = f"{centAc} m/s²"
    a3 = f"{extraSupport} N"
    m1, m2, m3 = 2, 2, 3
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = None
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

def e1adb_swingpxax7():
    q = ucf.Question(ucf.currentFuncName())
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = fairgroundSetup()
    velocity = round(((mass * gravity * height)/0.5/mass)**0.5, 2)
    centAc = (velocity ** 2) / height
    extraSupprt = (2 * mass * gravity * height) / height
    name = ("Trump's Beautiful Wall World", "Corbyn's Soviet Dreamworld", "Boris' Brexitland", "Greta's Dare Park", "Merkl's Magical Happy Euroland", "Assad's No Nulcear Activity Here Land")
    q.questionBase = f"An innapropriately named swing at {name[randint(0, len(name)-1)]} is {height} m in length. A pleb of mass {mass} kg descends from a position where the swing is horizontal. Calculate:"
    q1 = f"the speed of the pleb at the lowest point, assuming air resistance and friction don't exist because science,"
    q2 = f"the centripetal acceleration at the bottom of the dip,"
    q3 = f"the extra support force on a person at the lowest point."
    a1 = f"{velocity} m/s"
    a2 = f"{centAc} m/s²"
    a3 = f"{extraSupport} N"
    m1, m2, m3 = 2, 2, 3
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = None
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

def e1adc_wheelpxax7():
    q = ucf.Question(ucf.currentFuncName())
    gravity, mass, radius, height, time, circumference, speedOfPoint, velocity, centAc, centForce, support, extraSupport, reaction = fairgroundSetup()
    centAc = round((speedOfPoint ** 2) / radius, 2)
    extraSupport = round(((mass * speedOfPoint ** 2) / radius) - mass * gravity, 2)
    name = ("Trump's Beautiful Wall World", "Corbyn's Soviet Dreamworld", "Boris' Brexitland", "Greta's Dare Park", "Merkl's Magical Happy Euroland", "Assad's No Nulcear Activity Here Land")
    q.questionBase = f"The 'Big Wheel' at {name[randint(0, len(name)-1)]} has a radius of {radius} m and rotates once every {time} seconds. Calculate:"
    q1 = f"the speed of rotation of the perimeter of the wheel,"
    q2 = f"the centripetal acceleration of a person at the perimeter,"
    q3 = f"the support force on a person  of mass {mass} kg at the highest point."
    a1 = f"{speedOfPoint} m/s"
    a2 = f"{centAc} m/s²"
    a3 = f"{extraSupport} N"
    m1, m2, m3 = 2, 2, 3
    name = currentFuncName()
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:3], 0, 3, ucf.currentFuncName(), module_path())
    q.diagram, q.constant, q.answer, marks = None, "\u03c0 = 3.1415926535898", None, None
    q.hint = None
    q.video, q.weblink = None, None
    q.piclink = None
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': q1, 'sub_answer': a1, 'sub_mark': m1 }, 
       {'sub_number': 2, 'sub_question': q2, 'sub_answer': a2, 'sub_mark': m2 }, 
       {'sub_number': 3, 'sub_question': q3, 'sub_answer': a3, 'sub_mark': m3 }, 
    ]
    return q.returnAll()

