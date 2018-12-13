from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Task
from .forms import TaskForm, UpdateTaskForm

# Create your views here.
def todo(request):
    tasks = Task.objects.filter(for_today=False, done=False)

    context = {
        'tasks': tasks,
        'title': 'TO DO Task'
    }

    return render(request, 'tasks/todo.html', context)

def done(request):
    tasks = Task.objects.filter(done=True)

    context = {
        'tasks': tasks,
        'title': 'DONE'
    }

    return render(request, 'tasks/todo.html', context)

def task(request, pk):

    task = get_object_or_404(Task, pk=pk)
    form = UpdateTaskForm(None)

    context = {
        'task': task,
        'update_form': form
    }

    return render(request, 'tasks/task.html', context)

def create_task(request):

    context = {
        'form': TaskForm(None)
    }

    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('/tasks/task/{0}/'.format(instance.pk))
        else:
            context['form'] = form
            return render(request, 'tasks/create_task.html', context)

    return render(request, 'tasks/create_task.html', context)

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task )

    context = {
        'form': form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        return redirect(reverse("tasks:task", kwargs={"pk": task.pk}))
    else:
        context['form'] = form
    return render(request, 'tasks/create_task.html', context)


def task_action(request, pk, action):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        if action == 'Delete':
            task.delete()
            return redirect(reverse("tasks:todo"))
        elif action == 'Done':
            task.done = True
            task.for_today = False
            task.important_today = False
            task.save()
        elif action == 'Today':
            task.for_today = True
            task.save()
        elif action == 'Important':
            task.important_today = True
            task.save()

    return redirect(reverse("tasks:task", kwargs={"pk": pk}))
