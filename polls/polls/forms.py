from django import forms 
from .models import  Choice, Question

from betterforms.multiform import MultiModelForm
from django.forms import ModelForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
