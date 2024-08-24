from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def home(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
            fname=form.cleaned_data["fname"]
            lname=form.cleaned_data["lname"]
            email=form.cleaned_data["email"]
            contact=form.cleaned_data["contact"]
            print(fname,lname,email,contact)
            user = Registration.objects.filter(email=email)
            if user:
                msg = "Email already exit"
                form = RegistrationForm()
                return render(request,"home.html",{"form":form,"msg":msg})
            else:
                form.save()
                msg="Registration succesfull"
                form=RegistrationForm()
                return render(request,"home.html",{"form":form,"msg":msg})
            # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
            # Registration.objects.create(fname=fname,lname=lname,email=email,contact=contact)
            form.save()
    return render(request,"home.html",{"form":form})

def login(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        
    
    if form.is_valid():
          email=form.cleaned_data["email"]
          contact=form.cleaned_data["contact"]
          print(email,contact)
          user=Login.objects.filter(email=email)
          if user:
            msg = "Email already exit"
            form = LoginForm()
            return render(request,"login.html",{"form":form,"msg":msg})
          else:
            form.save()
            msg="Registration succesfull"
            form=LoginForm()
            return render(request,"login.html",{"form":form,"msg":msg})
    return render(request,'login.html',{'form':form})
