"""Youtube URL Configuration

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
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('video/<int:id>', video, name='video'),
    path('playlist/<int:id>', playlist, name='playlist'),
    path('channel/<int:id>', channel, name='channel'),
    path('history', history, name='history'),
    path('browseChannel',BrowseChannel, name='BrowseChannel'),
    path('subscription',subscription, name='subscription'),
    path('signup', signup, name='signup'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'), name='loginView'),
    path('upload', upload, name='upload'),
    path('sigout',signoutView, name='signoutView')
]
