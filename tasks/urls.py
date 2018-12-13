from django.conf.urls import url, include
from django.urls import path

from .views import todo, create_task, task_action, task, done, edit_task

app_name = 'tasks'

urlpatterns = [
    path("todo/", todo, name='todo'),
    path("done/", done, name='done'),
    path("create-task/", create_task, name='create-task'),
    path("task/<int:pk>/", task, name='task'),
    path("edit-task/<int:pk>/", edit_task, name='edit-task'),
    path("task-action/<int:pk>/<slug:action>/", task_action, name='task-action'),
]