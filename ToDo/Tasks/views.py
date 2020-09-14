from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .froms import TaskForm


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        print("Happy Birthday Lalit")
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'Tasks/list.html', context=context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        print("Happy Birthday Lalit")
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'Tasks/update_task.html', context=context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        print("Happy Birthday Lalit")
        item.delete()
        return redirect('/')

    context = {
        'item': item,
    }
    return render(request, 'Tasks/delete.html', context=context)
