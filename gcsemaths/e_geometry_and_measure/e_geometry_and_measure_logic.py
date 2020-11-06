from django.shortcuts import render
from random import randint, randrange
from fractions import Fraction
from decimal import Decimal
import sys
import math

from gcsemaths import gcsemaths_classes_functions as cf
#from gcsemaths import variety_lists as vl

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
    return cf.moduleListGen(list_callable_functions(), 'e', 0, 1)

def module_path():
    return '/gcsemaths/e_geometry_and_measure/'

def triangle():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2F564x%2Fe4%2F33%2F53%2Fe433536f48dbb7624afe948d118a4bcd.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmemegenerator.net%2Fimg%2Finstances%2F75884024.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2Foriginals%2Fd7%2F3f%2F97%2Fd73f97d8d55c5f78027abc9c8af85971.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgflip.com%2Fsdp60.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi0.kym-cdn.com%2Fphotos%2Fimages%2Fnewsfeed%2F000%2F403%2F150%2Fb01.png&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.Xdw7ITdnQcHst926igzqrgHaHa%26pid%3DApi&f=1", "http://undergrad.osu.edu/buckeyes_blog/wp-content/uploads/2015/10/1.jpg", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.dumpaday.com%2Fwp-content%2Fuploads%2F2016%2F01%2Ffunny-pictures-144.jpg&f=1&nofb=1"]
    return shape_list[randint(0,len(shape_list)-1)]

def parallelogram():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fparallelogram-a-parallelogram-is-a-rectangle-that-just-cannot-today-18734770.png&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.me.me%2Fquadrilaterals-perimeter-name-the-quadrilateral-bo-on-name-hole-rectangle-7221385.png&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2F736x%2F23%2F51%2F16%2F23511668497135cace929da12fb69acf.jpg&f=1&nofb=1"]
    return shape_list[randint(0,len(shape_list)-1)]

def trapezium():
    shape_list = ("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi2.kym-cdn.com%2Fphotos%2Fimages%2Ffacebook%2F000%2F439%2F553%2F48f.png&f=1&nofb=1","https://img00.deviantart.net/4624/i/2006/115/3/5/quarrel_of_quadrilaterals_by_cynosura.jpg", "https://pics.me.me/applic-as-a-head-shaped-li-a-trapezoid-11050166.png","https://pics.onsizzle.com/improtant-don-t-spill-trapezoids-on-yorr-existence-cake-my-cousin-29574757.png","http://www.kappit.com/img/pics/201603_2331_ecidi_sm.jpg","https://pics.me.me/barber-what-do-you-want-supreme-leader-him-hit-me-16614478.png","https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2F736x%2F4e%2F60%2F17%2F4e6017f46f6dbeeaa13db07c38ec1a51.jpg&f=1&nofb=1","https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.kappit.com%2Fimg%2Fpics%2F19527281cdhaf_sm.jpg&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fits-a-trapezoid-9001383.png&f=1&nofb=1")
    return shape_list[randint(0,len(shape_list)-1)]

def completePeopleGen():
    he = ["Bob", "Alfred", "Batman", "Borris Johnson", "Donald Trump", "Jeremy Corbyn", "Spongebob Squarepants", "Rick Astley", "Napoleon", "Bob Marley","Jacob Marley"]
    she = ["Madonna", "She-Ra", "Superwoman", "Applejack", "Theresa May", "Elsa", "Anna"]
    choice = randint(0,1)
    if choice == 0: return "he", he[randint(0,len(he)-1)]
    if choice == 1: return "she", she[randint(0,len(she)-1)]

def letterGen(low = 1, high = 26):
    return chr(randint(96+low, 96+high))

