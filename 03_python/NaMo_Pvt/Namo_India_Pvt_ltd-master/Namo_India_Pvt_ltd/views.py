from django.http import response
from django.shortcuts import render
from App1.models import Newuser
from django.contrib import messages
from App1.models import Registration



# Create your views here.
def Indexpage(request):
    return render(request, 'index.html')

def Userreg(request):
    if request.method=='POST':
       Username=request.POST['Username']
       Email = request.POST['Email']
       pwd = request.POST['pwd']
       PhoneNumber= request.POST['PhoneNumber']
       Newuser(Username=Username, Email=Email, pwd=pwd, PhoneNumber=PhoneNumber).save()
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
            messages.success(request,'Username / Password Invalid / Please Register if you are a new user ...!')
    return render(request, 'login.html')

def view(request):
    App1_newuser = Newuser.objects.all()
    context = {'table': App1_newuser}
    return render(request, 'index.html', context)


def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'index.html')
    return render(request,'index.html')    


def new_registration(request):
    if request.method=='POST':
       Name=request.POST['Name']
       Email = request.POST['Email']
       PhoneNumber = request.POST['PhoneNumber']
       Gender = request.POST['Gender']
       Prerequisite = request.POST['Prerequisite']
       Education = request.POST['Education']
       Description = request.POST['Description']
       Registration(Name = Name, Email=Email,PhoneNumber=PhoneNumber,Gender=Gender,Prerequisite=Prerequisite,Education=Education,Description=Description).save()
       messages.success(request, "The New User " + request.POST['Name'] + " is Successfully Registered" )
       return render(request, 'main_registration.html')
    else:
        return render(request, 'main_registration.html')