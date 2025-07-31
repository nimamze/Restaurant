from django.shortcuts import render,redirect
from . import forms 
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout
from . import models

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
            msg = "Invalid Information"
            return render(request,'login.html',{'form':form,'msg':msg})
    msg = "Please Enter Your Information For Log In"       
    form = forms.UserLoginForm()
    return render(request,'login.html',{'form':form,'msg':msg})

def LogOutView(request:HttpRequest):
    
    logout(request)
    return redirect('home')

def ResetPassword(request: HttpRequest):

    if request.method == "POST":
        form = forms.ResetPassword(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            phone = request.session.get('phone')
            if not phone:
                return redirect('phone')  
            try:
                user = models.User.objects.get(phone=phone)
            except models.User.DoesNotExist:
                msg = "User not found"
                return render(request, 'reset_password.html', {'form': form, 'msg': msg})
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                del request.session['phone']  
                return redirect('login')  
            else:
                msg = "Passwords do not match"
                return render(request, 'reset_password.html', {'form': form, 'msg': msg})
    form = forms.ResetPassword()
    return render(request, 'reset_password.html', {'form': form})


def Phone(request:HttpRequest):
    
    if request.method == "POST":
        form = forms.PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            request.session['phone'] = phone
            return redirect('reset_password')
    form = forms.PhoneForm()
    return render(request,'phone.html',{'form':form})