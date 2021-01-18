from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path(r'hr/', views.hr, name="hr"),
    path(r'logini/', views.logini, name="logini"),
    path(r'logoutUser/', views.logoutUser, name="logoutUser"),
    path(r'change_password/', views.change_password, name="change_password"),
    path(r'manage_departments/', views.manage_departments, name="manage_departments"),
    path(r'manage_employees/', views.manage_employees, name="manage_employees"),
    path(r'manage_holidays/', views.manage_holidays, name="manage_holidays"),
    path(r'emp_page/', views.emp_page, name="emp_page"),
    path(r'manager_page/', views.manager_page, name="manager_page"),
    path(r'see_answer_requests/', views.see_answer_requests, name="see_answer_requests"),
    path(r'manage_jobs/', views.manage_jobs, name="manage_jobs"),

]