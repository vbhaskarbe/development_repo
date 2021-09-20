from django.http import response
from django.shortcuts import render
from App1.models import Newuser
from django.contrib import messages



# Create your views here.
def Indexpage(request):
    return render(request, 'index.html')

def Userreg(request):
    if request.method=='POST':
       Username=request.POST['Username']
       Email = request.POST['Email']
       pwd = request.POST['pwd']
       Age = request.POST['Age']
       Gender = request.POST['Gender']  
       MartialStatus = request.POST['MartialStatus']
       Newuser(Username=Userreg, Email=Email,pwd=pwd, Age=Age, Gender=Gender, MartialStatus=MartialStatus).save()
       messages.success(request, "The New User" + request.POST['Username'] + " is Successfully Registered" )
       return render(request, 'registration.html')
    else:
        return render(request, 'registration.html')

def loginpage(request):
    if request.method == "POST":
        try:
            userdetails=Newuser.objects.get(Email=request.POST['Email'],pwd=request.POST['pwd'])
            print("Username=",userdetails)
            request.session['Email']=userdetails.Email
            return render(request,'index.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username / Password Invalid...!')
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'index.html')
    return render(request,'index.html')    