from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('departments', views.DepartmentView)
router.register('users', views.UsersView)
router.register('roles', views.RoleView)
router.register('userrole', views.UserRoleView)
router.register('holidays', views.OfficalHolidaysView)
router.register('allowance_request', views.AllowanceRequestView)
router.register('profil', views.ProfilView)


urlpatterns = [
    path('', include(router.urls))

]
