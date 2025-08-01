import random
from django.db.models.base import Model as Model
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms 
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout
from . import models
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

@login_required
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

@login_required
def Phone(request:HttpRequest):
    
    if request.method == "POST":
        form = forms.PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            request.session['phone'] = phone
            return redirect('reset_password')
    form = forms.PhoneForm()
    return render(request,'phone.html',{'form':form})

class Profile(LoginRequiredMixin,DetailView):

    model = models.User
    template_name = 'profile.html'
    context_object_name = 'user'
    def get_object(self):
        return self.request.user 
    
class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = models.User
    form_class = forms.ProfileUpdateForm
    context_object_name = 'form'
    template_name = 'profileUpdate.html'
    def get_object(self):
        return self.request.user 
    def get_success_url(self):
        return reverse_lazy('profile')

@login_required
def Verify(request: HttpRequest):

    user = request.user
    if request.method == 'POST':
        form = forms.VerifyForm(request.POST)
        if form.is_valid():
            input_code = form.cleaned_data.get('input')
            saved_code = request.session.get('verification_code')
            if input_code == str(saved_code):
                user.verified = True  # type: ignore
                user.save()
                del request.session['verification_code']  
                return redirect('profile')
            msg = 'Wrong Code'
            return render(request, 'verify.html', {'form': form, 'msg': msg})
    random_number = random.randint(100, 999)
    request.session['verification_code'] = random_number
    send_mail(
        subject='Verify Account',
        message=str(random_number),
        from_email='nimamze3@gmail.com',
        recipient_list=[user.email],  # type: ignore
        fail_silently=False
    )
    form = forms.VerifyForm()
    return render(request, 'verify.html', {'form': form})
