from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUpView,name='signup'), # type: ignore
    path('login/',views.LogInView,name='login'), # type: ignore
    path('logout/',views.LogOutView,name='logout'), # type: ignore
]