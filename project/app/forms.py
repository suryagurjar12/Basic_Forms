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
        widgets = {
            'stu_name': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stu_city': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'stu_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    
class LoginForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields=('email','contact')
        widgets = {
            'stu-email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stu_contact':forms.NumberInput(attrs={'class': 'form-control'}),
        }  
        
        
class StudentForm(forms.ModelForm):
    class Meta:
        models=QureyModel
        fields=('name','email','qurey') 
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'query': forms.TextInput(attrs={'class': 'form-control'}),  
        }