def eselect_random():
    modList = moduleListGen("e",0, 1)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def egeometry_basics_random():
    modList = moduleListGen("ea1", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def egeometry_parallel_random():
    modList = moduleListGen("ea2", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")

def egeometry_problems_random():
    modList = moduleListGen("ea3", 0, 3)
    return eval(f"{modList[randint(0,len(modList)-1)]}()")


#previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video

def ea1_angles_in_triangle_no_diagram13():
    a = [letterGen(1,10), 40 + randint(0, 40)]
    b = [letterGen(11,18), 40 + randint(0, 40)]
    c = [letterGen(19, 26), 180 - a[1] - b[1]]
    questionBase = f"'{a[0]}{b[0]}{c[0]}', '{c[0]}{a[0]}{b[0]}' and '{b[0]}{c[0]}{a[0]}' are three angles in a triangle. If '{a[0]}{b[0]}{c[0]}' is {b[1]}\u00B0 and '{c[0]}{a[0]}{b[0]}' is {a[1]}\u00B0, what is the value of '{b[0]}{c[0]}{a[0]}'?"
    answer = f"{c[1]}\u00B0"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


    
def ea1_angles_in_triangle_diagram13():
    a = ['x', 40 + randint(0, 40)]
    b = ['y', 40 + randint(0, 40)]
    c = ['z', 180 - a[1] - b[1]]
    questionBase = f"Find the value of {c[0]} if {a[0]} = {a[1]}\u00B0 and {b[0]} = {b[1]}\u00B0"
    answer = f"{c[1]}\u00B0"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.diagram = '/diagrams/gcsemaths/triangle_scalene_xyz.jpg'
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ea1_angles_on_straight_line_diagram13():
    a = ['x', 40 + randint(0, 40)]
    b = ['y', 40 + randint(0, 40)]
    c = ['z', 180 - a[1] - b[1]]
    questionBase = f"Find the value of {c[0]} if {a[0]} = {a[1]}\u00B0 and {b[0]} = {b[1]}\u00B0"
    answer = f"{c[1]}\u00B0"
    diagram, constant, marks = '/diagrams/gcsemaths/straight_line_xyz.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea1_angles_in_quadrilateral_diagram13():
    a = ['k', 50 + randint(0, 40)]
    b = ['l', 50 + randint(0, 40)]
    c = ['m', 50 + randint(0, 40)]
    d = ['n', 360 - a[1] - b[1] - c[1]]
    questionBase = f"{a[0]} = {a[1]}\u00B0, {b[0]} = {b[1]}\u00B0, {c[0]} = {c[1]}\u00B0. Find the value of the angle at x"
    answer = f"{d[1]}\u00B0"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, '/diagrams/gcsemaths/quadrilateral_klmn.jpg'
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea1_angles_in_isosceles_triangle_diagram13():
    a = ['a', 40 + randint(0, 40)]
    b = ['b', a[1]]
    c = ['c', 180 - (a[1]*2)]
    questionBase = f"{a[0]} = {a[1]}\u00B0, {b[0]} = {b[1]}\u00B0. Find the value of the angle at c"
    answer = f"{c[1]}\u00B0"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, '/diagrams/gcsemaths/isosceles_abc.jpg'
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea1_isosceles_triangle_pair_known_diagram13():
    a = ['a', 40 + randint(0, 40)]
    b = ['b', a[1]]
    c = ['c', 180 - (a[1]*2)]
    angle = [a,b,c]
    choice = randint(1,2)
    questionBase = f"Angle {a[0]} is {a[1]}\u00B0. What is the value of angle {angle[choice][0]}?"
    answer = f"{angle[choice][1]}\u00B0"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, '/diagrams/gcsemaths/isosceles_abc.jpg'
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea1_isosceles_triangle_single_known_diagram():
    a = ['a', 40 + randint(0, 40)]
    b = ['b', a[1]]
    c = ['c', 180 - (a[1]*2)]
    angle = [a,b,c]
    choice = randint(0,1)
    questionBase = f"Angle {c[0]} is {c[1]}\u00B0. What is the value of angle b?"
    answer = f"{a[1]}\u00B0"
    diagram = '/diagrams/gcsemaths/isosceles_abc.jpg'
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ea2_angles_around_parallel_lines13():
    y = 10 + randint(10, 60)
    x = 180 - y
    values = [['a', x],['d', x], ['e', x],['h', x], ['b',y], ['c',y],['f',y], ['g',y]]
    choice1 = randint(0,7)
    choice2 = choice1
    while choice2 == choice1: choice2 = randint(0,7)
    questionBase = f"Angle {values[choice1][0]} is {values[choice1][1]}\u00B0. What is the value of angle {values[choice2][0]}?"
    answer = f"{values[choice2][1]}\u00B0"
    diagram, constant, marks = '/diagrams/gcsemaths/parallel_around_abcdefgh.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea2_alternate_angles_parallel_lines13():
    x = 10 + randint(10, 60)
    y = 180 - x
    values = [['a', x],['z', x]]
    questionBase = f"Angle a is {x}\u00B0. What is the value of angle z?"
    answer = f"{x}\u00B0"
    diagram, constant, marks = '/diagrams/gcsemaths/parallel_alternate_side_az.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea2_allied_angles_parallel_lines13():
    x = 10 + randint(10, 60)
    y = 180 - x
    values = [['a', x],['z', x]]
    questionBase = f"Angle a is {x}\u00B0. What is the value of angle z?"
    answer = f"{y}\u00B0"
    diagram, constant, marks = '/diagrams/gcsemaths/parallel_allied_az.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea2_corresponding_angles_parallel_lines13():
    x = 10 + randint(10, 60)
    y = 180 - x
    values = [['a', x],['z', x]]
    questionBase = f"Angle a is {x}\u00B0. What is the value of angle z?"
    answer = f"{x}\u00B0"
    diagram, constant, marks = '/diagrams/gcsemaths/parallel_corresponding_az.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea3_problem213():
    a = randint(30, 80)
    b = a
    c = 180 - (a*2)
    d = 180 - a
    e = 180 - c
    answers = [["a", a],["b", b],["c",c],["d",d],["e",e]]
    choice1 = randint(0,4)
    choice2 = choice1
    while choice2 == choice1:
        choice2 = randint(0,4)
    questionBase = f"On the diagram above, angle {answers[choice1][0]} = {answers[choice1][1]}\u00B0. What is the value of angle {answers[choice2][0]}?"
    answer = f"{answers[choice2][1]}\u00B0"
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem2.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea3_problem333():
    dab = randint(45, 85)
    bcd = randint(45, 85)
    y = 360 - 90 - dab - bcd
    x = 90 - (180 - (dab + dab))
    questionBase = f"On the diagram above, DAB = {dab}\u00B0 and BCD = {bcd}\u00B0. Find the values of x and y."
    answer = f"x = {x}\u00B0, y = {y}\u00B0"
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem3.jpg', None, 3
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea3_problem433():
    fde = randint(10, 40)
    x = randint(10, 30)
    dEf = fde
    efd = 180-fde-fde
    w = dEf
    z = dEf
    bcd = 180 - x - z
    answers = [["FDE", fde],["x", x],["DEF",dEf],["EFD",efd],["w",w],["z",z],["BCD",bcd]]
    nope = []
    choice1 = randint(0,len(answers)-1)
    nope.append(choice1)
    choice2 = choice1
    while choice2 in nope:
        choice2 = randint(0,len(answers)-1)
    nope.append(choice2)
    choice3 = choice2
    while choice3 in nope:
        choice3 = randint(0,len(answers)-1)
    questionBase = f"On the diagram above, angle {answers[choice1][0]} = {answers[choice1][1]}\u00B0 and {answers[choice2][0]} = {answers[choice2][1]}\u00B0. What is the value of angle {answers[choice3][0]}?"
    answer = f"{answers[choice3][1]}\u00B0"
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem4.jpg', None, 3
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea3_problem533():
    n = randint(120, 160)
    o = 180 - n
    z = randint(10,30)
    r = 180 - o - z
    p = 180 - r
    q = r
    s = p
    t = o
    u = 180 - t
    v = p
    w = q
    x = n
    y = s
    answers1 = [["n",n],["o",o],["t",t],["u",u],["x",x]]
    answers2 = [["r",r],["p",p],["q",q],["s",s],["v",v],["w",w],["y",y]]
    nope = []
    choice1 = randint(0,len(answers1)-1)
    choice2 = randint(0,len(answers2)-1)
    choice3 = z
    questionBase = f"On the diagram above, angle {answers1[choice1][0]} = {answers1[choice1][1]}\u00B0 and z = {z}\u00B0. What is the value of angle {answers2[choice2][0]}?"
    answer = f"{answers2[choice2][1]}\u00B0"
    q = Question(cf.currentFuncName())
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem5.jpg', None, 3
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea2_alternate_allied_corresponding13():
    angleTypes = [['/diagrams/gcsemaths/parallel_alternate_side_az.jpg', "alternate"],['/diagrams/gcsemaths/parallel_allied_az.jpg',"allied"],['/diagrams/gcsemaths/parallel_corresponding_az.jpg',"corresponding"]] 
    choice = randint(0,2)
    questionBase = "What is the name given to angles such as the pair (a and z) in the diagram above?"
    answer = f"{angleTypes[choice][1]} angles"
    diagram, constant, marks = f'{angleTypes[choice][0]}', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
        
def ea3_problem613():
    x = randint(3,7)*5
    print(x)
    timesX = randint(3, 5)
    print(timesX)
    print(x*timesX)
    print(180 - x*timesX)
    plus = randint(10, 50)
    group1 = ["e","h"]
    group2 = ["f","g"]
    x1 = (f"{timesX-1}x")
    y1 = (f"x + {int(180 - (x*timesX))}")
    questionBase = f"{group1[randint(0,1)]} = {x1} and {group2[randint(0,1)]} = {y1}. Calculate x."
    answer = f"x = {x}"
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem6.jpg', None, 2
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea3_problem724():
    e = randint(50, 80)
    f = randint(110, 160)
    missing1 = f - e 
    h = randint(30, 60)
    missing2 = 180 - f - h
    g = 180 - missing1 - missing2
    questionBase = f"e = {e}, f = {f}, h = {h}. Calculate g."
    answer = f"g = {g}"
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem7.jpg', None, 2
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea3_problem813():
    x = randint(40, 70)
    questionBase = f"Angle x in the triangle above is {x}. Bob says that angle y is also {x} because the base angles in isoceles triangles are the same. Bob is wrong. Why?"
    answer = "An isoceles triangle is defined by two of its sides and angles being equal. The two equal angles do not have to be at the base of the triangle"
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem8.jpg', None, 2
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea3_problem923():
    statements = [["e = 180 - f because both angles are on a srtaight line", "e = f because both angles are on a straight line"],
                  ["e = h because they are alternate angles", "e = h because they are allied angles"],
                  ["h = 180 - f because they are allied angles", "g = f because they are allied angles"]]
    choice1 = randint(0,len(statements)-1)
    choice2 = choice1
    while choice1 == choice2: choice2 = randint(0,len(statements)-1)
    choice1, choice2 = statements[choice1], statements[choice2]
    wrong = randint(0,1)
    right = 1 if wrong == 0 else 0
    questionBase = f"One of these statements is incorrect: '{choice1[0]}', '{choice2[1]}'. Correct the incorrect statement."
    answer = f"{choice2[0]}"
    print(questionBase)
    print(answer)
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem6.jpg', None, 2
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ea3_problem1023():
    efd = randint(20, 50)
    bcd = randint(60, 80)
    baf = bcd
    afb = efd
    abf = 180 - baf - afb
    fed = abf
    answer = [["FED", fed], ["ABF", abf]]
    choice = randint(0, len(answer)-1)
    questionBase = f"Angle EFD = {efd}. Angle BCD = {bcd}. Find the value of {answer[choice][0]}."
    answer = f"{answer[choice][1]}"
    print(questionBase)
    print(answer)
    diagram, constant, marks = '/diagrams/gcsemaths/geometry_problem10.jpg', None, 2
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ea", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def polygons():
    return ("triangle","square","pentagon","hexagon","heptagon","octagon","nonagon","decagon")

def sides():
    return [i+3 for i in range(len(polygons()))]

def eb11_polygon_attributes13():
    polygonList, sidesList = polygons(), sides()
    choice = randint(0, len(polygonList)-1)
    attribute = ("sides", "interior angles", "exterior angles")
    choice2 = randint(0, len(attribute)-1) 
    questionBase = f"How many {attribute[choice2]} does a {polygonList[choice]} have?"
    answer = f"{sidesList[choice]}"
    diagram, constant, marks = None, None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb12_polygon_intext_angles13():
    polygonList, sidesList = polygons(), sides()
    choice = randint(0, len(polygonList)-1)
    attribute = ("interior angles", "exterior angles")
    choice2 = randint(0, len(attribute)-1)
    ans = (sidesList[choice]-2)*180 if choice2 == 0 else 360
    questionBase = f"What the sum of {attribute[choice2]} in a {polygonList[choice]}?"
    answer = f"{ans}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer,None
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb13_regular_polygon_attributes13():
    polygonList, sidesList = polygons(), sides()
    choice = randint(0, len(polygonList)-1)
    article = "an equilateral" if choice == 0 else "a regular"
    if choice == 1: article = "a"
    attribute = ("What is the order of rotational symmetry", "How many lines of symmetry", "What is the value of an exterior angle")
    choice2 = randint(0, len(attribute)-1)
    questionBase = f"{attribute[choice2]} in {article} {polygonList[choice]}?"
    answer = f"{sidesList[choice]}"
    if choice2 == 2: answer = f"{360 / sidesList[choice]}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer,None
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def eb14_regular_polygon_exterior_angles13():
    polygonList, sidesList = polygons(), sides()
    choice = randint(0, len(polygonList)-1)
    article = "an equilateral" if choice == 0 else "a regular"
    if choice == 1: article = "a"
    questionBase = f"What is the value of an exterior angle in {article} {polygonList[choice]}?"
    answer = f"{int(360 / sidesList[choice])}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer,None
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def eb25_triangle_attributes13():
    #equal sides, equal angles of 60, lines of, rotational
    trilist = ("an equilateral", "a right angled", "an isosceles", "a scalene")
    answerList = ((3, "3 equal angles of 60 degrees", 3, 3),
                  ("Up to 2 equal sides. Right angled triangles may be isosceles or scalene", "1 angle of 90 degrees", "1 if isosceles, 0 if scalene (right angled triangles can be either)", 0),
                  (2, "2 angles are the same", 1, "No rotational symmetry"),
                  ("All three sides are different", "All three angles are different",0,"No rotational symmetry"))
    choice = randint(0, len(trilist)-1)
    attribute = ("How many equal sides", "For a given triangle, how do its internal angles make it","How many lines of symmetry are", "What is the order of rotational symmetry")
    choice2 = randint(0, len(answerList)-1)
    questionBase = f"{attribute[choice2]} in {trilist[choice]} triangle?"
    answer = f"{answerList[choice][choice2]}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer,None
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def eb26_quadrilateral_attributes13():
    #sides, parallel, angles, lines of, rotational, diagonal
    polyList = ("a square", "a rectangle", "a rhombus", "a parallelogram", "a trapezium", "an isosceles trapezium", "a kite")
    answerList = (("4 sides of equal length", "2 pairs of parallel sides", "4 equal angles of 90 degrees", 4, 4, "Diagonals are the same length and are at right angles"),
                  ("2 pairs of sides of equal length", "2 pairs of parallel sides", "4 equal angles of 90 degrees", 2, 2, "Diagonals are the same length"),
                  ("4 sides of equal length", "2 pairs of parallel sides", "2 pairs of equal angles, where opposite angles are equal and neighbouring angles add up to 180 degrees", 2, 2),
                  ("All three sides are different", "2 pairs of parallel sides", "2 pairs of equal angles, where opposite angles are equal and neighbouring angles add up to 180 degrees",0,2),
                  ("No sides are the same length", "1 pair of parallel sides", "All angles may be different", 0,0,"diagonals have no relationship"),
                  ("Sloping sides are the same length", "1 pair of parallel sides", "Two pairs of identical angles", 1, 0, "diagonals are the same length"),
                  ("2 pairs of equal sides","No parallel sides", "1 pair of equal angles", 1, 0, "Diagonals cross at right angles"))
    choice = randint(0, len(polyList)-1)
    attribute = ("How are the length of the sides related in", "How many sides are parallel in", "How are the internal angles related in","How many lines of symmetry are in","What is the order of rotational symmetry in", "How are the diagonals related in")
    choice2 = randint(0, len(attribute)-1)
    questionBase = f"{attribute[choice2]} {polyList[choice]}?"
    answer = f"{answerList[choice][choice2]}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer,None
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def peopleGen():
    people = ("Donald Trump", "Stalin", "Jeremy Corbyn", "Madonna", "Posh Spice", "Justajolt", "An intelligent gorilla", "Boris Johnson", "Some pleb", "A man with a dry cough", "An unwilling kung fu student")
    return people
'''
def eb30_tangent_radius_diameter_chord():
    people = peopleGen()
    true_tuple = ("line a is a tangent", "line b is a radius", "line c is a diameter", "line d is a chord", "line b will always be half line c", "line a will only ever touch the circumference at one point", "line c always passes through the centre of the circle", "line b meets the cetre of the circle at one end and the circumference at the other end", "lines c and d both touch the circumference at two points", "line c meets the circumference at two points", "line d meets the circumference at two points")
    false_tuple = ("line a is a radius", "line a is a diameter", "line a is a chord", "line c will always be half line b", "line a will only ever touch the circumference at two points", "line c never passes through the centre of the circle", "line d meets the cetre of the circle at one end and the circumference at the other end", "lines b and d both touch the circumference at two points", "line a meets the circumference at two points", "line b meets the circumference at two points","line b is a tangent", "line b is a diameter", "line b is a chord", "line c is a tangent", "line c is a radius", "line c is a chord", "line d is a tangent", "line d is a radius", "line d is a diameter")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, line abc is a tangent and touches the circumference at the same point as radius r at point b. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip = "A tangent always makes an angle of exactly 90\u00b0 with the radius it meets at this point."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    previousQ, nextQ = previousNext("eb", 0, 2, currentFuncName())
    pre, preans, marks, level = None, None, 1, 3
    tip, video = None, None
    return previousQ, nextQ, diagram, constant, questionBase, answer, pre, preans, marks, level, tip, video
'''

def eb31_circle_radius_tangent():
    people = peopleGen()
    true_tuple = ("the angle xba will always be 90\u00b0", "xba is a right angle", "xbc is a right angle", "line abc will never touch the circle again after point b","joining x, b and c makes a right angled triangle")
    false_tuple = ("angle xba and xbc are not the same", "joining points x, b and c can make an equilateral triangle", "angle xbc is the only right angle on the diagram")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, line abc is a tangent and touches the circumference at the same point as radius r at point b. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip = "A tangent always makes an angle of exactly 90\u00b0 with the radius it meets at this point."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def eb32_circle_two_radi_isosceles():
    people = peopleGen()
    true_tuple = ("angles xba and xab are the same", "the triangle in the diagram has one line of symmetry", "two of the angles in the triangle made by radi r1 and r2 are the same", "two of the angles in the triangle made by r1 and r2 are the same","the triangle made by r1 and r2 has no rotational symmetry","any other two other radi would make another isoceles triangle")
    false_tuple = ("angle xba and xab are not the same", "joining points x, b and a can make an equilateral triangle", "the triangle made by r1 and r2 has rotational symmetry order 2","the triangle made by r1 and r2 is scalene", "the triangle made by r1 and r2 has three different angles",)
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"Radi r1 and r2 meet the circumference are joined by a chord to make a triangle. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip = "Two radi formed from the ends of a chord which meet in the centre of a circle form an isosceles triangle."
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def eb33_perpendicular_bisector_chord():
    people = peopleGen()
    true_tuple = ("xy passes directly through the centre of the circle", "the angles around the point where ab and xy cross are all right angles", "the angles around the point where ab and xy cross are all equal", "the lengths of ab on either side of xy are equal")
    false_tuple = ("xy does not pass through the centre of the circle", "the angles around the point where ab and xy interect are not equal", "the two pairs of angles around the point where ab and xy intesect are not the same","the lengths of ab on either side of xy will never be equal")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, xy bisects the chord ab exactly. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="The perpendicular bisector of a chord passes through the centre of the circle."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def eb34_angle_centre_twice_circumference():
    people = peopleGen()    
    true_tuple = ("angle y is double angle x", "and x is half angle y", "if angle x were {number}\u00b0, angle y would be{number*2}\u00b0", "the lengths of ab on either side of xy are equal", "if you know one of the angles at the base of the small triangle, you can calculate angles x and y", "There is one isosceles triangle in the diagram","if you know angle x, you can calculate angle y", "if you know angle y, you can calculate angle x", "if you know either angle x or y, you can calculate all of the angles in the smaller triangle", "The smaller triangle in the diagram is isosceles")
    false_tuple = ("angle y is half angle x", "angle x is double angle y", "even if you knew one of the angles, the other would be impossible to caclulate", "if angle x were {number}\u00b0, angle y would be{number*2}\u00b0 the two pairs of angles around the point where ab and xy intesect are not the same","both triangles are isosceles", "both triangles in the circle are scalene", "if one angle is {number} degrees, the other will be too", "if you know angle x or y, you can calculate the angles in both of the triangles", "the smaller triangle is scalene", "it's impossible to calculate the angles in the smaller triangle if you only know x or y" )
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, z is a chord. Angle y is made with lines directly from the ends of chord z, which meet at the centre of the circle. Angle x is also made with lines originating at the ends of chord z which meet at the circumference. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb35_angle_semi_circle():
    people = peopleGen()    
    true_tuple = ("angles at points c and d are both right angles", "angles at points c and d are both equal", "the triangle between points a, b and d is a right angled triangle", "the triangle between points a, b and c is a right angled triangle", "the triangle between the points a, b and c has no lines of symmetry", "the triangle between the points a, b and c has no rotational symmetry","the triangle between the points a, b and d has no lines of symmetry", "the triangle between the points a, b and d has no rotational symmetry")
    false_tuple = ("angles at points c and d are both greater than 90 degrees", "angles at points c and d are not equal", "the triangle between points a, b and d is an equilateral triangle", "the triangle between points a, b and c is equilateral", "the triangle between the points a, b and c has one line of symmetry", "the triangle between the points a, b and c has rotational symmetry order 1","the triangle between the points a, b and d has 1 lines of symmetry", "the triangle between the points a, b and d has rotational symmetry order 1")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, line ab is the diameter. Points c and d are where lines originating at the ends of the diameter meet the circumference. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    previousQ, nextQ = previousNext("eb", 0, 2, currentFuncName())
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb36_angle_same_segment_equal():
    people = peopleGen()
    num = randint(30, 60)
    true_tuple = ("angles at points c and d are the same", "angles at points e and f are the same", "if you know the angles at points c or d, you can calculate the angles at points e or f", "angle c plus angle e equals 180 degrees", "angle c plus angle f equals 180 degrees", "angle d plus angle e equals 180 degrees", "angle d plus angle f equals 180 degrees", "if the angle at point c were {num} degrees, the angle at point e or f would be {180-num} degrees", "if the angle at point e were {180-num} degrees, the angle at point c or d would be {num} degrees")
    false_tuple = ("angles at points c and d are different", "angles at points e and f are not the same", "if you know the angles at points c or d, you can't calculate the angles at points e or f", "angle c plus angle e equals 90 degrees", "angle c plus angle f equals 270 degrees", "angle d plus angle e equals 270 degrees", "angle d plus angle f equals 90 degrees", "if the angle at point c were {num} degrees, the angle at point e or f would be {90-num} degrees", "if the angle at point e were {270-num} degrees, the angle at point c or d would be {num} degrees", "the angles at points c and f are the same", "the angles at points d and f are the same", "the angles at point c and e are the same", "the angles at points d and e are the same")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, line ab is a chord. Points c, d, e and f are where lines originating at the ends of the chord meet the circumference. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb37_opposite_cyclic_quadrilateral():
    people = peopleGen()
    num = randint(30, 60)
    true_tuple = ("angles at points a and d add up to 180 degrees", "angles at points c and b add up to 180 degrees", "if you know angle at point a, you can work out angle at point d", "knowing point a won't help in calculating point b", "knowing point c won't help in calculating point d")
    false_tuple = ("angles at point a and d are equal", "angles at points c and d are equal", "angles a and b add up to 180 degrees", "angles c and d add up to 180 degrees", "if you know point a, you can calculate point b", "if you know point c, you can calculate point d")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, points a, b, c and d make a cyclic quadrilateral. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb38_tangents_point_same_length():
    people = peopleGen()
    num = randint(30, 60)
    true_tuple = ("the two triangles in the diagram above are congruent", "line cb is the same length as line db", "line ac is the same length as line ad", "angle acb is a right angle", "angle adb is a right angle", "triangle acb is a right angled triangle", "triangle abd is a right angled triangle", "both of the triangles are right angled triangles", "both of the angles at point a are the same", "both of the angles at point b are the same")
    false_tuple = ("the two triangles in the diagram above have different dimensions", "line cb is the same length as line ab", "line ac is the same length as line ab", "angle acb is not a right angle", "angle adb is not a right angle", "triangle acb is an equilateral triangle", "triangle abd is not a right angled triangle", "both of the triangles are slightly different", "the angles at point a the same as points c and d", "the angles at point b are different")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, lines bc and bd are tangents drawn from the same point. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb39_alternate_segment_theorem():
    people = peopleGen()
    num = randint(30, 60)
    true_tuple = ("angles a and e are the same", "angles b and d are the same", "angles c and f are the same", "angles c, b and e add up to 180 degrees", "angles d, f and a add up to 180 degrees", "if you know angles f and a , you can calculate all angles in the triangle in the diagram", "if you know angles d and e, you can calculate all angles in the triangle")
    false_tuple = ("angles a and e are not the same", "angles b and d are not the same", "angles c and f are not the same", "angles c, b and e add up to 360 degrees", "angles d, f and a add up to 90 degrees", "if you know angle f, you can calculate all angles in the triangle in the diagram", "if you know angles e, you can calculate all angles in the triangle")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"In the diagram above, lines bc and bd are tangents drawn from the same point. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="The angle made at the centre of a circle is exactly double the angle at the circumference of the circle from the same two points at the ends of a chord."
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb3_circle_problem1():
    abc = randint(30, 80)
    aoc = abc * 2
    adc = 180 - abc
    answer = [["ABC", abc], ["AOC", aoc], ["ADC",adc]]
    choice = randint(0, len(answer)-1)
    choice2 = choice
    while choice2 == choice:
        choice2 = randint(0, len(answer)-1)
    questionBase = f"A,B,C and D are points on the circumference of the circle in the diagram and O is the centre. Angle {answer[choice][0]} = {answer[choice][1]}\u00B0. Find the value of {answer[choice2][0]}."
    answer = f"{answer[choice2][1]}\u00B0"
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def eb3_circle_problem2():
    abd = randint(30, 80)
    acd = abd
    adf = abd
    aed = 190 - abd
    answer = [["ABD", abd], ["ACD", acd], ["ADF",adf], ["AED",aed]]
    choice = randint(0, len(answer)-1)
    choice2 = choice
    while choice2 == choice:
        choice2 = randint(0, len(answer)-1)
    questionBase = f"A,B,C,D and E are points on the circumference of the circle in the diagram. Line FDG is a tangent and O is the centre. Angle {answer[choice][0]} = {answer[choice][1]}\u00B0. Find the value of {answer[choice2][0]}."
    answer = f"{answer[choice2][1]}\u00B0"
    print(questionBase)
    print(answer)
    diagram, constant, marks = f'/diagrams/gcsemaths/{currentFuncName()}.jpg', None, 1
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,3
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"eb", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec11_congruent_similar():
    people = peopleGen()
    true_tuple = ("congruent means the same size and the same shape", "Similar means the same shape, but a different size", "in a congruent shape, all sides are the same length", "in a similar shape all angles are the same", "both congruent and similar shapes can be reflected or rotated", "similar shapes can be rotated or reflected", "congruent shapes can be rotated or reflected") 
    false_tuple = ("congruent and similar mean the same thing", "congruent means the same shape, but a different size", "similar means exactly the same shape", "in a similar shape, all sides are the same length", "in a congruent shape, all angles are the same but sides are different lengths", "neither congruent nor similar shapes can be reflected or rotated", "similar shapes cannot be rotated or reflected", "congruent shapes cannot be rotated or refelcted")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"{people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,4
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec12_congruent_similar_diagrams():
    people = peopleGen()
    congruent_tuple = ("congruent_circles", "congruent_squares", "congruent_pentagons", "congruent_lightning", "congruent_mouse") 
    similar_tuple = ("similar_circles", "similar_squares", "similar_pentagons", "similar_lightning", "similar_mouse") 
    neither_tuple = ("neither_pentagons", "neither_lightning", "neither_mouse") 
    choice = randint(0,2)
    if choice == 0:
        answer,diagram_choice = "Congruent",f"{congruent_tuple[randint(0,len(congruent_tuple)-1)]}"
    if choice == 1:
        answer,diagram_choice = "Similar",f"{similar_tuple[randint(0,len(similar_tuple)-1)]}"
    if choice == 2:
        answer,diagram_choice = "Neither",f"{neither_tuple[randint(0,len(neither_tuple)-1)]}"
    questionBase = f"In the diagram above, do the shapes appear to be congruent, similar or neither?"
    tip ="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size. This is true even if the congruent or similar shape is rotated or reflected"
    diagram = f'/diagrams/gcsemaths/congruence/ec1_{diagram_choice}.jpg'
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,4
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec13_congruent_triangle_rules():
    people = peopleGen()
    true_tuple = ("two triangles are congruent if three sides are the same", "two triangles are congruent if two angles and a corresponding side match up", "two triangles are congruent if two sides and the angle between them match up", "two triangles are congruent if a right angle, the hypotenuse and one other side all match up", "two triangles are congruent if one rule out of SSS, AAS, SAS and RHS apply", "two triangles can be congruent if they are rotated", "two triangles can be congruent if they are reflected") 
    false_tuple = ("two triangles are congruent if two sides are the same", "two triangles are congruent if all three angles match up", "two triangles are congruent if all three sides are proportional", "two triangles are congruent if they are both right angled triangles", "two triangles are congruent if they are both equilateral", "two triangles cannot be congruent if one of them is rotated", "two triangles cannot be congruent if one of them is reflected") 
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"Congruent means the same shape and size. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, None
    q.marksBase, q.level = 2,4
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec14_congruent_triangle_rules_diagrams():
    people = peopleGen()
    diagram_tuple = (["ec1_congtruent_triangle_sss1","Three sides are the same (SSS)"],["ec1_congtruent_triangle_sss2","Three sides are the same (SSS)"],
                     ["ec1_congtruent_triangle_aas1","Two angles and a corresponding angle are the same (AAS)"],["ec1_congtruent_triangle_aas2","Two angles and a corresponding angle are the same (AAS)"],
                     ["ec1_congtruent_triangle_sas1","Two sides and the angle between them match up (SAS)"],["ec1_congtruent_triangle_sas2","Two sides and the angle between them match up (SAS)"],
                     ["ec1_congtruent_triangle_rhs1","A right angle, the hypotenuse and one other side all match up (RHS)"],["ec1_congtruent_triangle_rhs2","A right angle, the hypotenuse and one other side all match up (RHS)"])
    choice = randint(0, len(diagram_tuple)-1)
    answer,diagram_choice = diagram_tuple[choice][1],diagram_tuple[choice][0]
    questionBase = f"The triangles above are congruent. What condition proves that this is the case?"
    tip ="A triangle is congruent if: three sides are the same OR two angles and a corresponding side match up OR two sides and the angle between them match up OR a right angle, the hypotenuse and one oter side all match up."
    diagram = f'/diagrams/gcsemaths/congruence/{diagram_choice}.jpg'
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 2,4
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec21_similar_congruent():
    people = peopleGen()
    true_tuple = ("congruent means the same size and the same shape", "Similar means the same shape, but a different size", "in a congruent shape, all sides are the same length", "in a similar shape all angles are the same", "both congruent and similar shapes can be reflected or rotated", "similar shapes can be rotated or reflected", "congruent shapes can be rotated or reflected") 
    false_tuple = ("congruent and similar mean the same thing", "congruent means the same shape, but a different size", "similar means exactly the same shape", "in a similar shape, all sides are the same length", "in a congruent shape, all angles are the same but sides are different lengths", "neither congruent nor similar shapes can be reflected or rotated", "similar shapes cannot be rotated or reflected", "congruent shapes cannot be rotated or refelcted")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"{people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.marksBase, q.level = 1,4
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    q.tip ="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size"
    return q.returnAll()

def ec22_similar_congruent_diagrams():
    people = peopleGen()
    congruent_tuple = ("congruent_circles", "congruent_squares", "congruent_pentagons", "congruent_lightning", "congruent_mouse") 
    similar_tuple = ("similar_circles", "similar_squares", "similar_pentagons", "similar_lightning", "similar_mouse") 
    neither_tuple = ("neither_pentagons", "neither_lightning", "neither_mouse") 
    choice = randint(0,2)
    if choice == 0:
        answer,diagram_choice = "Congruent",f"{congruent_tuple[randint(0,len(congruent_tuple)-1)]}"
    if choice == 1:
        answer,diagram_choice = "Similar",f"{similar_tuple[randint(0,len(similar_tuple)-1)]}"
    if choice == 2:
        answer,diagram_choice = "Neither",f"{neither_tuple[randint(0,len(neither_tuple)-1)]}"
    questionBase = f"In the diagram above, do the shapes appear to be congruent, similar or neither?"
    tip ="Congruence means two shapes are the same size and shape. Similarity means that two shapes are the same shape, containing the same angles, but a different size. This is true even if the congruent or similar shape is rotated or reflected"
    diagram = f'/diagrams/gcsemaths/congruence/ec1_{diagram_choice}.jpg'
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, diagram, tip
    q.marksBase, q.level = 2,4
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec23_similar_triangle_rules():
    people = peopleGen()
    true_tuple = ("two triangles are similar if all three angles match up", "all sides in one triangle are proportionalto the other", "any two sides are proportional and the angle between them is the same","two triangles can be similar if they are also rotated", "two triangles can be similar if they are also reflected") 
    false_tuple = ("two triangles are similar if all two angles match up", "all sides are the same length in both triangles", "any two sides are proportional","two triangles cannot be similar if they are also rotated", "two triangles cannot be similar if they are also reflected") 
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"Similarity means the same shape, but different size. {people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    tip ="Similarity means shapes are exactly the same shape, but can be different sizes as well as rotated or reflected."
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, None, tip
    q.marksBase, q.level = 2,4
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec25_all_angles_match_up():
    a = randint(30, 50)
    b = randint(40, 60)
    c = 180 - a - b
    questionBase = f"In the diagram above, all angles a are {a} degrees, all angles b are {b} degrees and all angles c are {c} degrees. Are these triangles similar, congruent or neither?"
    answer = "Similar"
    diagram = f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg'
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, diagram, tip
    q.marksBase, q.level = 1,4
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec26_all_sides_match_up():
    a = randint(8, 10)
    b = randint(6, 7)
    c = randint(3,5)
    y = a * 2
    x = b * 2
    z = c * 2
    questionBase = f"In the smaller triangle above, side a is {a}cm, side b is {b}cm and side c is {c}cm. In the larger triangle, side y is {y}cm, side x is {x}cm and side z is {z}cm. Are these triangl similar, congruent or neither?"
    answer = "Similar"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg', None
    q.marksBase, q.level = 1,6
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ec27_two_sides_one_angle():
    n = randint(20,50)
    a = randint(15, 20)
    b = randint(10, 14)
    y = a*2
    x = b*2
    questionBase = f"In both triangles above, angle n is {n} degrees. Side a is {a}cm, side b is {b}cm, side y is {y}cm and side x is {x}cm. Are these triangles similar, congruent, or neither?"
    answer = "Similar"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg', None
    q.marksBase, q.level = 1,6
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec28_all_angles_match_up_proof():
    a = randint(30, 50)
    b = randint(40, 60)
    c = 180 - a - b
    questionBase = f"In the diagram above, all angles a are {a} degrees, all angles b are {b} degrees and all angles c are {c} degrees. How do you know these triangles are similar?"
    answer = "All three angles match up"
    diagram = f'/diagrams/gcsemaths/congruence/ec25_all_angles_match_up.jpg'
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, diagram, None
    q.marksBase, q.level = 1,6
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ec29_all_sides_match_up_proof():
    a = randint(8, 10)
    b = randint(6, 7)
    c = randint(3,5)
    y = a * 2
    x = b * 2
    z = c * 2
    questionBase = f"In the smaller triangle above, side a is {a}cm, side b is {b}cm and side c is {c}cm. In the larger triangle, side y is {y}cm, side x is {x}cm and side z is {z}cm. How do you know these triangles are similar?"
    answer = "All three sides are proprtional"
    diagram = f'/diagrams/gcsemaths/congruence/ec26_all_sides_match_up.jpg'
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, diagram, None
    q.marksBase, q.level = 1,6
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec210_two_sides_one_angle_proof():
    n = randint(20,50)
    a = randint(15, 20)
    b = randint(10, 14)
    y = a*2
    x = b*2
    questionBase = f"In both triangles above, angle n is {n} degrees. Side a is {a}cm, side b is {b}cm, side y is {y}cm and side x is {x}cm. How do you know these triangles are similar?"
    answer = "Any two sides are proportional and the angle between them is the same"
    diagram = f'/diagrams/gcsemaths/congruence/ec27_two_sides_one_angle.jpg'
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg', None
    q.marksBase, q.level = 1,6
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec1_prove_congruency1():
    questionBase = "AB and AC are tangents to the circle with centre O and touch the circumference at points C and B. Prove that triangles ABO and ACO are congruent."
    answer = "Sides OB and OC are the same length as they are both radii. Both triangles have a right angle because the radii meet tangents AB and AC at right angles. OA is the hypotenuse of both triangles. Therefore, both triangles have a right angle, a matching hypotenuse and one other matching side. the RHS rule holds and triangles ABO and ACO are congruent."
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg', None
    q.marksBase, q.level = 3,7
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec1_prove_congruency2():
    questionBase = "Prove that triangles ABD and BCD are congruent."
    answer = "Side BD is the same in both triangles. Angles DAB and DCB are the same im both triangles, because opposite angles in a parallelogram are the same. Angles ABD and CBD are the same because they are made from an angle which is bisected by line BD. ADB and CDB are likewise the same. Therefore, SSS, AAS and SAS rule are all true"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg', None
    q.marksBase, q.level = 3,7
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ec2_prove_similarity1():
    questionBase = "Prove that triangles ABD and AED are similar."
    answer = "Angles ABC and ADE are alternate angles. BCA and AED are also alternate angles. Third angle in each triangle around point A will be 180 minus the other two angles. Therefore all the angles match up and the triangles are similar"    
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg', None
    q.marksBase, q.level = 2,6
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ec2_use_similarity1():
    pronoun, people = completePeopleGen()
    action = ("lying down", "rolling around", "pretending to swim")
    place = ("sea", "park", "houses of parliament", "antarctic", "deasert", "shopping centre")
    object1 = ("rather tall cactus", "rose bush", "rather large dog", "statue of David Beckham", "large ice cream stand", "rather large kebab van", "rock", "large cabage")
    object1height = randint(2, 8)
    object1dist = randint(10, 20)
    object2 = ("lighthouse", "block of flats", "decorative column", "flag pole", "helter skelter", "dinosaur skeleton")
    object2dist = randint(25, 40)
    object2height = (object2dist / object1dist) * object1height
    action = action[randint(0,len(action)-1)]
    place = place[randint(0,len(place)-1)]
    object1 = object1[randint(0,len(object1)-1)]
    object2 = object2[randint(0,len(object2)-1)]
    
    questionBase = f"The diagram above shows {people} {action} in the {place}. Currently, {pronoun} is {object1dist}m (length Y) from a {object1} at A, the top of which is {object1height}m above the ground. There is a {object2} {object2dist}m (length Y) from {people} that is directly behind the {object1}. To them, the top of the {object2} is in line with the {object1}. Find the height of the {object2} (length B)?"
    answer = f"{round(object2height, 2)}m"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg', None
    q.marksBase, q.level = 2,6
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ec2_use_similarity2():
    de = randint(15, 20)
    bc = randint(8, 12)
    ab = randint(17, 23)
    ad = round(de/bc*ab, 2)
    lengths = ((de,"DE"),(bc,"BC"),(ab,"AB"),(ad,"AD"))
    choices = []
    num = randint(0, len(lengths)-1)
    for i in range(len(lengths)):
        while num in choices:
            num = randint(0, len(lengths)-1)
        choices.append(num)
    questionBase =f"In the diagram above: {lengths[choices[0]][1]} = {lengths[choices[0]][0]}cm, {lengths[choices[1]][1]} = {lengths[choices[1]][0]}cm and {lengths[choices[2]][1]} = {lengths[choices[2]][0]}cm. Find the length of {lengths[choices[3]][1]}."
    answer =f"{lengths[choices[3]][0]}cm"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint = questionBase, answer, f'/diagrams/gcsemaths/congruence/{currentFuncName()}.jpg', None
    q.marksBase, q.level = 2,6
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ec", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()



def ed10_area_triangle_quadrilateral_formulas11():
    formulas = (("triangle", "\u00bd \u00d7 base \u00d7 height OR \u00bdab sin (angle between a and b)"),
                ("paralellogram", "base \u00d7 height"),
                ("trapezium", "\u00bd ( top + base ) \u00d7 height"))
    choice = randint(0, len(formulas)-1)
    if randint(0,1) == 0:
        questionBase = f"What is the formula for the area of a {formulas[choice][0]}?"
        answer = f"{formulas[choice][1]}"
    else:
        questionBase = f"The following formula will find the area for which shape: {formulas[choice][1]}"
        answer = f"{formulas[choice][0]}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ed11_area_triangles13():
    base = randint(4,12)
    height = randint(4,12)
    area = 0.5*base*height
    questionBase = f"The triangle in the diagram (not to scale) has a base of {base}cm and a height of {height}cm. Find the area."
    answer = f"{area}cm\u00b2"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    q.piclink = triangle()
    return q.returnAll()

def ed12_area_parallelogram13():
    base = randint(4,12)
    height = randint(4,12)
    area = base*height
    questionBase = f"The parallelogram in the diagram has a base of {base}cm and a height of {height}cm. Find the area."
    answer = f"{area}cm\u00b2"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    q.piclink = parallelogram()
    return q.returnAll()
    
def ed13_area_trapezium23():
    a = randint(3, 12)
    b = randint(3, 12)
    while b == a: b = randint(3, 12)
    h = randint(3, 10)
    area = 0.5*(a+b) * h
    questionBase = f"The trapezium in the diagram has a base of {b}cm and a height of {h}cm. Find the area."
    answer = f"{area}cm\u00b2"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    q.piclink = trapezium()
    return q.returnAll()
    
def ed14_area_triangles23():
    base = randint(4,12)
    height = randint(4,12)
    area = 0.5*base*height
    values = (("base", base, "cm"),("height", height, "cm"),("area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)    
    questionBase = f"The triangle in the diagram has a {values[choices[0]][0]} of {values[choices[0]][1]}{values[choices[0]][2]} and a {values[choices[1]][0]} of {values[choices[1]][1]}{values[choices[1]][2]}. Find the {values[choices[2]][0]}."
    answer = f"{values[choices[2]][1]}{values[choices[2]][2]}"
    
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    q.piclink = triangle()
    return q.returnAll()
    
def ed15_area_parallelogram24():
    base = randint(4,12)
    height = randint(4,12)
    area = base*height
    values = (("base", base, "cm"),("height", height, "cm"),("area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = f"The parallelogram in the diagram has a {values[choices[0]][0]} of {values[choices[0]][1]}{values[choices[0]][2]} and a {values[choices[1]][0]} of {values[choices[1]][1]}{values[choices[1]][2]}. Find the {values[choices[2]][0]}."
    answer = f"{values[choices[2]][1]}{values[choices[2]][2]}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    q.piclink = parallelogram()
    return q.returnAll()

def ed16_area_trapezium24():
    level = currentFuncName()[-1]
    a = randint(3, 8)
    b = randint(5, 12)
    while b == a: b = randint(3, 12)
    h = randint(3, 10)
    area = 0.5*(a+b) * h
    values = (("the top length", a, "cm"),("the bottom length",b, "cm"),("height",h, "cm"),("the area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = f"In the trapezium above, {values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]}, {values[choices[1]][0]} = {values[choices[1]][1]}{values[choices[1]][2]} and  {values[choices[2]][0]} = {values[choices[2]][1]}{values[choices[2]][2]}. Find the {values[choices[3]][0]}."
    answer = f"{values[choices[3]][1]}{values[choices[3]][2]}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase = questionBase, answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    q.piclink = trapezium()
    return q.returnAll()

def ed17_area_trapezium_problem25():
    level = currentFuncName()[-1]
    x = randint(3,9)
    area = x * x * 2
    values = (("x", x, "cm"),("the area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = f"The shape above shows a square with sides of length x cm drawn inside an isosceles trapezium. The base of the trapezium is three times as long as one side of the square. If {values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]}, find the value of {values[choices[1]][0]}."
    answer = f"{values[choices[1]][1]}{values[choices[1]][2]}"
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/{name}.jpg', None
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram = questionBase, answer, diagram
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    q.piclink = parallelogram()
    return q.returnAll()


def ed18_area_triangle_rectangle24():
    level = currentFuncName()[-1]
    h = randint(3,8)
    b = randint(8, 20)
    area_tri = 0.5*h*b
    y = randint(3, 10)
    x = round(area_tri / y, 2)
    values = (("h", h), ("b", b), ("y", y), ("x", x))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = f"The triangle and rectangle above have the same area. {values[choices[0]][0]} = {values[choices[0]][1]}cm, {values[choices[1]][0]} = {values[choices[1]][1]}cm and {values[choices[2]][0]} = {values[choices[2]][1]}cm. Find the value of {values[choices[3]][0]}"
    answer = f"{values[choices[3]][1]}cm"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, diagram = questionBase, answer, f'/diagrams/gcsemaths/area_volume/{name}.jpg'
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    q.piclink = parallelogram()
    return q.returnAll()
   
def list_mangle(values):
    order, num = [], randint(0, len(values)-1)
    for i in range(len(values)):
        while num in order:
            num = randint(0, len(values)-1)
        order.append(num)
    return order   

def ed20_circumference_radius_and_diameter_12():
    values = (("a", "circumference"),("b","radius"),("c","diameter"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][0]} represent?", f"{values[choice][1]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][1]}?", f"{values[choice][0]}"
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/{name}.jpg', None
    tip = "The circumference is the outside of the circle. The radius is a line from the centre of the circle to the circumference. The diameter is the line which passes through the middle of a circle and touches opposide sides of the circumference. It is like two radi going in opposite directions."
    video, website = None, "https://www.emathzone.com/tutorials/geometry/the-circle-and-parts-of-a-circle.html"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint, q.website = questionBase, answer, diagram, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ed21_formulas_for_area_circumference_arcs_sectors_and_segments13():
    formulas = (("the area of a circle", "\u03c0r\u00b2"),("the circumference of a circle","2\u03c0r or \u03c0d"),("the area of a sector","(sector angle \u00f7 360) \u00d7 area of circle"),("the length of an arc","(arc angle \u00f7 360) \u00d7 circumference"),("area of a segment","area of sector - (\u00bdr\u00b2sin(angle of sector"))
    choice = randint(0, len(formulas)-1)
    if randint(0,1) == 0:
        questionBase = f"What is the formula for {formulas[choice][0]}?"
        answer = f"{formulas[choice][1]}"
    else:
        questionBase = f"The following formula will find the area for what: {formulas[choice][1]}"
        answer = f"{formulas[choice][0]}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.hint, q.website = questionBase, answer, None, None, None
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ed22_area_of_a_circle_23():
    pi = 3.1415835898
    b = randint(2,10)
    c = b*2
    area = round(pi * b * b, 2)
    values = (("b", b, "cm"),("c",c,"cm"),("the area",area,"cm\u00b2"))
    order = list_mangle(values)
    questionBase = f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}. Find {values[order[1]][0]}."
    answer = f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}"
    print(questionBase)
    print(answer)
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/ed20_circumference_radius_and_diameter_12.jpg', "\u03c0 = 3.14159"
    tip = "Area of a circle = \u03c0r\u00b2."
    video, website = None, "https://www.mathsisfun.com/geometry/circle-area.html"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ed23_circumference_of_a_circle_23():
    pi = 3.1415835898
    b = randint(2,10)
    c = b*2
    circumference = round(pi * 2 * b, 2)
    values = (("b", b, "cm"),("c",c,"cm"),("the circumference",circumference,"cm"))
    order = list_mangle(values)
    questionBase = f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}. Find {values[order[1]][0]}."
    answer = f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}"
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/ed20_circumference_radius_and_diameter_12.jpg', "\u03c0 = 3.14159"
    tip = "Circumference of a circle = 2\u03c0r OR \u03c0d."
    video, website = None, "https://www.wikihow.com/Calculate-the-Circumference-of-a-Circle"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ed24_area_and_circumference_23():
    pi = 3.1415835898
    b = randint(2,10)
    c = b*2
    area = round(pi * b * b, 2)
    circumference = round(pi * 2 * b, 2)
    if randint(0,1) == 0:
        values = (("b", b, "cm"),("c",c,"cm"),("the circumference",circumference,"cm"))
        order = list_mangle(values)
        questionBase = f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}. Find {values[order[1]][0]}."
        answer = f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}"
    else:
        values = (("b", b, "cm"),("c",c,"cm"),("the area",area,"cm\u00b2"))
        order = list_mangle(values)
        questionBase = f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}. Find {values[order[1]][0]}."
        answer = f"{values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}"
    diagram, constant = f'/diagrams/gcsemaths/area_volume/ed20_circumference_radius_and_diameter_12.jpg', "\u03c0 = 3.14159"
    tip = "Area of a circle = \u03c0r\u00b2. Circumference of a circle = 2\u03c0r OR \u03c0d."
    video, website = None, None
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

       

