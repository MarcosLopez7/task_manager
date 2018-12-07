from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=80)
    reason = models.TextField(null=True)
    how = models.TextField(null=True)
    deadline_date = models.DateField(null=True)
    duration = models.DecimalField(null=True, decimal_places=2, max_digits=8)
    important_today = models.BooleanField(default=False)
    priority = models.IntegerField()
    currently_working = models.BooleanField(default=False)
    for_today = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    init_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)