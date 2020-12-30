from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from . import views
from .views import *

urlpatterns = [
    path(r'dep-all/',  DepartmentView.as_view()),
    path(r'dep-one/<int:id>/',  OneDepartmentView.as_view()),
]