def ed25_arcs_and_sectors_12():
    values = (("a", "major arc"),("b","minor arc"),("c","minor sector"),("d","major sector"),("x","angle of minor sector"),("y","angle of major sector"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][0]} represent?", f"{values[choice][1]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][1]}?", f"{values[choice][0]}"
    print(questionBase)
    print(answer)
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/{name}.jpg', "\u03c0 = 3.14159"
    tip = "A major arc is a larger part of a circumference. A minor arc is the smaller part. A major sector is the larger area of a circle which is split by two radi. A minor sector is the smaller part."
    video, website = None, None
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ed26_segments_12():              
    values = (("r", "radius"),("e","chord"),("f","segment"),("h","distance from centre to chord"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][0]} represent?", f"{values[choice][1]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][1]}?", f"{values[choice][0]}"
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/{name}.jpg', "\u03c0 = 3.14159"
    pre, preans, marks, level = None, None, name[-2],name[-1]
    tip = "A chord is a line which contacts both parts of the circumference but does not pass through the centre. A segment is a part of a cirle divided by a chord."
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

   
def ed27_segments_arcs_and_sectors13():
    values = (("a", "major arc"),("b","minor arc"),("c","minor sector"),("d","major sector"),("e","chord"),("f","segment"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][0]} represent?", f"{values[choice][1]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][1]}?", f"{values[choice][0]}"
    print(questionBase)
    print(answer)
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/{name}.jpg', "\u03c0 = 3.14159"
    tip = "A chord is a line which contacts both parts of the circumference but does not pass through the centre. A segment is a part of a cirle divided by a chord."
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, None
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


    
def ed28_area_of_a_sector26():
    x = randint(1,179)
    y = 360 - x
    area = randint(5,50)
    minor_sector = round(x/360*area, 2)
    major_sector = round(y/360*area, 2)
    values = (("the minor sector's area",minor_sector,"cm\u00b2"),("the major sector's area", major_sector,"cm\u00b2" ))
    order = list_mangle(values)
    questionBase = f"On the diagram (not to scale), x = {x}\u00b0, area = {area}cm\u00b2. Find {values[order[0]][0]}."
    answer = f"{values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}"
    diagram, constant = f'/diagrams/gcsemaths/area_volume/ed25_arcs_and_sectors_12.jpg', "\u03c0 = 3.14159"
    tip = "The area of a sector = (angle of sector/360) x area of the circle."
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/1"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()




