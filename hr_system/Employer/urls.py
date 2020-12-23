from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path(r'test/', views.test),
    path('', views.home, name="home"),
    path(r'logini/', views.logini, name="logini"),
    path(r'logoutUser/', views.logoutUser, name="logoutUser"),
    path(r'register/', views.register, name="register"),

]