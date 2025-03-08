from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]

        widgets = {
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
