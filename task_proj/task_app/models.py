from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=[
        ('in_progress', 'In Progress'),
        ('done', 'Done')])
    priority = models.CharField(max_length=10, choices=[
        ('low', 'Low'),
        ('mid', 'Mid'),
        ('high', 'High')
    ])
    deadline = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    dislikes = models.ManyToManyField(User, related_name='post_dislikes')

    def __str__(self):
        return f"Comment by {self.author.username} on {self.task.name}"