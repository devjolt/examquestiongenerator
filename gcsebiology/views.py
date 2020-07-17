from django.shortcuts import render

def home(request):

    questionBase = "hello"
    question1 = "you"
    question2 = "and you"
    answer1 = "yo"
    answer2 = "and yo"
    nextPage = ""
    prevPage = ""


    return render(request,"questionAnswerButtons.html", {"questionBase":questionBase, "question1":question1, "question2":question2, "answer1":answer1, "answer2":answer2})

def experiment(request):
    return render(request,"questionAnswer.html")