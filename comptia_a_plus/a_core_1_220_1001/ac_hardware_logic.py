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
def ac_aa_coaxial_cables_termination_mc():
    correct = ("RG-59",)
    incorrect = ("DB9", "RJ45", "RS-232")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = "Which of the following terminates a coaxial cable?"
    q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
    return q.returnAll()

def ac_ab_network_cables_and_terminations_dr():
    items = (
        ('a type of coaxial cable used for low-power video and radio frequency signal connections', 'RG-59/U'),
        ('a connector commonly used for video output and Controller Area Network', 'DE-9'),
        ('a connector used to terminate ethernet cable with one data ine and programming resistor', 'RJ45'),
    )
    fillers = ('DB9', 'RS-232')
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
            None, None, None, items, fillers, 1, 1, 4
            )
        q.questionBase = f"Which of these describes {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag(
            'drag', None, None, items, fillers, 1, randint(3,4), 5
            )
        q.questionBase = f"Match the descriptions with their names."  
    q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
    return q.returnAll()

def ac_ab_ethernet_cables_mc():
    items = (
        ("100 Mbit/s","Cat 5"),
        ("125 Mbit/s","Cat 5e"),
        ("1 Gbit/s","Cat 6"),
        ("10 Gbit/s","Cat 7"),
        ("25 Gbit/s","Cat 8"),
    )
    fillers = ('Cat 3',)
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
                None, None, None, items, fillers, 1, 1, randint(4,6)
                )
        q.questionBase = f"Which of the following would allow Ethernet at {items[q.choice][0]} at the lowest cost?"
    else:
        q = cf.SelectMcDrag(
                'drag', None, None, items, fillers,1, randint(3,4), randint(5,6)
                )
        q.questionBase = f"Match the speeds with the ethernet cable classifications."  
    q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
    return q.returnAll()

def ac_ab_ethernet_cables_dr():
    items = (
        ('used for data networks employing frequencies up to 16 MHz with up to 10 Mbps Ethernet networks', 'Cat 3'),
        ('allows data transmission over Ethernet at 100 Mbit/s and above at 100 MHz, uses twisted pairs', 'Cat 5'),
        ('allows data transmission over Ethernet at 125 Mbit/s and above at 100 MHz, uses twisted pairs', 'Cat 5e'),
        ('ethernet cable containing shield protected twisted pair wires, supports speeds of up to 1 Gb/s at up to 250 MHz, up to 55 meters', 'Cat 6'),
        ('well protected, but less flexible, supports speeds of up to 10 Gb/s at 500 MHz, over 55 meters', 'Cat 6A'),
        ('comprises four individually shielded pairs inside an overall shield, transmission of 10 Gb/s at 600 Mhz up to 15m', 'Cat 7'),
        ('shielded cable allowing data transmission over Ethernet at 25 Gb/s at 2 Ghz', 'Cat 8'),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
                None, None, None, items, (), 1, 1, randint(4,6)
                )
        q.questionBase = f"Which of the following fits the following description at the lowest cost: {items[q.choice][0]}"
    else:
        q = cf.SelectMcDrag(
                'drag', None, None, items, (),1, randint(3,5), randint(5,7)
                )
        q.questionBase = f"Match the descriptions of different types with Ethernet cable with their names."
    q.previousQ, q.nextQ = cf.previousNext(
            list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
            )
    return q.returnAll()

def ac_ba_usb_connectors_mc():
    items = (
        ("a non-directional connector","USB-C"),
        ("an almost square-shaped connector","USB-B"),
        ("a rectangular shaped connector, sized 16 x 8mm","USB-A"),
    )
    fillers = ("Micro-USB", "Mini-USB")
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
                None, None, None, items, fillers, 1, 1, randint(4,5)
                )
        q.questionBase = f"Which of the following charging and data ports has a {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag(
                'drag', None, None, items, fillers,1, randint(1,3), 5
                )
        q.questionBase = "Match the descriptions of different types of USB connectors with their names."
    q.previousQ, q.nextQ = cf.previousNext(
            list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
            )
    return q.returnAll()

def ac_bb_usb_connectors_dr():
    items = (
        ('24-pin USB connector system with a rotationally symmetrical connector.', 'USB-C'),
        ('6.85 by 1.8 mm connector intended for use with mobile devices', 'Micro-USB'),
        ('3 by 7 mm connector intended for use with small devices', 'Mini-USB'),
        ('16 by 8 mm with an elongated rectangular cross-section, carries both power and data', 'USB-A'),
        ('11.5 by 10.5 mm with a near square cross-section with the top exterior corners beveled, ', 'USB-B'),
    )
    if randint(0,1) ==0:
        q = cf.SelectMcDrag(
                None, None, None, items, (), 1, 1, randint(4,5)
                )
        q.questionBase = f"Which of the following is a {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag(
                'drag', None, None, items, (),1, randint(3,5), 5
                )
        q.questionBase = "Match the descriptions of different types of USB connectors with their names."
    q.previousQ, q.nextQ = cf.previousNext(
            list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
            )
    return q.returnAll()

