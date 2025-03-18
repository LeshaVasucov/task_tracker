from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]

        widgets = {
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("", "ALL")
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False,
                               label="Статус")