def ed29_length_of_arc26():
    x = randint(1,179)
    y = 360 - x
    circumference = randint(5,50)
    minor_arc = round(x/360*circumference, 2)
    major_arc = round(y/360*circumference, 2)
    values = (("the minor arc's length",minor_arc,"cm"),("the major arc's length", major_arc,"cm" ))
    order = list_mangle(values)
    questionBase = f"On the diagram (not to scale), x = {x}\u00b0, the circumference = {circumference}cm. Find {values[order[0]][0]}."
    answer = f"{values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}"
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/ed25_arcs_and_sectors_12.jpg', "\u03c0 = 3.14159"
    tip = "The length of an arc = (angle of sector/360) x circumference."
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/2"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ed210_area_of_segments37():
    r = randint(2,12)
    x = randint(1,110)
    e = randint(2,12)
    segment_area = round((x/360 * 3.14159 * r * r) - 0.5 * r * r * math.sin(math.radians(x)),2)
    values = (("x", x, "\u00b0"),("r",r,"cm"),("e",e,"cm"),("the area of the segment", segment_area,"cm\u00b2" ))
    order = list_mangle(values)
    questionBase = f"On the diagram (not to scale), {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]}, {values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]} and {values[order[2]][0]} = {values[order[2]][1]}{values[order[2]][2]}. Find {values[order[3]][0]}."
    answer = f"{values[order[3]][0]} = {values[order[3]][1]}{values[order[3]][2]}"
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/ed26_segments_12.jpg', "\u03c0 = 3.14159"
    pre, preans, marks, level = None, None, name[-2],name[-1]
    tip = "The area of a segment = the area of a sector - the area of the triangle made by the two radi and the chord. This triangle = \u00bdr\u00b2sin x."
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/5"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ed211_area_of_pacman26():
    a = randint(2,15)
    x = randint(1,110)
    shaded_area = round((3.14159 * a * a) - (x/360*(3.14159 * a * a)), 2)
    values = (("x", x, "\u00b0"),("a",a,"cm"),("the area of pacman", shaded_area,"cm\u00b2" ))
    order = list_mangle(values)
    questionBase = f"On the diagram, {values[order[0]][0]} = {values[order[0]][1]}{values[order[0]][2]} and {values[order[1]][0]} = {values[order[1]][1]}{values[order[1]][2]}. Find {values[order[2]][0]}."
    answer = f"{values[order[2]][0]} = {values[order[2]][1]}{values[order[2]][2]}"
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/{name}.jpg', "\u03c0 = 3.14159"
    tip = "The area of a sector = (angle of sector/360) x area of the circle. The pacman in the diagram is a major sector."
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/1"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ed212_shape_problem26():
    x = randint(100,160)
    a = randint(3,15)
    area_sector = round((x/360 * 3.14159 * a * a),2)
    length_arc = round((x/360 * 2 * 3.14159 * a), 2)
    area_segment = round((x/360 * 3.14159 * a * a) - 0.5 * a * a * math.sin(math.radians(x)),2)
    perimeter_shape = round((x/360 * 2 * 3.14159 * a) + a + a, 2)
    values = (("area of the sector", area_sector, "cm\u00b2"),("length of the arc",length_arc,"cm"),("area of the segment",area_segment,"cm\u00b2" ),("perimeter of the shape",perimeter_shape,"cm"))
    order = randint(0, len(values)-1)
    questionBase = f"On the diagram, x = {x}\u00b0 and a = {a}cm. Find {values[order][0]}."
    answer = f"{values[order][0]} = {values[order][1]}{values[order][2]}"    
    name = currentFuncName()
    diagram, constant = f'/diagrams/gcsemaths/area_volume/{name}.jpg', "\u03c0 = 3.14159"
    tip = "The perimeter of this shape includes the arc AND the two radii, which are also on the outside of the shape. Feel free to go back a few questions if you need help with the others!"
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/z9hsrdm/revision/1"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ed", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def prism():
    shape_list = ["http://www.k6-geometric-shapes.com/image-files/prism-rectangle-1.jpg",
                  "http://www.clipartkid.com/images/78/3d-rectangular-prism-in-real-life-image-galleries-imagekb-com-kGqhFW-clipart.png",
                  "https://netninja.com/wp-content/uploads/2014/05/toblerone.jpg",
                  "https://ae01.alicdn.com/kf/HTB151mQXODxK1RjSsphq6zHrpXaY/Triangular-color-prism-K9-Optical-Glass-Right-Angle-Reflecting-Triangular-Prism-For-Teaching-Light-Spectrum-Total.jpg",
                  "https://www.software3d.com/JPeg/Prism5.jpg",
                  "https://alchetron.com/cdn/pentagonal-prism-39739ed7-2b34-4eb4-9cab-29561face1d-resize-750.png"
                  "https://i.imgflip.com/2b5qcq.jpg",
                  ]
    return shape_list[randint(0,len(shape_list)-1)]

