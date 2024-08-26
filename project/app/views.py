from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from .models import StudentModel
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
            password =form.cleaned_data['password']
            print(fname,lname,email,contact,password)
            form.save()
            msg="Registration Successfully"
            return render(request,"home.html",{"form":form,'msg':msg})
            
    else:
          
           return render(request,"home.html",{"form":form})

def login(request):
    form = LoginForm()
    if request.method=="POST":
        data = LoginForm(request.POST)
        if data.is_valid():
            email = data.cleaned_data['stu_email']
            password = data.cleaned_data['stu_password']
            # print(email,password)
            user = StudentModel.objects.filter(stu_email=email)
            
            if user:
                user = StudentModel.objects.get(stu_email=email)
                # print(user.stu_password)
                if user.stu_password==password:
                    name = user.stu_name
                    email = user.stu_email
                    contact = user.stu_mobile
                    city = user.stu_city
                    data = {
                        'name':name,
                        'email':email,
                        'contact':contact,
                        'city':city
                    }
                    return render(request,'dashboard.html',{'data':data})
                else:
                    msg = "Email & Password not matched"
                    return render(request,'login.html',{'form':form,'msg':msg})
            else:
                msg = "Email not register so please register first"
                return render(request,'login.html',{'form':form,'msg':msg})
    else:
        return render(request,'login.html',{'form':form})
    
