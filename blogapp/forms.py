from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import CheckboxInput, PasswordInput, RadioSelect, TextInput
from .models import registration

class u_reg(forms.ModelForm):
    class Meta:
        model = registration
        fields = ['name','email','address','country','state','fi_password','se_password','phone','gender','is_tick']

        labels = {'name':'Enter your Name','email':'Enter your Email Id','fi_password':"Enter Password",'se_password':"Confirm Password",'phone':'Phone No.'}

        widgets = {'name':TextInput(attrs={'class':'form-control'}),'email':TextInput(attrs={'class':'form-control'})
        ,'address':TextInput(attrs={'class':'form-control'})
        ,'country':TextInput(attrs={'class':'form-control'})
        ,'state':TextInput(attrs={'class':'form-control'})
        ,'fi_password':PasswordInput(render_value=True,attrs={'class':'form-control'})
        ,'se_password':PasswordInput(render_value=True,attrs={'class':'form-control'}),
        'phone':TextInput(attrs={'class':'form-control'}),
        'gender':RadioSelect
        }
