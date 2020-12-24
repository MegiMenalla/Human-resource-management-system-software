from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path(r'test/', views.test),
    path(r'hr/<int:id>/', views.hr, name="hr"),
    path(r'logini/', views.logini, name="logini"),
    path(r'logoutUser/', views.logoutUser, name="logoutUser"),
    path(r'register/', views.register, name="register"),
    path(r'manage_departments/', views.manage_departments, name="manage_departments"),
    path(r'manage_employees/', views.manage_employees, name="manage_employees"),
    path(r'manage_holidays/', views.manage_holidays, name="manage_holidays"),

]