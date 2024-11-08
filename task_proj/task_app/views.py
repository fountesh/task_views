from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixin import UserIsOwnerMixin
from .models import Task

# Create your views here.

class TaskList(ListView):
    model= Task
    template_name = "task_proj/task_app/templates/task_app/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = Task.objects.all()
        
        # Отримуємо параметри фільтрації
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        
        # Застосовуємо фільтри
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
            
        return queryset

class TaskDetail(DetailView):
    model = Task
    template_name = "task_app/task_detail.html"
    context_object_name = "task"

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description']
    template_name = "task_app/create_task.html"
    login_url = "/login/"
    success_url = "/"
    context_object_name = "add task"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteTask(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    login_url = "/login/"
    success_url = "/"
    template_name = "task_app/delete_confirm.html"

class UpdateTask(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    fields = ['name', 'description']
    success_url = "/"
    template_name = "task_app/update_task.html"

