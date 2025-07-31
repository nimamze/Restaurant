from django.contrib.auth.base_user import BaseUserManager

class UserManger(BaseUserManager):

    def create_user(self,email,phone,password,**kwargs):

        email = self.normalize_email(email)
        user = self.model(email=email,phone = phone,password = password,**kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,phone,password,**kwargs):

        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_superuser',True)
        return self.create_user(email=email,phone = phone,password = password,**kwargs)