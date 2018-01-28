from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import View, TemplateView, CreateView
from django.contrib.gis.geoip2 import GeoIP2
import requests as req
import json
from . import forms, models
from . import location

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
        form = forms.SearchForm()
        context['form'] = form
        return context

    def get(self,request, **kwargs):
        # loc  = location.Location(request)
        # aqi = loc.get_AQI(location='31.6798,76.5026')

        return render(request,'index.html')

    # def post(self,request,**kwargs):
    #     form =
