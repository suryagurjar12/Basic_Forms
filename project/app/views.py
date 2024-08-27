from django.shortcuts import render
from app.forms import RegistrationForm,LoginForm,StudentForm
from .models import StudentModel,QureyModel
# Create your views here.

def home(request):
    form = RegistrationForm()
    if request.method=='POST':
        data = RegistrationForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['fname']
            email=data.cleaned_data['email']
            contact=data.cleaned_data['contact']
            password = data.cleaned_data['password']
            print(name,email,contact,password)
            data.save()
            msg="Registration Successfully"
            return render(request,'home.html',{'form':form,'msg':msg})
    else:
        return render(request,'home.html',{'form':form})
    
def login(request):
    form = LoginForm()
    if request.method=="POST":
        data = LoginForm(request.POST)
        if data.is_valid():
            email = data.cleaned_data['email']
            contact = data.cleaned_data['contact']
            # print(email,password)
            user = StudentModel.objects.filter(email=email)
            
            if user:
                user =StudentModel.objects.get(email=email)
                # print(user.stu_password)
                if user.contact==contact:
                    name = user.fname
                    email = user.email
                    contact = user.contact
                    password = user.password
                    data = {
                        'name':name,
                        'email':email,
                        'contact':contact,
                        'password':password
                    }
                    form1=StudentForm()
                    return render(request,'dashboard.html',{'data':data,'query':form1})
                else:
                    msg = "Email & Password not matched"
                    return render(request,'login.html',{'form':form,'msg':msg})
            else:
                msg = "Email not register so please register first"
                return render(request,'login.html',{'form':form,'msg':msg})
    else:
        return render(request,'login.html',{'form':form})
    
