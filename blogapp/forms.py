from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import CheckboxInput, PasswordInput, RadioSelect, TextInput
from .models import registration,blog

class u_reg(forms.ModelForm):
    class Meta:
        model = registration
        fields = "__all__"

        labels = {'name':'Enter your Name','email':'Enter your Email Id','fi_password':"Enter Password",'se_password':"Confirm Password",'phone':'Phone No.'}

        widgets = {'name':TextInput(attrs={'class':'form-control'}),'email':TextInput(attrs={'class':'form-control'})
        ,'address':TextInput(attrs={'class':'form-control'})
        ,'country':TextInput(attrs={'class':'form-control'})
        ,'state':TextInput(attrs={'class':'form-control'})
        ,'fi_password':PasswordInput(attrs={'class':'form-control'})
        ,'se_password':PasswordInput(attrs={'class':'form-control'}),
        'phone':TextInput(attrs={'class':'form-control'}),
        'gender':RadioSelect
        }



# class to_e_add_blog(forms.ModelForm):
#     class Meta:
#         model = blog
#         fiels = "__all__"