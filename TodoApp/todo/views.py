from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TodoApp
# Create your views here.

def addTask(request):
    task = request.POST.get('task')
    TodoApp.objects.create(task=task)
    return redirect('home')

def markDone(request, pk):
    task = get_object_or_404(TodoApp, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markUnDone(request, pk):
    task = get_object_or_404(TodoApp, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(TodoApp, pk=pk)
    if request.method == "POST":
        updated_task = request.POST.get('task')
        print(task)
        print(updated_task)
        task.task = updated_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task
        }
        return render(request, 'edit_task.html', context)

def deleteTask(request, pk):
    task = get_object_or_404(TodoApp, pk=pk)
    task.delete()
    return redirect('home')
