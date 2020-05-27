from django.shortcuts import render, redirect
from django.utils.translation import activate

myLanguage  = "en"
currentPage = "index"

# Create your views here.
def index(request):
    global currentPage
    currentPage = "index"
    pageStatus = ""
    if currentPage == "index":
        pageStatus = "active"
    else:
        pageStatus = ""

    context = {
        'homepagestatus' : pageStatus,
    }
    activate(myLanguage)
    return render(request, 'index.html', context)

def english(request):
    global myLanguage
    myLanguage = "en"
    activate(myLanguage)
    return redirect(currentPage)

def french(request):
    global myLanguage
    myLanguage = "fr"
    activate(myLanguage)
    return redirect(currentPage)

def ourProgram(request):
    global currentPage
    currentPage = "our_program"
    pageStatus = ""
    if currentPage == "our_program":
        pageStatus = "active"
    else:
        pageStatus = ""

    context = {
        'programpagestatus' : pageStatus,
    }
    activate(myLanguage)
    return render(request, 'program.html', context)

def curriculum(request):
    global currentPage
    currentPage = "curriculum"
    pageStatus = ""
    if currentPage == "curriculum":
        pageStatus = "active"
    else:
        pageStatus = ""
    context = {
        'programpagestatus' : pageStatus,
    }
    activate(myLanguage)
    return render(request, 'curriculum.html', context)