def cylinder():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.me.me%2Fthe-orange-cylinder-is-here-it-is-orange-and-pillar-19722697.png&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2FFacebook-71403c.png&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.me.me%2FFacebook-We-hate-when-cylinder-5-says-0861e6.png&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F1d%2F48%2F5f%2F1d485fd3db4a92dbe8bd0b5398110fe2.jpg&f=1&nofb=1",
                  "https://i.pinimg.com/564x/d0/05/69/d0056904186322fc43f289160fa30bd1.jpg",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.conservativememes.com%2Fine-joseph-enouys-8-cylinder-48-shot-percussion-revolver-dated-1855-13726561.png&f=1&nofb=1"]
    return shape_list[randint(0,len(shape_list)-1)]

def sphere():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fgame-sphere-tsspherical-https-t-co-jnyuys9da1-11045947.png&f=1&nofb=1",
                  "https://duckduckgo.com/?q=sphere+meme&iar=images&iax=images&ia=images&iai=http%3A%2F%2Fwww.relatably.com%2Fm%2Fimg%2Fspherical-memes%2Fcb0.jpg",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimageproxy.ifcdn.com%2Fcrop%3Ax-20%2Cresize%3A320x%2Ccrop%3Ax800%2Cquality%3A90x75%2Fimages%2F1c6828a88032dee5543cd9ee8d32db05607596b3c99efd04eaa70a64460fe712_1.jpg&f=1&nofb=1",
                  "https://pics.me.me/self-contained-self-supporting-ecological-system-permanently-sealed-within-a-hand-blown-borsilica-11473078.png",
                  "https://pics.me.me/sometimes-its-hard-being-a-sphere-%3Cp%3E-%3Ca-href-https-www-reddit-com-r-surrealmemes-comments-80kxjh-%3Esrc%3C-a%3E-%3C-p%3E-33131160.png",
                  "https://i0.wp.com/142.93.220.71/wp-content/uploads/2019/03/Microwave-Tinfoil-Into-Sphere-Smooth-Ball-Within-Minutes2.jpg",
                  "https://i.pinimg.com/originals/2c/79/b9/2c79b90aafccd9c6ec814dfdcdbe0d34.jpg",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.boredpanda.com%2Fblog%2Fwp-content%2Fuploads%2F2018%2F02%2Fsphere-of-42000-matches-wallacemk-fb18.png&f=1&nofb=1"]
    return shape_list[randint(0,len(shape_list)-1)]

