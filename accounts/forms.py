from .models import User
from django import forms

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email','phone','first_name','last_name','password','is_manager']

class UserLoginForm(forms.Form):

    phone = forms.CharField(label='Enter Phone')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

class ResetPassword(forms.Form):

    new_password = forms.CharField(label='New Password',widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

class PhoneForm(forms.Form):

    phone = forms.CharField(label='Enter Phone')