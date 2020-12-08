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
    return ucf.moduleListGen(list_callable_functions(), 'f', 0, 1)

def module_path():
    return '/physics/fields/'

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


#constants
def electron():
    return 'e = 1.6 x 10\u207b\u00b9\u2079 C'

# Individual question logic starts here
def fbaa_electrical_field_observations_pxax4():
    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = "Explain each of the following observations in terms of transfer of electrons:"
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:2], 0, 2, ucf.currentFuncName(), module_path())
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': 'An insulated metal can is given a positive charge by touching it with a positively charged rod', 'sub_answer': 'On contact, electrons flow from the insulated metal to the positively charged rod, resulting in a net positive charge on the metal', 'sub_mark': 2 }, 
       {'sub_number': 2, 'sub_question': 'A negatively charged metal sphere suspended on a thread is discharged by connecting it to the ground using a wire', 'sub_answer': 'Electrons from the sphere are repelled by the negative charge on the ball and flow down the wire until the charge of the sphere is no longer negative', 'sub_mark': 2 }, 
    ]
    return q.returnAll()

def fbab_shuttling_ball_experiment_pxax4():
    q = ucf.Question(ucf.currentFuncName())
    q.questionBase = "In the shuttling ball experiment, explain why the ball shuttles faster if:"
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:2], 0, 2, ucf.currentFuncName(), module_path())
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': 'the potential difference between the plates is increased', 'sub_answer': 'On contact, electrons flow from the insulated metal to the positively charged rod, resulting in a net positive charge on the metal', 'sub_mark': 2 }, 
       {'sub_number': 2, 'sub_question': 'the plates are brought closer together', 'sub_answer': 'Electrons from the sphere are repelled by the negative charge on the ball and flow down the wire until the charge of the sphere is no longer negative', 'sub_mark': 2 }, 
    ]
    return q.returnAll()

def fbac_shuttling_ball_experiment2_pxax3():
    frequency = randint(20, 30)/10
    charge = 30
    charge_nano = 30e-9
    current = round(frequency*charge)
    number_of_electrons = (charge_nano/1.6e-19)/1e11

    q = ucf.Question(ucf.currentFuncName())
    q.constant = electron()
    q.questionBase = f"A ball shuttles between two oppositely charged metal plates at a frequency of {frequency}Hz. The ball carries a charge of {charge}nC each time it shuttles from one plate to the other. Calculate:" 
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:2], 0, 2, ucf.currentFuncName(), module_path())
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': 'the average current in the circuit', 'sub_answer': f'{current}nA', 'sub_mark': 1 }, 
       {'sub_number': 2, 'sub_question': 'the number of electrons transferred each time the ball makes contact with a metal plate', 'sub_answer': f'{number_of_electrons}x10\u00b9\u00b9', 'sub_mark': 2 }, 
    ]
    return q.returnAll()

def fbad_charging_an_insulated_metal_conductorpxax3():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:2], 0, 2, ucf.currentFuncName(), module_path())

    q.questionBase = f"An insulated metal conductor is earthed before a negatively charged object is brought near to it:" 
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': 'Explain why the free electrons in the conductor move as far away from the charged object as they can.', 'sub_answer': f'The free electrons in the metal are repelled by negatively charged object because they are also negatively charged.', 'sub_mark': 1 }, 
       {'sub_number': 2, 'sub_question': 'The conductor is then briefly earthed. The charged object is then removed from the vicinity of the conductor. Explain why the conductor is left with an overall positive charge. ', 'sub_answer': f'When the conductor is earthed, electrons are able to flow out of the conductor to earth, resulting in less electrons in the conductor and an overall positive charge.', 'sub_mark': 2 }, 
    ]
    return q.returnAll()
'''
def fbba_electric_field_strength():
    q = ucf.Question(ucf.currentFuncName())
    q.previousQ, q.nextQ = ucf.previousNext(list_callable_functions(),ucf.currentFuncName()[:2], 0, 2, ucf.currentFuncName(), module_path())
    point_charge = 40
    

    q.questionBase = f"A +40 nC point charge O1 is placed in an electric field.
    q.questionPartList = [
       {'sub_number': 1, 'sub_question': 'Calculate the magnitude of the force on 01 ifthe electric field 1 strength where 0 is placed is 3.5 x 104 Vm- . 1.', 'sub_answer': f'The free electrons in the metal are repelled by negatively charged object because they are also negatively charged.', 'sub_mark': 1 }, 
       {'sub_number': 2, 'sub_question': 'b 	 0 1 is moved to a different position in the electric field. The force on O at this position is 1.6 x 10-3 N. Calculate the magnitude of the 1 electric field strength at this position. ', 'sub_answer': f'When the conductor is earthed, electrons are able to flow out of the conductor to earth, resulting in less electrons in the conductor and an overall positive charge.', 'sub_mark': 2 }, 
    ]
    return q.returnAll()
'''

#358