from django import forms
from .models import *


# class Registration(forms.Form):
#     fname=forms.CharField(max_length=50,label="First Name")
#     lname=forms.CharField(max_length=50,label="Last Name")
#     email=forms.EmailField(label="email")
#     contact=forms.IntegerField(label="Contact")

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields="__all__"
    
class LoginForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields=('email','contact')   
