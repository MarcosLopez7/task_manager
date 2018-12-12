from django.conf.urls import url, include
from django.urls import path

from .views import todo, create_task, task_action, task, done, edit_task

app_name = 'tasks'

urlpatterns = [
    url("^todo/", todo, name='todo'),
    url("^done/", done, name='done'),
    url("^create-task/", create_task, name='create-task'),
    url("^task/(?P<pk>\d+)/", task, name='task'),
    path("edit-task/<int:pk>/", edit_task, name='edit-task'),
    url("^task-action/(?P<pk>\d+)/", task_action, name='task-action'),
]