from django.urls import path 
from .views import create_task, get_tasks, get_project_tasks, update_task, delete_task, update_task_status, update_task_priority, task_analytics

urlpatterns = [
    path('create/', create_task, name = 'create_task'),
    path('task/', get_tasks, name = 'get_tasks'),
    path('project/<int:project_id>/', get_project_tasks, name = 'get_project_tasks'),
    path('update/<int:pk>/', update_task, name = 'update_task'),
    path('delete/<int:pk>/', delete_task, name = 'delete_task'),
    path('update_status/<int:pk>/', update_task_status, name = 'update_task_status'),
    path('update_priority/<int:pk>/', update_task_priority, name = 'update_task_priority'),
    path('task_analytics/', task_analytics, name = 'task_analytics'),
]