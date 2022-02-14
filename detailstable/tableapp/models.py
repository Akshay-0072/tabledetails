from django.db import models



class TeacherDetails(models.Model):
    teach_name = models.CharField(max_length=20)
    teach_address = models.CharField(max_length=30)
    teach_email = models.EmailField()
    teach_salary = models.IntegerField(max_length=20)
    teach_phone = models.IntegerField(max_length=20)

class EmployeesDetails(models.Model):
    empname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    salary = models.IntegerField(max_length=20)
    phone = models.IntegerField(max_length=20)
    teacher = models.ForeignKey(TeacherDetails,on_delete=models.CASCADE,related_name="employees")
