from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Departments(models.Model):
    id_department = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100, null=True)
    parent_dep = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    salary = models.FloatField(null=True)
    phone_no = models.CharField(max_length=200, null=True)
    hire_date = models.DateField(auto_now_add=True)
    department_id = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    role = models.CharField(max_length=200, null=True)
    min_salary = models.FloatField(null=True)
    max_allowance_no = models.IntegerField(null=True)
    lifespan = models.IntegerField(null=True)

    users = models.ManyToManyField(Users, through='UserRole')

    def __str__(self):
        return self.role


class UserRole(models.Model):
    user = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)


class OfficalHolidays(models.Model):
    id_holidays = models.AutoField(primary_key=True)
    holiday_name = models.CharField(max_length=200, null=True)
    active_flag = models.BooleanField(default=True)
    last_active = models.DateField(null=True)

    def __str__(self):
        return self.holiday_name


class AllowanceRequest(models.Model):
    id_request = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, null=True, on_delete=models.CASCADE, related_name='kerkuesi')
    approver_id = models.ForeignKey(Users, null=True, on_delete=models.CASCADE, related_name='aprovuesi')

    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_hour = models.TimeField(default='00:00:00')
    end_hour = models.TimeField(default='23:59:59')

    approval_flag = models.BooleanField(default=False)


class Profil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    account = models.OneToOneField(Users, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user
