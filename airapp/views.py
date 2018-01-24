from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import View, TemplateView
from django.contrib.gis.geoip2 import GeoIP2


import requests as req
import json
import geoip2.database

class IndexView(TemplateView):
    template_name = 'index.html'


def funcView(request):
    data = get_location(request)
    loc = data['loc']
    get_AQI(loc)
    return HttpResponse('Hello: '+str(data))
