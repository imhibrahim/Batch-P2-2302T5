from django.http import HttpResponse
from django.shortcuts import render


def firstpage(request):
    return HttpResponse("My First Page")


def about1(request):
    return HttpResponse("About Us......")

def sum(request):
    ans=5+5
    return HttpResponse(f"<h1>Your Answer Is : {ans}</h1>")

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")