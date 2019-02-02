"""two URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from appone import views
from appone.views import home
from appone.views import getlogin
from appone.views import getlogout
from appone.views import getafter
from appone.views import getregister
from appone.views import getprofile
from appone.views import getshow

from django.contrib.auth.views import password_reset, password_reset_done,password_reset_confirm,password_reset_complete
urlpatterns = [

    path('', home, name='home'),
    path('login', getlogin, name="login"),
    path('after', getafter, name="after"),
    path('logout', getlogout, name="logout"),
    path('register', getregister, name="register"),
    path('profile', getprofile, name="profile"),
    path('reset-password', password_reset, name="reset_password"),
    path('reset-password/done', password_reset_done, name="password_reset_done"),
    path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)', password_reset_confirm, name="password_reset_confirm"),
    path('reset-password/complete', password_reset_complete, name="password_reset_complete"),
    path('show', getshow, name="show")


]
