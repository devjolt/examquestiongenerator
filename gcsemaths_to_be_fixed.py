#from algebra_logic.py
def surd_rule_2a7():
    char2 = randint(2,12)
    char1 = char2*randint(1,10)
    questionBase = "Simplify:"
    pre = f'''
    \u221A{char1}
    \u2500\u2500\u2500
    \u221A{char2}'''
    if type (char1) == int:
        if type(char2) == int:
            if char1%char2==0:
                if ((char1/char2)**0.5)%1==0:
                    answer = f"{int((char1/char2)**0.5)}"
                else: answer = f"\u221A{int(char1/char2)}"
            else:answer =  f"\u221A({char1}\u2044{char2})"
        elif type(char2) == str:
            answer = f"\u221A({char1}\u2044{char2})"
    elif type (char1) == str:
        if type (char2) == str:
            if ord(char1) == ord(char2): answer = 1
            else: answer = f"\u221A({char1}\u2044{char2})"
        elif type(char2) == int:
            answer = f"\u221A({char1}\u2044{char2})"
    diagram, constant, marks = None, None, 1
    previousQ, nextQ = previousNext("surd", 0, 4, currentFuncName())
    return previousQ, nextQ, diagram, constant, questionBase, answer, marks, None, None, None, None, None, None, None, None, None,None, None, None, pre, None
#from algebra_roots_surds.py
    def surd_rule_2a7(request):
    previousQ, nextQ, diagram, constant, questionBase, answer, marks, None, None, None, None, None, None,None, None, None, None, None, None, pre, None = eval(f"algebra_logic.{currentFuncName()}()")
    return render(request, "questionAnswerButtons2.html", allArguments(previousQ, nextQ, diagram, constant, questionBase, answer, marks, None, None, None, None, None, None,None, None, None, None, None, None, pre, None))
    