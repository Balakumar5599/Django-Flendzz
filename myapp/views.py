
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee

def myView(request):
    return HttpResponse('Hello World')

def empView(request):
    emps=Employee.objects.all()
    emp={
         "emp":emps
        }
    if request.method == "POST":
        if request.POST.get('emp_id') and request.POST.get('emp_name') and request.POST.get('task_name'):
            post=Employee()
            post.emp_id=request.POST.get('emp_id')
            post.emp_name=request.POST.get('emp_name')
            post.task_name=request.POST.get('task_name')
            post.save()
            return render(request,"emppage.html",emp)
    else:

        return render(request,"emppage.html",emp)

def remove(request,emp_id,emp_name,task_name):
    delete_data=Employee.objects.filter(emp_id=emp_id,emp_name=emp_name,task_name=task_name).delete()
    return redirect('/emp')

def learings_list(request,emp_id):
    learnings=Employee.objects.filter(emp_id=emp_id).all()
    learning={
        "learning":learnings
    }
    return render(request,"learnings.html",learning)
