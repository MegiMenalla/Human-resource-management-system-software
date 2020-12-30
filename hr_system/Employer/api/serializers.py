from rest_framework import serializers

from ..models import *


class DepartmentSerializer(serializers.ModelSerializer):
    parent_dep_name = serializers.SerializerMethodField()

    class Meta:
        model = Departments
        fields = ('id', 'department_name', 'department_manager', 'parent_dep', 'parent_dep_name')

    @staticmethod
    def get_parent_dep_name(obj):
        return obj.parent_dep.department_name
