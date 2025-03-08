from django.shortcuts import render
from tasks.models import Task
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from tasks.forms import TaskForm
# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"

class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("task-list")
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)