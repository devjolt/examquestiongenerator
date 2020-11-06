from django.shortcuts import render
from random import randint
from fractions import Fraction
from decimal import Decimal
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
    return cf.moduleListGen(list_callable_functions(), 'a', 0, 1)

def module_path():
    return '/gcsemaths/a_number/'

def abaa_add_unit_11():
    q = cf.QuestionInteger(cf.currentFuncName(),2,9,10,99,'+',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abab_add_sub_integers_11():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,110,999,'-',1)
    q.op = q.opSetup(0,1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abac_sub_integers_11():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,110,999,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abad_multiply_unit13():
    q = cf.QuestionInteger(cf.currentFuncName(),2,9,10,99,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abae_subtract_unit13():
    q = cf.QuestionInteger(cf.currentFuncName(),2,9,10,99,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abaf_add_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,100,999,'+',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def abag_subtract_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,100,999,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abah_multiply_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),100,999,10,99,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abai_divide_unit13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,2,9,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abaj_divide_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),100,999,10,30,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abak_negative_add_unit13():
    q = cf.QuestionInteger(cf.currentFuncName(),-9,-1,10,100,'+',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abal_negative_add_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),100,999,-99,10,'+',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abam_negative_subtract_unit13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,100,-9,-2,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def aban_negative_subtract_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),100,999,-99,-10,'-',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abao_negative_add_sub_integers13(): 
    q = cf.QuestionInteger(cf.currentFuncName(),-999,999,-99,99,'-',1)
    q.op = q.opSetup(0,1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abap_negative_multiply_unit13():
    q = cf.QuestionInteger(cf.currentFuncName(),2,9,-99,-10,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abaq_negative_multiply_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,-999,-10,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abar_negative_divide_unit13():
    q = cf.QuestionInteger(cf.currentFuncName(),-99,-10,2,9,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abas_negative_divide_tens_hundreds13():
    q = cf.QuestionInteger(cf.currentFuncName(),-999,-100,10,99,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abat_multiply_divide_random13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,99,100,999,'-',1)
    q.op = q.opSetup(2,3)
    q.answerBase = q.answer
    if q.op == '/': q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abau_multiply_integers13():
    q = cf.QuestionInteger(cf.currentFuncName(),-999,-100,10,99,'*',1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abav_divide_integers13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,100,10,100,'/',1)
    q.answerBase = f"{q.x//q.y} remainder {q.x % q.y}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abaw_random_integers13():
    q = cf.QuestionInteger(cf.currentFuncName(),10,100,10,100,'/',1)
    q.op = q.opSetup(0,3)
    q.answerBase = q.answer
    if q.op == '/': q.answerBase = f"{round(eval(q.questionBase))} remainder {q.x % q.y}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abba_add_sub_decimals24():
    q = cf.QuestionDecimal(cf.currentFuncName(),0,0,0,0,'-',1)
    q.op = q.opSetup(0,1)
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abbb_multiply_decimals24():
    q = cf.QuestionDecimal(cf.currentFuncName(),0,0,0,0,'*',1)
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abbc_divide_decimals24():
    q = cf.QuestionDecimal(cf.currentFuncName(),0,0,0,0,'/',1)
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
    
def abbd_random_decimals23():
    q = cf.QuestionDecimal(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,3)
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abca_add_sub_fractions24():
    q = cf.QuestionFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abcb_multiply_fractions24():
    q = cf.QuestionFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abcc_divide_fractions24():
    q = cf.QuestionFraction(cf.currentFuncName(),0,0,0,0,'/',1)
    q.divideQuestionAnswer()
    q.answerBase = q.answer
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abcd_random_fractions24():
    q = cf.QuestionFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,3)
    if q.op =='/': q.divideQuestionAnswer()
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abce_add_sub_mixed_fractions24():
    q = cf.QuestionMixedFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abcf_multiply_mixed_fractions24():
    q = cf.QuestionMixedFraction(cf.currentFuncName(),0,0,0,0,'*',1)
    q.opSetup(0,1)
    q.questionBase += " (Give your answer in decimal form)"
    q.answerBase = str(round(float(q.answer), 2))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abce_decimal_as_fraction24():
    q = cf.Question(cf.currentFuncName())
    denOptions = [2,4,5,6,8,10,12,15,20]
    den = denOptions[randint(0,len(denOptions)-1)]
    num = randint(1,den-1)
    decimal = round(num/den, 5)
    q.questionBase = (f"Write {decimal} as a fraction")
    q.answerBase = (Fraction(f"{num}/{den}"))
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()

def abcf_fraction_as_decimal24():
    q = cf.Question(cf.currentFuncName())
    denOptions = [2,4,5,6,8,10,12,15,20]
    den = denOptions[randint(0,len(denOptions)-1)]
    num = randint(1,den-1)
    decimal = round(num/den, 5)
    frac = Fraction(f"{num}/{den}")
    q.questionBase = (f"Write {frac} as a decimal")
    q.answerBase = f"{decimal}"
    q.previousQ, q.nextQ = cf.previousNext(list_callable_functions(),"ab", 0, 2, cf.currentFuncName(), module_path())
    return q.returnAll()
