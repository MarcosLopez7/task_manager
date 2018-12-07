from django.conf.urls import url, include

from .views import todo, create_task, task_action, task, done

app_name = 'tasks'

urlpatterns = [
    url("^todo/", todo, name='todo'),
    url("^done/", done, name='done'),
    url("^create-task/", create_task, name='create-task'),
    url("^task/(?P<pk>\d+)/", task, name='task'),
    url("^task-action/(?P<pk>\d+)/", task_action, name='task-action'),
]