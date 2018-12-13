from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name task'}))
    reason = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Why do I it?'}), required=False)
    how =  forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How can I do it?'}), required=False)
    duration = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hours duration'}), required=False)
    important_today = forms.BooleanField(widget=forms.CheckboxInput(), label='Important for today', required=False)
    priority = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Priority task'}))
    for_today = forms.BooleanField(widget=forms.CheckboxInput(), label='Is for today?', required=False)
    init_date = forms.DateTimeField(widget=forms.DateTimeInput, label='Init date', required=False)
    end_date = forms.DateTimeField(widget=forms.DateTimeInput, label='end date', required=False)

    class Meta:
        model = Task
        fields = [
            'name',
            'reason',
            'how',
            'duration',
            'important_today',
            'priority',
            'for_today',
            'init_date',
            'end_date'
        ]

class UpdateTaskForm(forms.ModelForm):
    important_today = forms.BooleanField(widget=forms.CheckboxInput(), label='Important for today', required=False)
    for_today = forms.BooleanField(widget=forms.CheckboxInput(), label='Is for today?', required=False)
    done = forms.BooleanField(widget=forms.CheckboxInput(), label='finished', required=False)

    class Meta:
        model = Task
        fields = [
            'important_today',
            'for_today',
            'done'
        ]