def hemisphere():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.bo7qvXsehd77DPbUbb7GwAAAAA%26pid%3DApi&f=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.3gqUMVoQ9quaXQWZPWRdYwHaEo%26pid%3DApi&f=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.SjdteI3c4F_xKp6m0B1MNQHaHa%26pid%3DApi&f=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.NXmgxl0CctoJK-98Q51nZAHaFT%26pid%3DApi&f=1",
                  "http://www.cs.columbia.edu/CAVE/projects/DiffuseSL/images/hemisphere/Hemisphere.JPG",
                  "http://www.cmspinning.com/images/hemisphere_6_large.jpg"]
    return shape_list[randint(0,len(shape_list)-1)]

def pyramid():
    shape_list = ["https://s.newsweek.com/sites/www.newsweek.com/files/styles/full/public/2018/02/20/gettyimages-918637914.jpg",
                  "https://i2.wp.com/www.trinfinity8.com/wp-content/uploads/2015/12/Pyramid.jpg",
                  "http://supplies.thesmartteacher.com.s3.amazonaws.com/assets/exchange/22118713.jpg",
                  "https://i.stack.imgur.com/ARVST.jpg",
                  "http://2.bp.blogspot.com/-DSqvsmnwWfA/U_o-VpTTH7I/AAAAAAAABKU/KA-uD-nC6eU/s1600/Tetrahedron%2BAlpha.jpg,"
                  "http://etc.usf.edu/clipart/43100/43188/pent1_43188_lg.gif",
                  "https://upload.wikimedia.org/wikipedia/commons/0/02/Pentagonal_pyramid.png",
                  "https://upload.wikimedia.org/wikipedia/commons/2/2a/Hexagonal_pyramid.png",
                  "https://www.det.nsw.edu.au/eppcontent/glossary/app/resource/image/111.png",]
    return shape_list[randint(0,len(shape_list)-1)]


