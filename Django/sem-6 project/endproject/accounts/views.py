from django.shortcuts import render,redirect
from .form import Registrationform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method=="POST":
        form=Registrationform(request.POST)
        if form.is_valid():
             user=form.save()
             messages.success(request,"User Registeration Successfully .....!")
             return redirect('login')
    else:
            form=Registrationform()
            return render(request,'Auth/register.html',{'regForm':form})
    
    
def userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid user Name or password")
             
    return render(request,"Auth/login.html")
             
             

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request,'user/index.html')
