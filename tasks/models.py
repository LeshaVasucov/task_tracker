from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title