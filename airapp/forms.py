from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# class myForm(forms.Form):
#     city_list = ['city1','city2']
#     city = forms.ChoiceField(choices=city_list)
