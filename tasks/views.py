from django.shortcuts import render , redirect
from tasks.models import Task, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from tasks.mixins import UserIsOwnerMixin
from tasks.forms import TaskForm , TaskFilterForm , CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserCreationForm
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

class TaskDetailView( DetailView):
    model = Task
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid() :
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()
        return redirect("task-detail", pk=comment.task.pk)
    


class CommentUpdateView( UpdateView):
    model = Comment
    fields = ['content']

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.task.id})
    
    

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy("task-list")
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

class CustomLoginView(LoginView):
    template_name = "tasks/login.html"

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "tasks/register.html"
    success_url = reverse_lazy("task-list")