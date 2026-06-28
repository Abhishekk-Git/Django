from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employees

# Create your views here.
def employee_details(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    print(employee)
    context = {
        'employee': employee
    }
    return render(request, 'employee_details.html', context)