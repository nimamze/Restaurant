from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUpView,name='signup'), 
    path('login/',views.LogInView,name='login'), 
    path('logout/',views.LogOutView,name='logout'), 
    path('reset-password/',views.ResetPassword,name='reset_password'),
    path('phone/',views.Phone,name='phone'),  
    path('profile/',views.Profile.as_view(),name='profile'),
    path('update-profile/',views.ProfileUpdate.as_view(),name='updateProfile'),
    path('verify/',views.Verify,name='verify'), # type: ignore
]