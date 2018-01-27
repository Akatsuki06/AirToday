from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import View, TemplateView, CreateView
from django.contrib.gis.geoip2 import GeoIP2


import requests as req
import json
from . import forms, models


class IndexView(TemplateView):
    template_name = 'index.html'
    # context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        form = forms.CustomUserForm()
        context['form'] = form
        context['hello']='hello'
        return context

    def post(self,request, **kwargs):
        form  = forms.CustomUserForm(request.POST)
        if form.is_valid():
            user = models.CustomUser(email = request.POST['email'],
                                    location =request.POST['location'],
                                    state = request.POST['state'] )
            user.set_password(request.POST['password'])
            user.save()

        return render(request,'index.html')
