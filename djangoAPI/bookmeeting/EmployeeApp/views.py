from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Departments, Employees, Register
from .serializers import DepartmentSerializer, EmployeeSerializer, RegisterSerializer

# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("thanh cong", safe=False)
        return JsonResponse("that bai", safe=False)
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('update thanh cong', safe=False)
        return JsonResponse('Update that bai', safe=False)
    elif request.method=='DELETE':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department.delete()
        return JsonResponse('xoa thanh cong', safe=False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method=='POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("thanh cong", safe=False)
        return JsonResponse("that bai", safe=False)
    elif request.method == 'PUT':
        employees_data = JSONParser().parse(request)
        employees = Departments.objects.get(EmployeeId=employees_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employees, data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse('update thanh cong', safe=False)
        return JsonResponse('Update that bai', safe=False)
    elif request.method == 'DELETE':
        employees_data = JSONParser().parse(request)
        employees = Employees.objects.get(EmployeeId=employees_data['EmployeeId'])
        employees.delete()
        return JsonResponse('xoa thanh cong', safe=False)




@csrf_exempt
def registerApi(request):
    if request.method == 'GET':
        registers = Register.objects.all()
        registers_serializer = RegisterSerializer(registers, many=True)
        return JsonResponse(registers_serializer.data, safe=False)
    elif request.method == 'POST':
        registers_data = JSONParser().parse(request)
        registers_serializer = RegisterSerializer(data=registers_data)
        registersChekuser = Register.objects.all()
        registers_serializer_checkuser = RegisterSerializer(registersChekuser, many=True)
        #if (registers_data['UserName']==i['UserName'] for i in registers_serializer_checkuser.data):
            #return JsonResponse('Trùng username')
        for i in registers_serializer_checkuser.data:
            if((registers_data['UserName']==i['UserName'])==True):
                return JsonResponse("trùng username", safe=False)
            if ((registers_data['Email'] == i['Email']) == True):
                return JsonResponse("đã tồn tại email", safe=False)
        if registers_serializer.is_valid():
            registers_serializer.save()
            return JsonResponse("thành công", safe=False)
        return JsonResponse("thất bại", safe=False)
    elif request.method == 'PUT':
        registers_data = JSONParser().parse(request)
        registers = Register.objects.get(RegisterId=registers_data['RegisterId'])
        registers_serializer = RegisterSerializer(registers, data=registers_data)
        if registers_serializer.is_valid():
            registers_serializer.save()
            return JsonResponse('update thanh cong', safe=False)
        return JsonResponse('Update that bai', safe=False)
    elif request.method == 'DELETE':
        registers_data = JSONParser().parse(request)
        registers = Register.objects.get(RegisterId=registers_data['RegisterId'])
        registers.delete()
        return JsonResponse('xoa thanh cong', safe=False)