def ac_ca_ram_upgrade():
    items = (
        ('A server needs a RAM upgrade','DDR'), 
        ('A laptop needs a RAM upgrade', 'SoDIMM'),
        ('The RAM in a router is faulty', 'SRAM'),
        ('Imagine that the RAM on a graphics card exploded', 'GDDR SDRAM'),
        )
    q = cf.SelectMcDrag(None, None, None, items, (), 1, 1, 4)
    q.questionBase = f"{items[q.choice][0]}, and a {q.item(vl.technitians)} technician has been tasked with retrieving the RAM from storage and then installing it. Which of the following is the BEST RAM type for the technician to retrieve?"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ac_da_storage():
    correct =('3TB HDD',)
    incorrect = ('500TB SAN','2GB USB drive' '50GB NAS','512GB SSD',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.users)} wants to upgrade a PCs internal storage to have more room to store backups, photos, and videos. The newstorage should be large enough to avoid expanding again next year. Which of the following BEST meets these needs at the lowest cost?"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ac_db_raid_solution():
    items = (
        ('want to prioritise performance due to the use of a large application with an enormous amout of data. They are prepared to accept the risk of data loss in case of failure.', 'RAID 0')
        ('want a fault tolerant system in case of failure, and can afford to purchase an additional storage device if needed.', 'RAID 1'),
        ('require consistent access to all data, high reliability and performance. They can afford to purchase two additional storage devices.', 'RAID 5'),
        ('insist on fast recovery in case of failure and high performance. Money is no object, and they can afford to purchase as many storage devices as needed.', 'RAID 10'),
    )
    fillers = ('RAID 2', 'RAID 3', 'RAID 4', 'RAID 6', 'RAID 7', 'RAID 8', 'RAID 9', 'RAID 11', 'RAID 15')
    q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4, 7))
    q.questionBase = f"A {q.item(vl.technitians)} technician is talking to a {q.item(vl.users)} about the specifications for an upgraded application server. The users {items[q.choice][0]}. Which of the following solutions should the technitian recommend?"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ac_dc_raid_description():
    items = (
        ('dividing data evenly across who or more storage devices.', 'RAID 0')
        ('simultaneously writing the same data to two storage devices.', 'RAID 1'),
        ('dividing data evenly across three or more storage devices, with parity spread across all drives.', 'RAID 5'),
        ('dividing data evenly across two or more devices, and duplicating the data on the same number of other devices.', 'RAID 10'),
        )
    fillers = ('RAID 2', 'RAID 3', 'RAID 4', 'RAID 6', 'RAID 7', 'RAID 8', 'RAID 9', 'RAID 11', 'RAID 15')
    if randint(0, 1) == 0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, randint(4, 7))
        q.questionBase = f"Which of the following options best fits this description: {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(2,4), randint(4, 7))
        q.questionBase = f"Match the following solutions with their descriptions:"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ac_fa_inventory_update_tags_mc():
    correct = ("Barcode scanner", "Magnetic Reader")
    incorrect = ("Label printer", "KVM switch", "NFC device", "Flatbed scanner", "Webcam", "CMOS")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 2, randint(4,6))
    q.questionBase = f"Which of the following peripherals would a {q.item(vl.businesses)} company use to take inventory quickly and update price tags for products? (Choose two.)"
    q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
    return q.returnAll()

def ac_fb_second_laptop_screena_mc():
	correct =('Adjust the monitor display settings.',)
	incorrect = (
        'Plug an external monitor into the USB port.',
        'Use the Fn and function key combination',
        'Enable DisplayPort',"ipconfid/display",
        "change BIOS settings")
	q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, randint(4,6))
	q.questionBase = f"An {q.item(vl.users)} wants to have a second monitor installed on a laptop. Which of the following would allow a technician to configurethe laptop to show both screens once the cable is connected?"
	q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
	return q.returnAll()

def ac_fc_projector_flickering():
    items = (
        ("A projector's image begins to flicker during a presentation. The laptop display does not produce this issue. When a technitian changes the resolution on the laptop, the issue persists.", "Check the connectivity of the VGA cable"),
        ("A projector sometimes seems to switch on and off during a presentation. The laptop is on throughout, as is the display.", "Check the connectivity of the power cable"),
        ("The image on a projector appears stretched, whilst the sides of the image are cut off compare to the laptop display.", "Change the aspect ratio on the laptop"),
    )
    fillers = ('Change the settings of the projector', 'Clean the projector\'s lens')
    q = cf.SelectMcDrag(
                None, None, None, items, fillers, 1, 1, randint(4,5)
                )
    q.questionBase = f"{items[q.choice][0]} Which of the following is the NEXT step the technitian should take?"
    q.previousQ, q.nextQ = cf.previousNext(
            list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
            )
    return q.returnAll()

