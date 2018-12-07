from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, redirect

from tasks.models import Task

def index(request):
    task_for_today = Task.objects.filter(for_today=True)

    context = {
        'important_task': task_for_today.filter(important_today=True),
        'today_task': task_for_today.filter(important_today=False)
    }

    return render(request, 'index.html', context)