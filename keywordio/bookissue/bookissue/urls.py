"""bookissue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from signup.views import signupaction,signup_student
from login.views import loginaction
from operation.views import create, delete, retrieve,show, update,logout,login_student,show_student
from homepage.views import homepageaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup_student/',signup_student),
    path('signup/',signupaction),
    path('login/',loginaction),
    path('login_student/',login_student),

    path('',homepageaction),
    path('login/create',create),
    path('login/',logout),
    path('login/show',show),
    path('login_student/show_student',show_student),

    path('login/retrieve',retrieve),
    path('login/update',update),
    path('login/delete',delete),





]
