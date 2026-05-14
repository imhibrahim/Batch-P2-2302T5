from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required;
from django.contrib.admin.views.decorators import staff_member_required



# @login_required(login_url='login')
def index(request):
    return render(request,'user/index.html')

def about(request):
    return render(request,'user/about.html')

@login_required(login_url='login')
def contact(request):
    return render(request,'user/contact.html')
def event(request):
    return render(request,'user/events.html')

@login_required(login_url='login')
def course(request):
    return render(request,'user/courses.html')


def detail(request):
    return render(request,'user/course-details.html')
def price(request):
    return render(request,'user/pricing.html')
def start(request):
    return render(request,'user/starter-page.html')
def train(request):
    return render(request,'user/trainers.html')


@staff_member_required
def adminindex(request):
    if not request.user.is_superuser:
        return redirect('home')
    return render(request,"myadmin/side.html")
    


