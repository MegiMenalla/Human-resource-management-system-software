from rest_framework import serializers

from ..models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'


class CreateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('department_name', 'department_manager', 'parent_dep')