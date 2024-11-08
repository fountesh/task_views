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