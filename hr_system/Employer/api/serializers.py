from rest_framework import serializers

from ..models import *


class DepartmentSerializer(serializers.ModelSerializer):
    parent_dep_name = serializers.SerializerMethodField()

    class Meta:
        model = Departments
        fields = ('id', 'department_name', 'department_manager', 'parent_dep', 'parent_dep_name')

    @staticmethod
    def get_parent_dep_name(obj):
        if obj.parent_dep is not None:
            return obj.parent_dep.department_name
        else:
            return 'no parent department'


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficalHolidays
        fields = ['id', 'holiday_name', 'active_flag', 'day', 'last_active']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'salary', 'phone_no', 'hire_date', 'department_id']


# serializer to make a request
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowanceRequest
        fields = ['id', 'user_id', 'start_date', 'end_date', 'start_hour', 'end_hour', 'approval_flag', 'checked',
                  'description']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role', 'min_salary', 'max_allowance_no', 'lifespan']


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id','user', 'role', 'end_date']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user', 'account', 'email', 'password']



