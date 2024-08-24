from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from .models import Registration,Login
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
    if request.method=="POST":
        data=LoginForm(request.POST)
        
        email=data.cleaned_data["email"]
        contact=data.cleaned_data["contact"]
        print(email,contact)
        user=Registration.objects.filter(email=email)
        # if user:
        #     user= Registration.objects.get(email=email)
        #     print (user)
        
    
    # if form.is_valid():
    #       email=form.cleaned_data["email"]
    #       contact=form.cleaned_data["contact"]
    #       print(email,contact)
    #       user=Login.objects.filter(email=email)
    #       if user:
    #         msg = "Email already exit"
    #         form = LoginForm()
    #         return render(request,"home.html",{"form":form,"msg":msg})
    #       else:
    #         form.save()
    #         msg="Registration succesfull"
    #         form=LoginForm()
    #         return render(request,"home.html",{"form":form,"msg":msg})
    
    form=LoginForm()
    return render(request,'login.html',{'form':form})

def login_data(request):
     form=LoginForm()
     if request.method=="POST":
        data=LoginForm(request.POST)
        
        email=data.cleaned_data["email"]
        contact=data.cleaned_data["contact"]
        print(email,contact)
        user=Registration.objects.filter(email=email)
        if user:
            user= Registration.objects.get(email=email)
            print (user)
        
    
