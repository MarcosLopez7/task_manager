from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, redirect

from tasks.models import Task
from .form import UserLoginForm

def index(request):
    task_for_today = Task.objects.filter(for_today=True)

    context = {
        'important_task': task_for_today.filter(important_today=True),
        'today_task': task_for_today.filter(important_today=False)
    }

    return render(request, 'index.html', context)

def sign_in(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = UserLoginForm(None)
            return render(request, 'login.html', {'form': form, 'message': 'Email or password are incorrect'})

    form = UserLoginForm(None)
    return render(request, 'login.html', {'form': form})
