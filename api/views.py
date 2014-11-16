from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from api.models import *
import json
import utils

# Create your views here.





def home(request):
    return HttpResponse("not implemented")

@login_required()
def apps(request):
    try :
        profile = utils.getProfile(request)
    except :
        return HttpResponse("No profile for this user", status=401)

    arr = []
    for app in profile.apps.all() :
        arr.append( app.get_dict() )

    return HttpResponse( json.dumps(arr) ,content_type="application/json")

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
    try :
        profile = utils.getProfile(request)
    except :
        return HttpResponse("No profile for this user", status=401)

    try :
        app = profile.apps.get(name = appName)
    except :
        return HttpResponse("App not found", status=404)

    res = {}
    for os in Os.objects.all():
        builds = []
        for build in app.build_set.filter(os = os) :
            builds.append( build.get_dict() )
        if builds:
            res[os.name] = builds

    return HttpResponse( json.dumps(res) ,content_type="application/json")


def buildCreate(request, appName):
    return HttpResponse("not implemented")


# TODO later
def buildView(request, appName, buildNumber):
    return HttpResponse("not implemented")
def buildUpdate(request, appName, buildNumber):
    return HttpResponse("not implemented")
def buildDestroy(request, appName, buildNumber):
    return HttpResponse("not implemented")


#todo later
## teams