from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import TaskList, TaskDetail, CreateTask, DeleteTask, UpdateTask, CommentDelete, CommentUpdate, LikeView, DislikeView

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('tasks/task/<int:pk>/', TaskDetail.as_view(), name= 'task_detail'),
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path('delete/task/<int:pk>', DeleteTask.as_view(), name='delete_task'),
    path('update/task/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('comment/delete/<int:pk>', CommentDelete.as_view(), name='comment_delete'),
    path('comment/update/<int:pk>', CommentUpdate.as_view(), name='comment_update'),
    path('like/<int:pk>', LikeView.as_view(), name='like_comment'),
    path('dislike/<int:pk>', DislikeView.as_view(), name='dislike_comment'),
    path('login/', LoginView.as_view(template_name = "task_app/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name = "login"), name="logout")
]