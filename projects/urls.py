from django.urls import path, include
from .views import create_project, get_projects, update_project, delete_project


urlpatterns = [
    path('', get_projects, name = "get_projects"),
    path('create/', create_project, name = "create_projects"),
    path('<int:pk>/update/', update_project, name = "update_project"),
    path('<int:pk>/delete/', delete_project, name = "delete_projects"),
]