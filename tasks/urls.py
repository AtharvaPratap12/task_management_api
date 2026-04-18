from django.urls import path 
from .views import create_task, get_tasks, get_project_tasks, update_task, delete_task

urlpatterns = [
    path('create/', create_task, name = 'create_task'),
    path('task/', get_tasks, name = 'get_tasks'),
    path('project/<int:project_id>/', get_project_tasks, name = 'get_project_tasks'),
    path('update/<int:pk>/', update_task, name = 'update_task'),
    path('delete/<int:pk>/', delete_task, name = 'delete_task'),
]