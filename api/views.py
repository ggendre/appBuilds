from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.




def home(request):
    return HttpResponse("not implemented")


def apps(request):
    return HttpResponse("not implemented")

# TODO later
def appCreate(request):
    return HttpResponse("not implemented")
def appCreate(request):
    return HttpResponse("not implemented")
def appView(request, appName):
    return HttpResponse("not implemented")
def appUpdate(request, appName):
    return HttpResponse("not implemented")
def appDestroy(request, appName):
    return HttpResponse("not implemented")



def builds(request, appName):
    return HttpResponse("not implemented")
def buildCreate(request, appName):
    return HttpResponse("not implemented")


# TODO later
def buildCreate(request, appName):
    return HttpResponse("not implemented")
def buildView(request, appName, buildNumber):
    return HttpResponse("not implemented")
def buildUpdate(request, appName, buildNumber):
    return HttpResponse("not implemented")
def buildDestroy(request, appName, buildNumber):
    return HttpResponse("not implemented")
