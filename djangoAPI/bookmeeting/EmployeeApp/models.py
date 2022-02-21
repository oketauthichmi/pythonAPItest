from django.db import models


# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=200)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=200)


class Register(models.Model):
    RegisterId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=100)
    Group = models.CharField(max_length=200)
