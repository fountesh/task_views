from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixin import UserIsOwnerMixin
from .models import Task
from .forms import TaskFilterForm

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_app/task_list.html"
    context_object_name = "tasks"
    login_url = "/login/"
    paginate_by = 6

    def get_queryset(self):
        # Спочатку фільтруємо за поточним користувачем
        queryset = Task.objects.filter(user=self.request.user)
        
        # Отримуємо параметри фільтрації
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        
        # Застосовуємо фільтри тільки якщо вибрано конкретні значення
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
            
        # Додаємо сортування для уникнення UnorderedObjectListWarning
        queryset = queryset.order_by('-priority')  # або інше поле

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskFilterForm(self.request.GET or None)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskFilterForm(self.request.GET or None)
        return context

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