def cone():
    shape_list = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.memecdn.com%2Fconezilla_c_3193391.jpg&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages5.memedroid.com%2Fimages%2FUPLOADED14%2F510ee3b0d7741.jpeg&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fmemecrunch.com%2Fmeme%2F1FXFO%2Fcone-head%2Fimage.png%3Fw%3D400%26c%3D1&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.tTNIoL5vfl9uH36bbsch2wHaKO%26pid%3DApi%26h%3D160&f=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fc0263062.cdn.cloudfiles.rackspacecloud.com%2Fcontent%2Fimages%2Fsized%2Ffunny-fail-meme-traffic-cone_b4e32e0661ac7b6aa236927c8c448bd5_3x2_jpg_600x400_q85.jpg&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.teamjimmyjoe.com%2Fwp-content%2Fuploads%2F2015%2F02%2Fice-cream-missing-cone-you-had-one-job.jpg&f=1&nofb=1",
                  "https://cleanmemes.files.wordpress.com/2014/09/coneofhappiness1.jpg",
                  "https://s-media-cache-ak0.pinimg.com/736x/8d/46/b1/8d46b1f0516922ba248b6650f6152c1f.jpg",
                  "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.freakingnews.com%2Fpictures%2F58500%2FTraffic-Cone-Space-Shuttle--58732.jpg&f=1&nofb=1",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpics.onsizzle.com%2Fthe-sorting-cone-youre-a-hazard-harry-memes-com-youre-3008662.png&f=1&nofb=1"]
                
    return shape_list[randint(0,len(shape_list)-1)]



