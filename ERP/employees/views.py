from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployeeRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('employee_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        print(form.errors)  # Debugging line to print form errors
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('employee_list')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def employee_list(request):
    return HttpResponse("Employee List View")
    # return render(request, 'employees/employee_list.html')  
