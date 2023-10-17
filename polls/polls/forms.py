from django import forms 
from .models import  Choice, Question

from betterforms.multiform import MultiModelForm
from django.forms import ModelForm



#last_active = forms.DateField(widget=DateInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            
           'pub_date': forms.DateTimeInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d %H:%M')
        }
       

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes']

class CreatePollform(MultiModelForm):
    class Meta:
        model = Question
        
    choice2 = forms.CharField(label="choice", max_length=100)
    vote2 = forms.IntegerField(label="vote")
    
    form_classes = {
        'question': QuestionForm,
        'choices': ChoiceForm,
        'choices': ChoiceForm,
        'choices2': ChoiceForm,
        'choices3': ChoiceForm,
    }
    
    
   