from asyncio import tasks
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from .models import *

from .form import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'base/list.html', context)


def updateTask(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        'form': form
    }
    return render(request, 'base/update_task.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("/")
    context = { 'task': task }
    return render(request, 'base/delete_task.html', context)
