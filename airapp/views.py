from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import View, TemplateView, CreateView
import requests as req
import json
from . import forms, models
from .location import Location
from AirToday import credentials as cred

class RegisterView(TemplateView):
    template_name = 'register.html'
    # context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        form = forms.CustomUserForm()
        context['form'] = form
        return context

    def post(self,request, **kwargs):
        form  = forms.CustomUserForm(request.POST)
        if form.is_valid():
            user = models.CustomUser(email = request.POST['email'],
                                    location =request.POST['location'],
                                    coordinates = request.POST['coordinates'] )
            user.set_password(request.POST['password'])
            user.save()
        else:
             print('invalid form')

        return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        loc = Location(self.request)
        clientip = loc.get_client_ip()
        clientip = cred.TEMP_IP#temporary ip while running on localhost
        context['appid'] = cred.AIRPOLLUTION_APPID
        data= json.loads(loc.get_AQI())
        context['status'] = data['data']['text']
        context['value'] = data['data']['value']
        context['updated'] = data['data']['updated']
        coordinates= str(data['data']['coordinates']["latitude"])+\
                        ","+\
                        str(data['data']['coordinates']["longitude"])
        addr = req.get("https://ipapi.co/{0}/json".format(clientip)).text
        print(addr)
        addr = json.loads(addr)
        context['addr'] =  str(addr["city"]+','+addr["region_code"])
        context['source'] = data['data']['source']['name']
        context['alert'] = data['data']['alert']
        for x in data['data']['aqiParams']:
            key = x['name'].lower().replace(" ", "").replace(".", "")
            context[key] = x['value']
        return context
