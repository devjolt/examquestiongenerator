
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


'''
PASTE ENTIRE WHATEVER_LOGIC.PY FILE HERE vvvvvvv!
'''


'''
PASTE ENTIRE WHATEVER_LOGIC.PY FILE HERE ^^^^^^^!
'''
#change the "e" in the next bit to the appropriate letter
module_list = moduleListGen("e", 0, 1)

list_of_paths = []
for thing in module_list:
    list_of_paths.append(f'''path("{thing}/", SOURCE_FILE_FOR_VIEWS_HERE!!!!.{thing}, name = "{thing}"),''')
print(list_of_paths)

list_of_defs = []
for thing in module_list:
    list_of_defs.append(f"def {thing}(request):")
print(list_of_defs)

list_of_urls = []
for thing in module_list:
    thingName = thing.replace("_", " ")
    thingName = thingName[5:-2] + f" (level {thingName[-1]})"
    list_of_urls.append(f'''<a class="dropdown-item" href="{thing}/" target="_blank">{thingName}</a>''')
print(list_of_urls)


#Copy and paste list printed on terminal into appropriate file, delete ', etc to format it and voila!

