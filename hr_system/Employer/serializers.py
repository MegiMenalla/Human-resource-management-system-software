from rest_framework import serializers

from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class OfficialHolidaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficalHolidays
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowanceRequest
        fields = '__all__'

