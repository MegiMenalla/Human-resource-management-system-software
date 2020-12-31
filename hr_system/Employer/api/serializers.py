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
        fields = ['id','holiday_name', 'active_flag', 'day', 'last_active']
