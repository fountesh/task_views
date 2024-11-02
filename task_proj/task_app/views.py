from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Task

# Create your views here.

class TaskList(ListView):
    model= Task
    template_name = "task_proj/task_app/templates/task_app/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all()

class TaskDetail(DetailView):
    model = Task
    template_name = "task_app/task_detail.html"
    context_object_name = "task"

class CreateTask(CreateView):
    model = Task
    fields = ['name', 'description']
    template_name = "task_app/create_task.html"
    success_url = "/"
    context_object_name = "add task"