from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from . import views
from .views import *

urlpatterns = [

    path(r'departments/',  DepartmentListCreateView.as_view()),
    path(r'departments/<int:pk>/',  DepartmentRetrieveDeletePut.as_view()),

    path(r'holidays/',  HolidayListCreateView.as_view()),
    path(r'holidays/<int:pk>/',  HolidayRetrieveDeletePut.as_view()),

    path(r'users/',  UsersListCreateView.as_view()),
    path(r'users/<int:pk>/',  UsersRetrieveDeletePutView.as_view()),

    path(r'requests/',  RequestListCreateView.as_view()),
    path(r'requests/<int:pk>/',  RequestRetrieveDeletePutView.as_view()),

    path(r'roles/',  RoleListCreateView.as_view()),
    path(r'roles/<int:pk>/',  RoleRetrieveDeletePutView.as_view()),

    path(r'user_role/',  UserRoleListCreateView.as_view()),
    path(r'user_role/<int:pk>/',  UserRoleViewRetrieveDeletePutView.as_view()),

    path(r'user_holiday/',   UserHolidayListCreateView.as_view()),
    path(r'user_holiday/<int:pk>/',  UserHolidayRetrieveDeletePut.as_view()),


]

