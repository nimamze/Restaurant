from django.shortcuts import render,redirect
from .forms import UserForm,UserChangeForm
from django.http import HttpRequest

def SignUpView(request:HttpRequest):
    
    msg = "Please Enter Your Information For Sign Up"
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = UserForm()
    return render(request,'signup.html',{'form':form,'msg':msg})
