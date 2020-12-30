from rest_framework import serializers

from ..models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'department_name', 'department_manager', 'parent_dep')