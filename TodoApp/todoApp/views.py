from django.shortcuts import render
from todo.models import TodoApp

def home(request):
    tasks = TodoApp.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = TodoApp.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)

def add_task(request):
    task = request
    return render(request, 'home.html')

