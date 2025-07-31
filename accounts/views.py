from django.shortcuts import render,redirect
from . import forms 
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout

def SignUpView(request:HttpRequest):
       
    if request.method == "POST":
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect('home')
        else:
            msg = 'User Already Exist'
            return render(request,'signup.html',{'form':form,'msg':msg})
    msg = "Please Enter Your Information For Sign Up"
    form = forms.UserCreateForm()
    return render(request,'signup.html',{'form':form,'msg':msg})

def LogInView(request:HttpRequest):

    if request.method == "POST":
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data           
            phone = data.get('phone')
            password = data.get('password')
            user = authenticate(request,username=phone,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                msg = "Invalid Information"
                return render(request,'login.html',{'form':form,'msg':msg})
    msg = "Please Enter Your Information For Log In"       
    form = forms.UserLoginForm()
    return render(request,'login.html',{'form':form,'msg':msg})

def LogOutView(request:HttpRequest):
    
    logout(request)
    return redirect('home')