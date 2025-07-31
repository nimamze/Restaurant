from .models import User
from django import forms

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email','phone','first_name','last_name','password']

class UserLoginForm(forms.Form):

    phone = forms.CharField(label='Enter Phone')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
