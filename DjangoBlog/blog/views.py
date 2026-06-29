from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to the Django Blog!</h1>')

def about(request):
    return HttpResponse('<h1>About the Django Blog</h1>')
