from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("Todo", "Todo"),
        ("In Progress", "In Progress"),
        ("Done", "Done")
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]

    title = models.CharField(max_length = 200) 
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'tasks')
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = "Todo")
    priority = models.CharField(max_length = 20, choices = PRIORITY_CHOICES, default = "Medium")
    due_date = models.DateField()