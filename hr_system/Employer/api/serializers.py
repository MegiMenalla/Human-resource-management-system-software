from rest_framework import serializers

from ..models import *


'''class depSer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'''


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
        read_only_fields = ('id_department',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ('id_user',)


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ('id_role',)


class UserRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'


class OfficialHolidaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OfficalHolidays
        fields = '__all__'
        read_only_fields = ('id_holidays',)


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllowanceRequest
        fields = '__all__'
        read_only_fields = ('id_request',)


class ProfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllowanceRequest
        fields = '__all__'
