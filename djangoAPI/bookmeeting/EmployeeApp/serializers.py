from rest_framework import serializers
from .models import Departments, Employees, Register


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('RegisterId', 'UserName', 'Email', 'Password', 'Group')
