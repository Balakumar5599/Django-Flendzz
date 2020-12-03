from django.db import models

class Task(models.Model):
    task_id=models.IntegerField(primary_key=True)
    task_name=models.CharField(max_length=100)

class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=50)
    task_name=models.CharField(max_length=100)


#class NameList(models.Model):
#   date=models.DateTimeField(auto_now_add=True)
#    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)
#    task=models.ForeignKey('Task',on_delete=models.CASCADE)