from django import forms 
from .models import  Choice, Question

from betterforms.multiform import MultiModelForm
from django.forms import ModelForm
from django.forms import formset_factory
from django.forms.models import (
    inlineformset_factory, 
    formset_factory, 
    modelform_factory, 
    modelformset_factory
)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)



class PreguntasModelForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    
class OpcionesModelForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes'] # No agregar el campo 'persona'
        

#class createpoll
class CreatePollsForm(MultiModelForm):
 
    form_classes = {
        'question': PreguntasModelForm,
        'options': OpcionesModelForm,
    }

   
choiceFormset = inlineformset_factory(
    Question, Choice, 
    form=OpcionesModelForm,
    extra=1, 
    can_delete=True, 
    can_delete_extra=True
)


# choiceFormset = inlineformset_factory(
#     Question,
#     Choice,
#     form=OpcionesModelForm,
#    # minimum number of forms that must be filled in
#     extra=1,  # number of empty forms to display
#     can_delete=True  # show a checkbox in each form to delete the row
# )