from django.shortcuts import render
from tasks.models import Task
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from tasks.mixins import UserIsOwnerMixin
from tasks.forms import TaskForm , TaskFilterForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"



    def get_queryset(self):
        qeuryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        if status :
            qeuryset = qeuryset.filter(status=status)
        return qeuryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm(self.request.GET)

        return context

class TaskDetailView(UserIsOwnerMixin, DetailView):
    model = Task
    context_object_name = "task"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy("task-list")
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

