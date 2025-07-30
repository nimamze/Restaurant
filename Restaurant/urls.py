from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView,name='home'), # type: ignore
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
]
