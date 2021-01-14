from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Departments(models.Model):
    department_name = models.CharField(max_length=100, null=True)
    department_manager = models.CharField(max_length=100, null=True)
    parent_dep = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name


class Users(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    salary = models.FloatField(null=True)
    phone_no = models.CharField(max_length=200, null=True)
    hire_date = models.DateField(auto_now_add=True)
    department_id = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=True, unique=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class UserHoliday(models.Model):
    us = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    days_left = models.FloatField(null=True)


class Role(models.Model):
    role = models.CharField(max_length=200, null=True)
    min_salary = models.FloatField(null=True)
    max_allowance_no = models.IntegerField(null=True)  # in days
    lifespan = models.IntegerField(null=True)
    users = models.ManyToManyField(Users, through='UserRole')


class UserRole(models.Model):
    user = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)


class OfficalHolidays(models.Model):
    holiday_name = models.CharField(max_length=200, null=True)
    active_flag = models.BooleanField(default=True, null=True)
    day = models.DateField(null=True)
    last_active = models.DateField(null=True)


class AllowanceRequest(models.Model):
    user_id = models.ForeignKey(Users, null=True, on_delete=models.CASCADE, related_name='applicant')
    approver = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_hour = models.TimeField(default='00:00:00')
    end_hour = models.TimeField(default='23:59:59')

    approval_flag = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    description = models.TextField(max_length=1000, null=True, blank=True)


'''class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    account = models.OneToOneField(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.first_name'''
