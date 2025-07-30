from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email','phone','first_name','last_name']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email','phone','first_name','last_name']

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['email','phone','first_name','last_name']