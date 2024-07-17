"""healthhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from hospital.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',loginaction),
    path('aboutus',aboutusaction),
    path('signup/',signaction),
    path('signup_login/',signup_login),
    path('logout/',logout),
    path('contactus',contactusaction),
    path('checkdisease',checkdisease),
    path('booking',bookingaction),
    # path('appoin',appaction),
    path('staff_login/',staffloginaction),
    path('queries',passqueries),
    path('addflight',addflightaction),
    path('security_login',securityloginaction),
    path('cons_his',consul_his),
    path('chat',patientchat),
    path('extractno',extractflytno),
    path('yes_appoin',extractflytno1),



















]