def frustum():
    shape_list = ["http://etc.usf.edu/clipart/42700/42799/frust-cone5_42799_lg.gif",
                  "http://www.matematicasvisuales.com/images/geometry/desarrollosplanos/cones/frustum5.jpg",
                  "http://etc.usf.edu/clipart/42200/42230/conefrust_42230_lg.gif",
                  "https://qph.fs.quoracdn.net/main-qimg-21afb1a5be952d5c11fc4cf44c1f8ab6-c",
                  "https://qph.fs.quoracdn.net/main-qimg-fc4d439cc7ea5a00d0c11b0a71ed4c11-c",
                  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.AVZoEcJfN9hjfjp5kbCZygHaGR%26pid%3DApi&f=1"]
    return shape_list[randint(0,len(shape_list)-1)]




def ee10_terminology13():
    #vertices, edge, face
    values = (("vertex", "a"),("edge", "b"),("face","c"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"On the diagram above, what does {values[choice][1]} represent?", f"{values[choice][0]}"
    else: questionBase, answer = f"On the diagram above, which letter represents the {values[choice][0]}?", f"{values[choice][1]}"
    diagram, constant = f"/diagrams/gcsemaths/area_volume/ee10_terminology13/{randint(0,3)}.jpg", "\u03c0 = 3.1415835898"
    tip = "Vertices are corners, where two or more edges meet. Edges are the lines in between vertices. Faces are the spaces in between edges. Curved faces are sometimes called surfaces."
    video, website = None, "https://www.mathsisfun.com/geometry/vertices-faces-edges.html"
    piclink = None
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()


def ee11_count_vertices_edges_faces13():
    values = (("cube",8,12,6,("http://memecrunch.com/meme/7WLH/ice-cube/image.png?w=400&c=1","https://ruwix.com/pics/memes/9-rubix-cube-neversolved.jpg","http://img.memecdn.com/don-t-know-if-ice-cube-has-balls-or-ice-cube-and-if-you-kick-him-does-ice-cube-have-crashed-ice_o_842184.jpg","https://pics.onsizzle.com/how-to-solve-a-1x1-rubiks-cube-tag-friends-to-10222173.png")),
               ("cuboid",8,12,6,(",https://i.imgflip.com/3rxwix.jpg","https://www.polyhedra.net/photo/rectangular-prism-01.jpg","https://ecdn.teacherspayteachers.com/thumbitem/3D-Shapes-Real-Life-Objects-Clip-Art-Rectangular-Prisms-4899203-1569632365/original-4899203-1.jpg")),
               ("square based pyramid",5,8,5,("https://i.pinimg.com/originals/a0/4f/26/a04f266a5d216d1ba4d74de0839a3618.jpg", "http://diggingforbones.files.wordpress.com/2012/08/how-the-pyramids.jpg","https://pics.onsizzle.com/my-food-pyramid-kind-of-looks-like-this-8948197.png","https://pics.onsizzle.com/the-great-pyramid-of-giza-contains-enough-stone-to-make-2908513.png", "https://kuulpeeps.com/wp-content/uploads/2018/06/Why-Bloggers-Should-Avoid-MLM-Like-the-Plague.jpg")),
               ("triangular prism",6,9,5,("https://www.procarton.com/wp-content/uploads/2015/02/toblerone_kopf2.jpg", "http://i1.kym-cdn.com/photos/images/facebook/001/191/306/5e8.jpg", "https://images7.memedroid.com/images/UPLOADED845/5aa68390474d5.jpeg", "https://breakbrunch.com/wp-content/uploads/2019/01/funny-meme-picture-1001180142-7.png")),
               ("tetrahedron", 4,6,4,("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthreesixty360.files.wordpress.com%2F2008%2F04%2Fsierpinski_tetrahedron.jpg%3Fw%3D450&f=1&nofb=1", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.stack.imgur.com%2FKWAvA.jpg&f=1&nofb=1")))
    choice = randint(0,len(values)-1)
    thing = ("vertices", "edges","faces")
    thingChoice = randint(0,len(thing)-1)
    questionBase = f"How many {thing[thingChoice]} in a {values[choice][0]}?"
    answer = f"{values[choice][thingChoice+1]} {thing[thingChoice]}"
    print(questionBase)
    print(answer)
    name = currentFuncName()
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Vertices are corners, where two or more edges meet. Edges are the lines in between vertices. Faces are the spaces in between edges. Curved faces are sometimes called surfaces."
    video, website = None, "https://www.mathsisfun.com/geometry/vertices-faces-edges.html"
    q = Question(cf.currentFuncName())
    q.piclink = f"{values[choice][4][randint(0,len(values[choice][4])-1)]}"
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
   

def ee12_surface_area14():
    people = peopleGen()
    true_tuple = ("the surface area is the total area of all faces", "the surface area is the total area of the shape's net", "a net is a 3D shape with each face folded out flat", "if you know area of one of the faces in a cube, you can calculate the whole surface area")
    false_tuple = ("the surface area is the total area of all the faces but, only ones you can directly see", "the surface area is half the total area of the shape's net, because you only see one side", "the surface area of a 3d shape includes the surface area on the inside", "if you know area of one of the faces in any 3d shape, you can calculate the whole surface area")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"{people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area only applies to 3D objects and it's the total area of all the faces when added together."
    video, website, piclink = None, None, None
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

  
def ee13_surface_area_formulas14():
    values = (("sphere", "4\u03c0r\u00b2"),("cone","\u03c0rl + \u03c0r\u00b2"),("cylinder","2\u03c0rh + 2\u03c0r\u00b2"))
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"what is the formula for the surface area of a {values[choice][0]}?", f"{values[choice][1]}"
    else: questionBase, answer = f"The following formula can be used to calculate the surface area of what: {values[choice][1]}?", f"{values[choice][0]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "All formulas in the link below!"
    video, website = None, "https://www.thoughtco.com/surface-area-and-volume-2312247"
    piclink = None
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ee14_surface_area_of_a_sphere25():
    r = randint(1,10)
    area = round(4*3.1415926*r*r, 2)
    questionBase = f"In the sphere above, the radius = {r}cm. Find the surface area."
    answer = f"{area}cm\u00b2"
    name = currentFuncName()
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area of a sphere = 4\u03c0r\u00B2"
    video, website = None, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F61WN2k1l5wL._SL1461_.jpg&f=1&nofb=1"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = sphere()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ee15_surface_area_of_a_cylinder25():
    r = randint(1,10)
    h = randint(1,10)
    area = round(2*3.1415926*r*h + 2*3.1415926*r*r, 2)
    questionBase = f"In the cylinder above, the radius of the cross section = {r}cm and the height is {h}cm. Find the surface area."
    answer = f"{area}cm\u00b2"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area of a cylinder = 2\u03c0rh + 2\u03c0r\u00B2"
    video, website = None, "https://mathopenref.com/cylinderareamain.html"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = cylinder()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    

def ee16_surface_area_of_a_cone25():
    r = randint(1,10)
    l = randint(1,10)
    area = round(3.1415926*r*l + 3.1415926*r*r, 2)
    questionBase = f"In the cone above, the radius of the base = {r}cm and the height of the cone = {l}cm. Find the surface area."
    answer = f"{area}cm\u00b2"
    name = currentFuncName()
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area of a cone = \u03c0rl + \u03c0r\u00B2"
    video, website = None, "https://www.web-formulas.com/Math_Formulas/Geometry_Surface_of_Cone.aspx"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = cone()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ee17_use_surface_area_formula_to_find_an_unknown_value_in_a_sphere25():
    r = randint(1,10)
    area = round(4*3.1415926*r*r, 2)
    values = (("the radius",r, "cm"),("the surface area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = f"In the sphere above, {values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]}. Find {values[choices[1]][0]}."
    answer = f"{values[choices[1]][1]}{values[choices[1]][2]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area of a sphere = 4\u03c0r\u00B2"
    video, website = None, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F61WN2k1l5wL._SL1461_.jpg&f=1&nofb=1"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = sphere()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ee18_use_surface_area_formula_to_find_an_unknown_value_in_a_cyinder25():
    r = randint(1,10)
    h = randint(1,10)
    area = round(2*3.1415926*r*h + 2*3.1415926*r*r, 2)
    values = (("the radius",r, "cm"), ("the height",h,"cm"),("the surface area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = f"In the cylinder above, {values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]} and {values[choices[1]][0]} = {values[choices[1]][1]}{values[choices[1]][2]} Find {values[choices[2]][0]}."
    answer = f"{values[choices[2]][1]}{values[choices[2]][2]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area of a cylinder = 2\u03c0rh + 2\u03c0r\u00B2"
    video, website = None, "https://mathopenref.com/cylinderareamain.html"
    piclink = cylinder()
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = sphere()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
   
def ee19_use_surface_area_formula_to_find_an_unknown_value_in_a_cone25():
    r = randint(1,10)
    l = randint(1,10)
    area = round(3.1415926*r*l + 3.1415926*r*r, 2)
    values = (("radius",r, "cm"), ("length",l,"cm"),("surface area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = f"In the cone above, {values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]} and {values[choices[1]][0]} = {values[choices[1]][1]}{values[choices[1]][2]} Find the {values[choices[2]][0]}."
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area of a cone = \u03c0rl + \u03c0r\u00B2"
    video, website = None, "https://www.web-formulas.com/Math_Formulas/Geometry_Surface_of_Cone.aspx"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = cone()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ee110_problem_hemisphere36():
    r = randint(1,10)
    area = round((4*3.1415926*r*r)/2 + 3.1415926*r*r, 2)
    values = (("the radius",r, "cm"),("the surface area", area, "cm\u00b2"))
    choices = []
    num = randint(0, len(values)-1)
    for i in range(len(values)):
        while num in choices:
            num = randint(0, len(values)-1)
        choices.append(num)
    questionBase = f"In the hemisphere above, {values[choices[0]][0]} = {values[choices[0]][1]}{values[choices[0]][2]}. Find {values[choices[1]][0]}."
    answer = f"{values[choices[1]][1]}{values[choices[1]][2]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "A hemisphere is exactly half of a sphere, and don't forget that a hemisphere also has a flat face. So: 4\u03c02r\u00B2 \u00f7 2 + 2\u03c0r\u00B2. This can be simplified to 3\u03c0r\u00B2"
    video, website = None, "http://mathcentral.uregina.ca/QQ/database/QQ.09.07/h/nicholas4.html"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = hemisphere()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ee20_identify_the_3D_shape13():
    options = ((prism(), "prism"),(sphere(),"sphere"),(pyramid(), "pyramid"),(sphere(),"sphere"),(cone(),"cone"),(frustum(),"frustum"),(hemisphere(),"hemisphere"))
    choice = randint(0,len(options)-1)
    answer = f"{options[choice][1]}"
    questionBase = "What is the name of the 3D shape in the image above?"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area only applies to 3D objects and it's the total area of all the faces when added together."
    video, website, piclink = None, "https://revisionmaths.com/gcse-maths/geometry-and-measures/3d-shapes", f"{options[choice][0]}"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ee21_definitions_of_3D_shapes13():
    people = peopleGen()
    true_tuple = ("a prism is a solid (3D) object which is the same all the way through",
                  "a prism has a constant area of cross section all the way though",
                  "if a prism has a circular cross section, it can be called a cylinder",
                  "a cylinder is a type of prism",
                  "a sphere has a constant radius, wherever you measure it",
                  "if all the sides of a prism are identical squares, it is called a cube",
                  "a pyramid is a shape that goes from a flat base up to a point at the top",
                  "a pyramid's base can be any shape at all",
                  "if a pyramid's base is circular, it is called a cone",
                  "a frustum is left when the top of a cone is cut off parallel to its base")
    false_tuple= ("a prism is a solid (3D) object which isn't always the same all the way through",
                  "the cross section of a prism can change",
                  "a cylinder is not a prism",
                  "any shape with a circular base is a cylinder",
                  "a cube is not a type of prism",
                  "a pyramid is a shape that goes from a flat base up to flat top",
                  "a pyramid's base must be square",
                  "a cone is not a pyramid",
                  "if you cut a cone parallel to its base, a frustum is the smaller cone at the top")
    choice = randint(0,1)
    answer = "Correct" if choice == 1 else "Incorrect"
    statement = true_tuple[randint(0,len(true_tuple)-1)] if answer == "Correct" else false_tuple[randint(0,len(false_tuple)-1)]
    questionBase = f"{people[randint(0,len(people)-1)]} says that {statement}. Is this statement correct or incorrect?"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Surface area only applies to 3D objects and it's the total area of all the faces when added together."
    video, website, piclink = None, None, None
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ee22_volume_formulas13():
    values = (("prism", "cross-sectional area \u00d7 length"),
              ("cylinder","\u03c0r\u00b2 \u00d7 length"),
              ("sphere", "4\u20443\u03c0r\u00b3"),
              ("pyramid", "\u2153 \u00d7 area of base \u00d7 height"),
              ("cone", "\u2153\u03c0r\u00b2h"),
              ("frustum","\u2153\u03c0R\u00b2H - \u2153\u03c0r\u00b2h where R and H are the radius and height of the complete cone and r and h are the radius and height of the smaller cone"),
              ("hemisphere","2\u20443\u03c0r\u00b3"))  
    choice = randint(0,len(values)-1)
    if randint(0,1) == 0 :questionBase, answer = f"what is the formula for the volume of a {values[choice][0]}?", f"{values[choice][1]}"
    else: questionBase, answer = f"The following formula can be used to calculate the surface area of what: {values[choice][1]}?", f"{values[choice][0]}"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "All formulas in the link below!"
    video, website = None, "https://byjus.com/maths/three-dimensional-shapes/"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
'''
Volume of:
prisms
spheres
pyramids
cones
frustrums
hemispheres

rates of flow

problems'''

def ee23_volume_of_a_prism_with_cross_sectional_area_known13():
    area = randint(8,80)
    length = randint(5,10)
    volume = area * length
    questionBase = f"In the diagram above (not to scale) the cross sectional area of the prism is {area}cm\u00b2 and the length is {length}cm. Find the volume of the prism"
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Volume of a prism = cross sectional area \u00d7 length"
    video, website = None, "https://www.wikihow.com/Calculate-the-Volume-of-a-Prism"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = prism()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def ee24_volume_of_a_sphere_with_radius_known25():
    r = randint(8,80)
    volume = round(4/3 * 3.14159 * r * r * r, 2)
    questionBase = f"In the diagram above (not to scale) the radius of the sphere is {r}cm. Find the volume of the sphere."
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Volume of a sphere = 4\u20443\u03c0r\u00b3"
    video, website = None, "https://www.onlinemathlearning.com/volume-of-a-sphere.html"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = sphere()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ee25_volume_of_a_pyramid_with_base_and_height_known25():
    base = randint(10,40)
    height = randint(5,20)
    volume = round(1/3 * base * height, 2)
    questionBase = f"In the diagram above (not to scale) the verticle height of the pyramid is {height}cm and area of the base is {base}cm\u00b2. Find the volume of the pyramid."
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "volume of pyramid = \u2153 \u00d7 area of base \u00d7 height"
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/zcnb8mn/revision/6"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = pyramid()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ee25_volume_of_a_cone_with_radius_and_height_known25():
    r = randint(5,20)
    height = randint(5,20)
    volume = round(1/3 * (3.1415 * r * r) * height, 2)
    questionBase = f"In the diagram above (not to scale) the verticle height of the cone is {height}cm and radius the base is {r}cm\u00b2. Find the volume of the pyramid."
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "volume of pyramid = \u2153 \u00d7 area of base \u00d7 height"
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/zcnb8mn/revision/6"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = cone()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ee26_volume_of_a_frustrum_with_volume_of_original_cone_known46():
    oc = randint(700, 1000)
    r = randint(5,15)
    height = randint(12,30)
    volume = round(oc - (1/3 * (3.1415 * r * r) * height), 2)
    questionBase = f"In the diagram above (not to scale) the volume of the original cone is {oc}cm\u00b3, the height of the removed cone is {height}cm and radius of the base of the removed cone is {r}cm. Find the volume of the pyramid."
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "volume of frustum of a cone = volume of original cone - volume of removed cone (volume of cone = \u2153 \u00d7 \u03c0r\u00d7\u00b2 \u00d7 height)"
    video, website = None, "https://www.bbc.co.uk/bitesize/guides/zcnb8mn/revision/6"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = cone()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def ee27_volume_of_a_hemisphere_with_radius_known35():
    r = randint(8,80)
    volume = round(2/3 * 3.14159 * r * r * r, 2)
    questionBase = f"In the diagram above (not to scale) the radius of the hemisphere is {r}cm. Find the volume of the hemispheresphere."
    answer = f"{volume} cm\u00b3"
    diagram, constant = None, "\u03c0 = 3.14159"
    tip = "Volume of a sphere = \u2154\u03c0r\u00b3"
    video, website = None, "https://www.onlinemathlearning.com/volume-of-a-sphere.html"
    q = Question(cf.currentFuncName())
    q.questionBase, q.answerBase, q.diagram, q.constant, q.hint, q.website = questionBase, answer, diagram, constant, tip, website
    q.piclink = sphere()
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ee", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()




'''
ea1 = basics
ea2 = parallel lines
ea3 = geometry problems

eb1 = polygons
eb2 = triangles and quadrilaterals
eb3 = circle geometry

ec1 = congruent shapes
ec2 = similar shapes
ec3 = the four transformations
ec4 = MORE ENLARGEMENTS AND PROJECTIONS

ed1 = area of trianges and quadrilaterals 
ed2 = area of circles

ee1 = 3D shapes and surface area
vertices 
faces 
edges 3

surface area 5
surface area = total area of all faces, area of net, 3d shape folded out flat, 
formulas for surface area of spheres cones and cylinders. 
find sphere
find cylinder
find cone

problem = surface of hemisphere


ee2 = 3D shapes and volume
definition
formulas

Volume
prisms
spheres
pyramids
cones
frustrums
hemispheres


rates of flow

problems



ef1 = Triangle construction
ef2 = Loci and construction

eg1 = bearings
'''

