from django.urls import path
from .views import departmentApi, employeeApi, registerApi
from . import views

urlpatterns = [
    path(r'api/department', views.departmentApi),
    path(r'department/([0-9]+)', views.departmentApi),

    path(r'api/employeeApi', views.employeeApi),
    path(r'employeeApi/([0-9]+)', views.employeeApi),

    path(r'api/registerApi', views.registerApi),
    path(r'registerApi/([0-9]+)', views.registerApi),
]