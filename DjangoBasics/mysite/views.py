from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employees

def home(request):
    employees = Employees.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'home.html', context)