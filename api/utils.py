# -*- coding: utf-8 -*-
from api.models import *


def getProfile(request):
    return Profile.objects.get(user__username=request.user)
