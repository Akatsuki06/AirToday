from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import View, TemplateView, CreateView
from django.contrib.gis.geoip2 import GeoIP2
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
        context['clientip'] = loc.get_client_ip()
        context['appid'] = cred.AIRPOLLUTION_APPID
        return context

    # def get(self,request, **kwargs):
    #     return render(request,'index.html')
#get client ip here and put it in html and then use js to find lat and lng and
#retrieve aqi
