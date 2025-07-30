from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManger

class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email','first_name','last_name']
    objects = UserManger() # type: ignore

    def __str__(self):
        return f"User : {self.first_name} {self.last_name}"
