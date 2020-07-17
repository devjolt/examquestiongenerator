from random import randint
from django.shortcuts import render

def moduleList(): #to be used in selecting random modules AND to be used to generate module list for use by prevNext
    entireModuleList = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__:
            entireModuleList.append(key) 
    usableModuleList = entireModuleList[7:]  #all modules not to be used for views kept at the front of the file are not added to the usable list.
    return usableModuleList

def previousNext(place): # generates urls for next and previous buttons
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
    return f"/physics/matter_and_radiation/{previous_q}", f"/physics/matter_and_radiation/{next_q}"

#just makes everything less messy
def allArguments(previousQ='', nextQ='', diagram='', constant=None, questionBase='', answer = None, marks = None, question1=None, answer1=None, marks1=None, question2=None, answer2=None, marks2=None, question3=None, answer3=None, marks3=None):
    return {'previousQ':previousQ, 'nextQ':nextQ, 'diagram':diagram,'constant':constant,
            'questionBase':questionBase, 'answer':answer, 'marks':marks,
            'question1':question1, 'answer1': answer1, 'marks1':marks1,
            'question2':question2, 'answer2': answer2, 'marks2':marks2,
            'question3':question3, 'answer3': answer3, 'marks3':marks3,
            }

def atomGenerator():
    table = [[1, 'n', 0], [1, 'H', 1], [4, 'He', 2], [7, 'Li', 3], [9, 'Be', 4], [11, 'B', 5], [12, 'C', 6], [14, 'N', 7], [16, 'O', 8], [19, 'F', 9], [20, 'Ne', 10], [23, 'Na', 11], [24, 'Mg', 12], [27, 'Al', 13], [28, 'Si', 14], [31, 'P', 15], [32, 'S', 16], [35, 'Cl', 17], [40, 'Ar', 18], [39, 'K', 19], [40, 'Ca', 20], [45, 'Sc', 21], [48, 'Ti', 22], [51, 'V', 23], [52, 'Cr', 24], [55, 'Mn', 25], [56, 'Fe', 26], [59, 'Co', 27], [59, 'Ni', 28], [64, 'Cu', 29], [65, 'Zn', 30], [70, 'Ga', 31], [73, 'Ge', 32], [75, 'As', 33], [79, 'Se', 34], [80, 'Br', 35], [84, 'Kr', 36], [85, 'Rb', 37], [88, 'Sr', 38], [89, 'Y', 39], [91, 'Zr', 40], [93, 'Nb', 41], [96, 'Mo', 42], [98, 'Tc', 43], [101, 'Ru', 44], [103, 'Rh', 45], [106, 'Pd', 46], [108, 'Ag', 47], [112, 'Cd', 48], [115, 'In', 49], [119, 'Sn', 50], [122, 'Sb', 51], [128, 'Te', 52], [127, 'I', 53], [131, 'Xe', 54], [133, 'Cs', 55], [137, 'Ba', 56], [139, 'La', 57], [140, 'Ce', 58], [141, 'Pr', 59], [144, 'Nd', 60], [145, 'Pm', 61], [150, 'Sm', 62], [152, 'Eu', 63], [157, 'Gd', 64], [159, 'Tb', 65], [162, 'Dy', 66], [165, 'Ho', 67], [167, 'Er', 68], [169, 'Tm', 69], [173, 'Yb', 70], [175, 'Lu', 71], [178, 'Hf', 72], [181, 'Ta', 73], [184, 'W', 74], [186, 'Re', 75], [190, 'Os', 76], [192, 'Ir', 77], [195, 'Pt', 78], [197, 'Au', 79], [201, 'Hg', 80], [204, 'Tl', 81], [207, 'Pb', 82], [209, 'Bi', 83], [209, 'Po', 84], [210, 'At', 85], [222, 'Rn', 86], [223, 'Fr', 87], [226, 'Ra', 88], [227, 'Ac', 89], [232, 'Th', 90], [231, 'Pa', 91], [238, 'U', 92], [237, 'Np', 93], [244, 'Pu', 94], [243, 'Am', 95], [247, 'Cm', 96], [247, 'Bk', 97], [251, 'Cf', 98], [252, 'Es', 99], [257, 'Fm', 100], [258, 'Md', 101], [259, 'No', 102], [262, 'Lr', 103], [261, 'Rf', 104], [262, 'Db', 105], [266, 'Sg', 106], [264, 'Bh', 107], [277, 'Hs', 108], [268, 'Mt', 109], [281, 'Ds', 110], [272, 'Rg', 111], [285, 'Cn', 112], [286, 'Nh', 113], [289, 'Fl', 114], [289, 'Mc', 115], [293, 'Lv', 116], [294, 'Ts', 117], [294, 'Og', 118]]
    nucleus = table[randint(0,118)]
    proton = nucleus[2]
    element = nucleus[1]
    mass = nucleus[0]
    neutron = nucleus[0] - nucleus[2]
    massNumber = str(mass)
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    atom = f"{mass}{element}{proton}".translate(SUP)
    return atom, mass, element, proton

