from django.shortcuts import render, redirect, get_object_or_404

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

        return redirect('/tasks/task/{0}/'.format(instance.pk))
    else:
        context['form'] = form
    return render(request, 'tasks/create_task.html', context)


def task_action(request, pk):

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            task.for_today = instance.for_today
            task.done = instance.done
            task.important_today = instance.important_today
            task.save()

            return redirect('/tasks/todo/')
    else:
        return redirect('/tasks/task/{0}/'.format(task.pk))

