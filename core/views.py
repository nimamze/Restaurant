from django.shortcuts import render
from django.http import HttpRequest

def HomeView(request:HttpRequest):
    return render(request,'home.html')
