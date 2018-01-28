from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserForm(forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = ('email','phone','password','location','coordinates')
        widgets = {
            'email': forms.EmailInput(attrs=
                        {'class':'form-control input-lg',
                        'placeholder':'email@email.email'}
                        ),
            'phone': forms.TextInput(attrs=
                        {'class':'form-control input-lg',
                        'placeholder':'1234567890'}
                        ),
            'password': forms.PasswordInput(attrs=
                        {'class':'form-control input-lg',
                        'placeholder':'password'}),
            'location': forms.Textarea(attrs=
                        {'class':'form-control input-lg',
                        'id':'locationid','rows':2, 'cols':10,
                        'readonly':'readonly',
                        'placeholder':'location'}
                        ),
            'coordinates': forms.TextInput(attrs=
                        {'class':'form-control input-lg',
                        'id':'coordinatesid',
                        'readonly':'readonly',
                        'placeholder':'coordinates'}
                        )
                    }

class SearchForm(forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = ('location','coordinates')
        widgets = {
            'location': forms.Textarea(attrs=
                        {'class':'form-control input-lg',
                        'id':'locationid','rows':2, 'cols':10,
                        'readonly':'readonly',
                        
                        'placeholder':'location'}
                        ),
            'coordinates': forms.TextInput(attrs=
                        {'class':'form-control input-lg',
                        'id':'coordinatesid',
                        'readonly':'readonly',
                        'placeholder':'coordinates'}
                        )

        }
