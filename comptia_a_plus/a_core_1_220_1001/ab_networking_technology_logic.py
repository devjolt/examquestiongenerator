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




def ab_aa_network_ports():
    items = (
        ('File Transfer Protocol, data transfer', 20),
        ('File Transfer Protocol, command and control', 21),
        ('Secure Shell', 22),
        ('Time protocol', 37),
        ('WHOIS', 43),
        ('Domain Name Service', 53),
        ('Hypertext Transfer Protocol', '80 and 443'),
        ('Trivial File Transfer Protocol', 69),
    )
    fillers = (501, 404, 99, 127, 8080)
    if randint(0,1) == 0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4, 8))
        q.questionBase = f"Which of the following ports deals with {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(4, 6), randint(6, 10))
        q.questionBase = f"Match the ports with their functions."
        q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ab_ab_network_ports():
    items = (
        ('close to block remote logins to a server', 21),
        ('change to another port because it is the default SSL port well known to hackers', 22),
    )
    fillers = (43, 53, 80, 443, 69)
    if randint(0,1) == 0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4, 5))
        q.questionBase = f"Which of the following ports should a technitian {items[q.choice][0]}?"
        q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ab_ca_cable_type_soho_mc():
    correct = ("Ethernet",)
    incorrect = ("Coaxial", "USB", "Thunderbolt", "Lightning", "Bluetooth")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, randint(4, len(incorrect)))
    q.questionBase = f"Which of the following cable types should be used to connect a cable modem to a SOHO router?"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ab_da_networking_numbers():
    items = (
        ("a channel commonly used on an 802.11 wireless network","6"),
        ("an ip address known as local host", "127.0.0.1"),
        ("an ip adress you would expect to be associated with a router","192.168.X.X"),
        ("a port number assigned to commonly used internet communication protocol","80"),
        ("a port number associated with DNS","500"),
        ("an alternative port for http","8080"),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4, len(items)))
        q.questionBase = f"Which one of the following is {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(1,4), randint(4, len(items)))
        q.questionBase = f"Match the description with the number."
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ab_ea_internal_external_networking_mc():
    correct = ("MAN","LAN")
    incorrect = ("WAN", "PAN", "SAN", "WLAN", "VPN", "Enterprise Internal Private Network", "System Area Network", "Skynet", "Mobile Network")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(4, len(incorrect)))
    q.questionBase = f"A {q.item(vl.businesses)} business client has three locations within city limits that need to be networked. Vendor network requirements for all three locations are a minimum of 1GB. Which of the following are the types of networks that will MOST likely be used for internal office and office-to-office networking? (Choose two.)"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ab_eb_networking_acronyms_dr():
    items = (
        ('a computer network that interconnects users with computer resources in a geographic region of the size of a metropolitan area', 'MAN'),
        ('a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building', 'LAN'),
        ('a telecommunications network that extends over a large geographic area', 'WAN'),
        ('a computer network for interconnecting electronic devices centered on an individual person\'s workspace', 'PAN'),
        ('a computer network which provides access to consolidated, block-level data storage', 'SAN'),
        ('a computer network that links two or more devices using wireless communication', 'WLAN'),
        ('a service which extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network', 'VPN'),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4, len(items)))
        q.questionBase = f"Which one of the following is {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(4,5), randint(5, len(items)))
        q.questionBase = f"Match the definitions with their acronyms."
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ab_ea_internal_external_networking_mc():
    items = (
        ("office to office networking within a city", "MAN"),
        ("computer network within the office", "LAN"),
        ("5G services nationwide","WAN"),
        ("connectivity for devices within employees personal space", "PAN"),
        ("access to consolidated, block level storage","SAN"),
        ("wireless facilities for employees at an office","WLAN"),
        ("increased security and privacy for employees","VPN"),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, randint(4, len(items)))
        q.questionBase = f"A {q.item(vl.businesses)} business wishes to provide {items[q.choice][0]}. Which of the following technologies are best suited to provide this service? (Choose one)"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, (), 1, randint(4,5), randint(5, len(items)))
        q.questionBase = f"Match the described services with the accronyms of the technology which makes them possible."
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ab_eb_reducing_password_tickets_mc():
    items = (
        ("Several company users are frequently forgetting passwords for their mobile devices and applications. Which of the following should the systems administrator do to reduce the number of help desk tickets submitted?",'Implement single sign-on.'),
        ("A business owner requires a high level of security on all of their devices. Which of the following could be implemented at the lowest cost to achieve this?", 'Enable multifactor authentication.'),
        ("A business requires that all devices are only able to be accessed by the emplyee to which it is issued. Which of the following would achieve this most effectively?", 'Configure biometric authentication.'),
    )
    fillers = ('Remove complex password requirements.','Remove password requirements', 'Adopt one password for all employees', 'Set each password to the employees employee number')
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4, 6))
        q.questionBase = f"A {q.item(vl.businesses)} business wishes to provide {items[q.choice][0]}. Which of the following technologies are best suited to provide this service? (Choose one)"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(4,5), randint(5, 6))
        q.questionBase = f"Match the described problems with solutions."
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()