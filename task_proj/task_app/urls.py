from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import TaskList, TaskDetail, CreateTask, DeleteTask, UpdateTask

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('tasks/task/<int:pk>/', TaskDetail.as_view(), name= 'task_detail'),
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path('delete/task/<int:pk>', DeleteTask.as_view(), name='delete_task'),
    path('update/task/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('login/', LoginView.as_view(template_name = "task_app/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name = "login"), name="logout")
]