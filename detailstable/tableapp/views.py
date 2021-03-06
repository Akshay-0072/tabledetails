from django.shortcuts import render, HttpResponse
from tableapp.models import EmployeesDetails, TeacherDetails

# def empDetails(request):
#     emp = EmployeesDetails.objects.all()
#     # if request.method == 'POST':
#     empname = request.POST.get('empname', 'default')
#     address = request.POST.get('address', 'default')
#     email = request.POST.get('email', 'default')
#     salary = request.POST.get('salary')
#     phone = request.POST.get('phone')
#     ins = EmployeesDetails(empname=empname, address=address, email=email, salary=salary, phone=phone)
#     ins.save()
#     return render(request, 'index.html')


def teachDetails(request):
    teach = TeacherDetails.objects.all()
    if request.method == 'POST':
        teach_name= request.POST['empname']
        teach_address= request.POST['address']
        teach_email= request.POST['email']
        teach_salary= request.POST['salary']
        teach_phone= request.POST['phone']
        pns = TeacherDetails(teach_name=teach_name, teach_address=teach_address, teach_email=teach_email, teach_salary=teach_salary, teach_phone=teach_phone)
        pns.save()
    return render(request, 'teacher.html')

def table(request):
    # emp = EmployeesDetails.objects.all()
    # teach = TeacherDetails.objects.all()
    return render(request, 'tables.html')

def empDetails(request):
    p = EmployeesDetails(empname='empname', address='address', email='email', salary=354, phone=3542)
    p.save()