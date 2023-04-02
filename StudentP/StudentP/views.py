from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutus(request):
    return HttpResponse("About us page")

def create_user(request):
    return HttpResponse("Create user")

def feedback(request):
    return HttpResponse("Feedback Page")
