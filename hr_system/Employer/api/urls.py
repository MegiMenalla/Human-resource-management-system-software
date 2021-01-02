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

]

