from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User,auth
from PlacementOfficer.models import *
# Create your views here.

def po_login(request):
    message=""
    if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']
     user=auth.authenticate(username=username,password=password)
     if user is not None:
       auth.login(request,user)
       print("user verified",user.username)
       return redirect('po_home')
     else:
       message="Invalid credentials"
    return render(request,'PlacementOfficer/login.html',{'message':message}) 

def po_logout(request):
  auth.logout(request)
  print("logged out")
  return redirect('po_login')  

def po_signup(request):
   if(request.method=="POST"):
    first_name=request.POST['firstName']
    last_name=request.POST['lastName']
    username=request.POST['username']
    password1=request.POST['password1']
    password2=request.POST['password2']
    email=request.POST['email']
    user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
    profile=ProfilePO.objects.create(username=username,user=user,name=first_name+" "+last_name)
    print("User saved")
    return redirect('po_login')
   else:
    return render(request,'PlacementOfficer/signup.html')
def po_home(request):
    return HttpResponse("POhome")
def po_oncampus(request):
    return HttpResponse("POOnCampus")
def po_placement_stats (request):
    return HttpResponse("POPlacementStats")

