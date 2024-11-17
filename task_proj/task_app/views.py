from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .mixin import UserIsOwnerMixin, UserIsCommentOwnerMixin
from .models import Task, Comment
from .forms import TaskForm, TaskFilterForm, CommentForm
from django.http import HttpResponseRedirect

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['comment_form'] = CommentForm

        return context

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
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
    form_class = TaskForm
    success_url = "/"
    template_name = "task_app/update_task.html"

class CommentDelete(LoginRequiredMixin, UserIsCommentOwnerMixin, DeleteView):
    model = Comment
    template_name = 'task_app/delete_confirm.html'

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={"pk": self.get_object().task.pk})


class CommentUpdate(LoginRequiredMixin, UserIsCommentOwnerMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'task_app/comment_update.html'

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={"pk": self.get_object().task.pk})


class LikeView(LoginRequiredMixin, UpdateView):
    model = Comment

    def post(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.dislikes.filter(id=request.user.id).exists():
            comment.dislikes.remove(request.user)

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.get_object().task.pk})


class DislikeView(LoginRequiredMixin, UpdateView):
    model = Comment

    def post(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)

        if comment.dislikes.filter(id=request.user.id).exists():
            comment.dislikes.remove(request.user)
        else:
            comment.dislikes.add(request.user)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.get_object().task.pk})

class RegisterUser(CreateView):
    template_name = "task_app/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Реєстрація'  
        return context