def electronCharge():
    return 1.6E-19

def nucleonMass():
    return 1.67e-27

def nucleus2(request):
    table = tableGenerator()
    nucleus = table[randint(0,118)]
    question = "How many protons and neutrons in this nucleus:"
    proton = nucleus[2]
    element = nucleus[1]
    nucleon = nucleus[0]
    neutron = nucleus[0] - nucleus[2]
    return render(request,"physics/nucleus.html", {'question': question, 'proton':proton, 'element':element, 'nucleon':nucleon, 'neutron':neutron})

def nucleus(request):
    place, diagram, constant = 0, None, None
    previousQ, nextQ=previousNext(place)
    atom, mass, element, proton = atomGenerator()    
    questionBase = f" {atom}"
    question1 = "How many protons in the above nucleus?"
    answer1 = f"{proton}"
    question2 = "How many neutrons in the above nucleus?"
    answer2 = f"{mass-proton}"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 1, question2, answer2,1))

def namepartoftheatom(request):
    place, diagram, constant = 1, None, None
    previousQ, nextQ=previousNext(place)
    answers = [["neutrons",["have zero charge", "have the largest mass", "when removed create a different isotope"]],
           ["protons", ["have positive charge", "have second to largest mass", " have the second to largest specific charge", "dictate what element an atom is"]],
           ["electrons", ["have negative charge", "have the highest specific charge", "dictate whether the atom is an ion"]]]
    nuclide = randint(0, len(answers)-1)
    qu = randint(0, len(answers[nuclide][1])-1)
    questionBase = f'Name the part of the atom which {answers[nuclide][1][qu]}.'
    answer = f'The {answers[nuclide][0]} {answers[nuclide][1][qu]}.'
    constant = ''
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, 1))

def ionised(request):
    place, diagram, constant = 2, None, f"charge of an electron = {electronCharge()}"
    previousQ, nextQ=previousNext(place)
    atom, mass, element, proton = atomGenerator()   
    losesGains = "loses" if randint(0,1)==0 else "gains"
    electrons = randint(1,4)
    electron = -electrons if losesGains == "loses" else electrons
    questionBase = f"An {atom} atom {losesGains} {electrons} electrons."
    question1 = "What is the charge of the atom in Coulombs?"
    answer1= f"{(-electron * electronCharge())} C"
    question2 = "State the number of nucleons the atom contains."
    answer2 = f"{mass}"
    question3 = "Calculate its specific charge in Ckg-1. "
    specificCharge = round((-electron * float(electronCharge())) / (mass * float(nucleonMass())), 2)
    if specificCharge < 0: specificCharge *= -1
    answer3 = f"{specificCharge}"
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, None, None, question1, answer1, 2, question2, answer2, 1, question3, answer3, 3))