def ac_ha_custom_video_editing_mc():
    correct = ( 
        "SSD", "Dual monitors", 
        "6 core processor", "discrete graphics card"
        )
    incorrect = (
        "Gigabit NIC", "Hypervisor", "Docking station", 
        "Flatbed scanner", "Webcam", "DVD drive"
        )
    choice = randint(1,3)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, choice, randint(4,6))
    q.questionBase = f"A {q.item(vl.users)} asks a {q.item(vl.users)} technician to help set up a specialized computing system for video editing. Which of the following should the technician install on the workstation to BEST meet the customer’s specifications? (Choose {choice})"
    q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
    return q.returnAll()

def ack1_print_settings_mc():
    single,double = ('Simplex',), ('Duplex',)
    other = (
        'Collate', 'Orientation', 'Transparency', 
        'Destination', 'Scale', 'Margins'
        )
    choice = randint(0,1)
    if choice == 1:
        correct, incorrect, component = double, single + other, 'both the front and back sides'
    else:
        correct, incorrect, component = single, double + other, 'one side'
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, randint(4,6))
    q.questionBase = f"A {q.item(vl.users)} wants to print a large job of {q.item(vl.printables)} on {component} of the paper. {q.item(vl.comments)} Which of the following settings should the technician advise the user to select in the printer settings?"
    q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
    return q.returnAll()

def ach1_custom_power_mc():
    correct = ("Input voltage",)
    incorrect = ("Efficiency rating","12V rail amperage","Number of SATA connectors")
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A technician is determining the specifications for a desktop computer that will be used at trade shows all over the world. The computer will have the maximum amount of RAM. The CPU, GPU, and storage will be typical of a business workstation. Which of the following system parameters is the MOST important for the technician to consider when choosing a power supply?"
    q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
    return q.returnAll()

def ach2_intermediate_use_gaming_mc():
    correct = ("Four-core processor","16GB DDR3 memory")
    incorrect = (
        "80mm case fans","12V rail amperage",
        "Number of SATA connectors", "RAID 5 array",
        "Encrypted hard drive"
        )
    q = cf.SelectMcDrag(
        None, correct, incorrect, None, (), 1, 2, randint(5,7)
        )
    q.questionBase = f"A {q.item(vl.users)} wants to purchase a new home computer. The machine will mainly be used for {q.item(vl.online_activities)}, except on weekends when the customer’s {q.item(vl.relations)} will use it to play games with friends. Which of the following should the technician focus on to meet these requirements? (Choose two)"
    q.previousQ, q.nextQ = cf.previousNext(
        list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path()
        )
    return q.returnAll()


def ac_ka_trouble_printing_document_type():
    correct = ('Verify the user is sending the document to the correct printer queue.',)
    incorrect = ('Stop and restart the PC print spooler service.','Have each user send the same document to the correct printer queue.','Stop and restart the print server queues, and then have the user resend the document.',)
    q = cf.SelectMcDrag(None, correct, incorrect, None, (), 1, 1, 4)
    q.questionBase = f"A {q.item(vl.users)} is having a problem with printing a specific document type. The network printer OCP shows that the printer is online with no errors. Other users are not having the same issue. The usersends the document to another printer and the document prints. Which of the following should a technician do FIRST in troubleshooting the problem?"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ac", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()




    '''
    ram = ('Continuous reboots','Blue Screen of death', 'The amount of RAM displays incorrectly', 'Sporadic freezes','Corrupted files', 'Attemps to install new programs fail','Video card fails to load', 'Ram not recognised by computer')
    cmos = ('Incorrect date or time displayed','Wrong BIOS time', 'Missing drivers for external devices such as printers', 'Unable to start programs')
    other = ('disdented capacitors', 'Computer starts in safe mode')
    choice = randint(0,1)
    number_to_find = randint(1,2)
    if choice == 1:
        correct, incorrect, component = ram, cmos + other, 'RAM'
        workon = "Symptoms of bad ram"
        weblink = "https://gigabytekingdom.com/signs-of-bad-ram/"
    else:
        correct, incorrect, component = cmos, ram + other, 'CMOS'
        workon = "Symptoms of CMOS battery failure"
        weblink = "https://www.techwalla.com/articles/the-signs-of-a-bad-cmos-battery"
    q = cf.MultipleChoice(correct, incorrect, 1, number_to_find, randint(3,6))
    q.workon, q.weblink = workon, weblink
    q.questionBase = f"A technitian is troubleshooting what appears to be a {component} issue on a PC. Which {number_to_find} of the following symptoms indicate that this is a {component} issue?"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"aea", 0, 3, cf.currentFuncName(), module_path())
    return q.returnAll()

    '''