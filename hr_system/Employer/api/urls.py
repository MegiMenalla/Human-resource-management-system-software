from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from . import views
from .views import DepartmentView, CreateDepartmentView

urlpatterns = [
    path(r'dep-view/',  DepartmentView.as_view()),
    path(r'dep-create',  CreateDepartmentView.as_view()),
]
