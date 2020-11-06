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


#start here...
def ada1_cloud_attributes():	
    items = (
        ("allows scalable services to be provided to the client", "Rapid elasticity"),
        ("means that you only pay for what you use", 'Metered'),
        ("allows a user to access resources when they need them", 'On-demand'),
    )
    fillers = ('High speed', 'Mobile', 'Plasticity', 'Iconicity', 'Publicity', 'Resource pooling')
    if randint(0,1) == 0:
        q = cf.SelectMcDrag(None, None, None, items, fillers, 1, 1, 5)
        q.questionBase = f"Which of the following terms describes how cloud computing {items[q.choice][0]}?"
    else:
        q = cf.SelectMcDrag('drag', None, None, items, fillers, 1, randint(1,3), randint(4,7))
        q.questionBase = f"Match the attributes of cloud computing with the correct descriptive terms."
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ad", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

