from django.shortcuts import render
from random import randint, randrange
from comptia_a_plus import comptia_classes_functions as cf
from comptia_a_plus import variety_lists as vl

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
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def module_path():
    return '/comptia_a_plus/core_1_220_1001/'

#paper, series, question, name, marks in names
def test():
    pairs = (
        ('Pair 1 item a', 'Pair 1 item b'),
        ('Pair 2 item a', 'Pair 2 item b'),
        ('Pair 3 item a', 'Pair 3 item b'),
        ('Pair 4 item a', 'Pair 4 item b'),
        ('Pair 5 item a', 'Pair 5 item b'),
        ('Pair 6 item a', 'Pair 6 item b'),
        ('Pair 7 item a', 'Pair 7 item b'),
        ('Pair 8 item a', 'Pair 8 item b'),
        ('Pair 9 item a', 'Pair 9 item b'),
        ('Pair 10 item a', 'Pair 10 item b'),
    )
    correct = ('correct1', 'correct2', 'correct3', 'correct4', 'correct5', 'correct6', 'correct7', 'correct8', 'correct9', 'correct10')
    incorrect = ('incorrect1', 'incorrect2', 'incorrect3', 'incorrect4', 'incorrect5', 'incorrect6', 'incorrect7', 'incorrect8', 'incorrect9', 'incorrect10')
    q = cf.SelectMcDrag('multi', None, None, pairs, () )
    return q.returnAll()

def test_dr():
    pairs = (
        ('Pair 1 item a', 'Pair 1 item b'),
        ('Pair 2 item a', 'Pair 2 item b'),
        ('Pair 3 item a', 'Pair 3 item b'),
        ('Pair 4 item a', 'Pair 4 item b'),
        ('Pair 5 item a', 'Pair 5 item b'),
        ('Pair 6 item a', 'Pair 6 item b'),
        ('Pair 7 item a', 'Pair 7 item b'),
        ('Pair 8 item a', 'Pair 8 item b'),
        ('Pair 9 item a', 'Pair 9 item b'),
        ('Pair 10 item a', 'Pair 10 item b'),
    )
    q = cf.DragAndDrop(pairs, None, 1, 2, 6)
    print('Trying')
    return q.returnAll()

def test_do():
    pairs = (
        ('Gaming PC RAM', '12GB RAM'),
        ('Gaming PC Graphics', 'Pair 2 item b'),
        ('Gaming PC Power Supply', 'Pair 3 item b'),
        ('Gaming PC Cooling', 'Pair 4 item b'),
        ('Gaming PC Peripherals', 'Pair 5 item b'),
        ('Virtualisation PC RAM', '24GB RAM'),
        ('Pair 7 item a', 'Pair 7 item b'),
        ('Pair 8 item a', 'Pair 8 item b'),
        ('Pair 9 item a', 'Pair 9 item b'),
        ('Pair 10 item a', 'Pair 10 item b'),
    )
    q = cf.DragAndDrop(pairs, None, 1, 10, 10)
    print('Trying')
    return q.returnAll()

def aaa1_grounding_hardware():
	correct =('Multimeter',)
	incorrect = ('Cable tester','Tone generator','Voltmeter','grounding meter', 'Ethernet tester')
	q = cf.SelectMcDrag(None, correct, incorrect,None, (), 1, 1, randint(4, len(incorrect)))
	q.questionBase = f"During an inspection, it was found that data racks were not properly grounded. To pass the inspection and address a growingconcern to protect data cabling and equipment, a technician must make sure all racks are properly grounded. Which of the following tools should the {q.item(vl.technitians)} technician use to verify this has been completed?"
	q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
	return q.returnAll()

def aac1_device_choice_mc():
    items = (
        ("chart activity while keeping in contact with the home office", "Smart watch"),
        ("count the number of footsteps she takes every day", "Fitness monitor"),
        ("track distance travelled to claim expenses", "Global Positioning sensor"),
        ("have internet access in locations without access to ethernet or wifi", "Portable hotspot"),
    )
    q = cf.SelectMcDrag('multi', None, None, items,())
    q.questionBase = f"A {q.item(vl.users)} is seeking advice on which device to purchase for a friend who is a {q.item(vl.businesses)} business owner. The friend needs the ability to {items[q.choice][0]}. Which of the following would be the BEST recommendation?"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aad1_device_power():
    items = (
        ("They are concerned about wall outlet availability at the conferences and needs to continuously use the device for important updates whilst moving easilly between workshops.", "Wireless charging pad"),
        ("It is expected that wall outlets will be readilly available.", "An extra charging cord"),
        ("Much of the conference will involve practical exercises away from the computer, but they will need to go online once during the day to check in with the office.", "Power saving mode"),
        ("The conference lasts for several days, and part of it will be spent in a remote location without access to power.", "Power bank"),
    )
    fillers = ("Airplane mode", "USB cable", "Mobile hotspot")
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4,7))
        q.questionBase = f"{q.item(vl.names)}, a {q.item(vl.technitians)} {q.item(vl.users)}, needs to attend several day-long conferences and wants to ensure their mobile device will have enough power for these events. {items[q.choice][0]} Which of the following should a technician recommend to BEST accommodate their needs at the lowest cost?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(1,3), randint(4,7))
        q.questionBase = f"Match the solutions with the concerns of a management team sending a delegate to a conference"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aae1_mobile_technology_dr():
    items = (
        ('Devices use haptic confirmation for sharing data wirelessly.', 'IR'),
        ('Devices are paired using a code for sharing data wirelessly.', 'Bluetooth'),
        ('Devices are placed in close proximity within line of sight for sharing data wirelessly', 'NFC'),
        ('Devices are connected via a wire for sharing data or connectivity', 'Tethering'),
    )
    fillers = ('Lightning', 'Digital Speech', 'Email', 'Microwaves', 'Ethernet', 'Hotspot', 'Cellular')
    q = cf.SelectMcDrag('drag', None, None, items, fillers)
    q.questionBase = "Drag each mobile technology to the description of its use. Some answers will not be used."
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aae2_laptop_security_mc():
    correct = ("Docking station",)
    incorrect = ("Port replicator", "Thunderbolt", "USB hub", "Lightning", "wireless hub",)
    q = cf.SelectMcDrag(None, correct, incorrect,None,(), 1, 1, randint(4, len(incorrect)))
    q.questionBase = f"A {q.item(vl.businesses)} business owner wants to provide security to laptop users with the ability to charge their devices, access corporate LAN resources, and allow for a variety of other removable hardware. Which of the following devices would BEST meet the owner’s needs?"    
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aae3_hotspot_mc():
    correct = ("The connection is throttled",)
    incorrect = ("There is a low RFID signal", "SSID is not found", "It is out of range", "IPconfig is invalid", "Incorrect port",)
    q = cf.SelectMcDrag(None, correct, incorrect, None, [], 1, 1, randint(4, len(incorrect)))
    q.questionBase = f"A {q.item(vl.technitians)} technician has noticed that when at a {q.item(vl.businesses)} company headquarters the laptop connection to the Internet is more responsive than when using the company-provided phone as a hotspot. The technician updated the drivers on the WiFi NIC without resolution and then verified the configuration on the WiFi was correct. Which of the following configurations could cause the decreased performance?"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aa", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()