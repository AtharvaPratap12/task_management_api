from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'projects')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = 'members')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'project_members')
    role = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.role})"
