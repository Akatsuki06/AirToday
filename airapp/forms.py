from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserForm(forms.ModelForm):
    # state_list =[('state1','state1'),('state2','state2')]
    # state = forms.ChoiceField(choices=state_list)
    class Meta():
        model = CustomUser
        fields = ('email','password','location','coordinates')

        widgets = {
            'password': forms.PasswordInput()
        }
