from random import randint

#atom generator
def generate_atom(proton_number = None):
    table = [[1, 'n', 0], [1, 'H', 1], [4, 'He', 2], [7, 'Li', 3], [9, 'Be', 4], [11, 'B', 5], [12, 'C', 6], [14, 'N', 7], [16, 'O', 8], [19, 'F', 9], [20, 'Ne', 10], [23, 'Na', 11], [24, 'Mg', 12], [27, 'Al', 13], [28, 'Si', 14], [31, 'P', 15], [32, 'S', 16], [35, 'Cl', 17], [40, 'Ar', 18], [39, 'K', 19], [40, 'Ca', 20], [45, 'Sc', 21], [48, 'Ti', 22], [51, 'V', 23], [52, 'Cr', 24], [55, 'Mn', 25], [56, 'Fe', 26], [59, 'Co', 27], [59, 'Ni', 28], [64, 'Cu', 29], [65, 'Zn', 30], [70, 'Ga', 31], [73, 'Ge', 32], [75, 'As', 33], [79, 'Se', 34], [80, 'Br', 35], [84, 'Kr', 36], [85, 'Rb', 37], [88, 'Sr', 38], [89, 'Y', 39], [91, 'Zr', 40], [93, 'Nb', 41], [96, 'Mo', 42], [98, 'Tc', 43], [101, 'Ru', 44], [103, 'Rh', 45], [106, 'Pd', 46], [108, 'Ag', 47], [112, 'Cd', 48], [115, 'In', 49], [119, 'Sn', 50], [122, 'Sb', 51], [128, 'Te', 52], [127, 'I', 53], [131, 'Xe', 54], [133, 'Cs', 55], [137, 'Ba', 56], [139, 'La', 57], [140, 'Ce', 58], [141, 'Pr', 59], [144, 'Nd', 60], [145, 'Pm', 61], [150, 'Sm', 62], [152, 'Eu', 63], [157, 'Gd', 64], [159, 'Tb', 65], [162, 'Dy', 66], [165, 'Ho', 67], [167, 'Er', 68], [169, 'Tm', 69], [173, 'Yb', 70], [175, 'Lu', 71], [178, 'Hf', 72], [181, 'Ta', 73], [184, 'W', 74], [186, 'Re', 75], [190, 'Os', 76], [192, 'Ir', 77], [195, 'Pt', 78], [197, 'Au', 79], [201, 'Hg', 80], [204, 'Tl', 81], [207, 'Pb', 82], [209, 'Bi', 83], [209, 'Po', 84], [210, 'At', 85], [222, 'Rn', 86], [223, 'Fr', 87], [226, 'Ra', 88], [227, 'Ac', 89], [232, 'Th', 90], [231, 'Pa', 91], [238, 'U', 92], [237, 'Np', 93], [244, 'Pu', 94], [243, 'Am', 95], [247, 'Cm', 96], [247, 'Bk', 97], [251, 'Cf', 98], [252, 'Es', 99], [257, 'Fm', 100], [258, 'Md', 101], [259, 'No', 102], [262, 'Lr', 103], [261, 'Rf', 104], [262, 'Db', 105], [266, 'Sg', 106], [264, 'Bh', 107], [277, 'Hs', 108], [268, 'Mt', 109], [281, 'Ds', 110], [272, 'Rg', 111], [285, 'Cn', 112], [286, 'Nh', 113], [289, 'Fl', 114], [289, 'Mc', 115], [293, 'Lv', 116], [294, 'Ts', 117], [294, 'Og', 118]]
    if proton_number == None:
        nucleus = table[randint(0,118)]
    else: 
        nucleus = table[proton_number]
    proton = nucleus[2]
    element = nucleus[1]
    mass = nucleus[0]
    neutron = nucleus[0] - nucleus[2]
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    atom = f"{mass}{element}{proton}".translate(SUP)
    return atom, mass, element, proton

def make_atom(mass = 1, element = 'H', proton_number = 1):
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    atom = f"{mass}{element}{proton_number}".translate(SUP)
    return atom, mass, element, proton_number

#symbols
def alpha():
    return '\u03b1'

def beta():
    return '\u03b2'

def gamma():
    return '\u03b3'

def pionneg():
    return '\u03c0\u207b'

def pionpos():
    return '\u03c0\u207a'

def lambdaneutral():
    return '\u039c\u2070'

def kaon():
    return 'K\u2070'

def arrow():
    return '\u2192'

def decay_constant():
    return '\u03bb'



#constants

def electronChargeString():
    return 'e = 1.6 x 10\u207b\u00b9\u2079 C'

def electronCharge():
    return 1.6E-19

def nucleonMass():
    return 1.67e-27

