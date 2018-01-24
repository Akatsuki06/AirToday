from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import View, TemplateView
from django.contrib.gis.geoip2 import GeoIP2
#>>>
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

def get_AQI(loc):
    lat,lon=loc.split(',')
    print('loc in inside aqi',lat,lon)
    params={
    'lat':'28.7040590&',
    'lon':'77.10249',
    'APPID':'m953d6onf11vvufmc8gmugatqb',
    }
    requrl ='http://api.airpollutionapi.com/1.0/aqi'
    data = req.get(requrl,params)
    print(data)

def get_location(request):
    ip=get_client_ip(request)
    ip='169.149.218.89'
    user_data = 'https://ipinfo.io/{0}/json'.format(ip)
    data = json.loads(req.get(user_data).text)
    print(data)
    print('ip:',data['ip'],'city: ',data['city'])
    print('loc',data['loc'])
    return data


def get_client_ip(request):
    remote_address = request.META.get('REMOTE_ADDR')
    # set the default value of the ip to be the REMOTE_ADDR if available
    # else None
    ip = remote_address
    # try to get the first non-proxy ip (not a private ip) from the
    # HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        # remove the private ips from the beginning
        while (len(proxies) > 0 and
                proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip
