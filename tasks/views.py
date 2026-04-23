from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task 
from django.shortcuts import get_object_or_404
from projects.models import ProjectMember, Project
# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    project_id = request.data.get('project')

    project = get_object_or_404(Project, id = project_id)

    if not is_project_member(request.user, project):
        return Response({"error": "Not Authorized"}, status = 403)

    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    tasks = Task.objects.filter(assigned_to = request.user)

    search = request.GET.get('search')
    if search:
        tasks = tasks.filter(title__icontains = search)

    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status = status)

    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority = priority)
    
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project_tasks(request, project_id):
    project = get_object_or_404(Project, id = project_id)

    if not is_project_member(request.user, project):
        return Response({"error": "Not Authorized"}, status = 403)

    tasks = Task.objects.filter(pk = project_id)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, pk):
    task = get_object_or_404(Task,pk = pk)
    project = task.project

    if not is_project_member(request.user, project):
        return Response({"error": "Not Authorized"}, status = 403)

    serializer = TaskSerializer(task, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    task = get_object_or_404(Task, pk = pk)
    project = task.project

    if not is_project_member(request.user, project):
        return Response({"error": "Not Authorized"}, status = 403)

    task.delete()
    return Response({'message': 'Task is deleted successfully'})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk = pk)
    new_status = request.data.get('status')

    if not new_status:
        return Response({"error": "Status is required"})

    if new_status not in ['To Do', 'In Progress', 'Done']:
        return Response({'error': "Invalid Status"})

    task.status = new_status
    task.save()

    return Response({"message": "Task status updated successfully "})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task_priority(request, pk):
    task = get_object_or_404(Task, pk = pk)
    new_priority = request.data.get('priority')

    if not new_priority:
        return Response({"error": "Priority is required"})

    if new_priority not in ['Low', 'Medium', 'High']:
        return Response({"error": "Invalid Priority"})

    task.priority = new_priority
    task.save()
    return Response({"message": "Task priority updated successfully"})

def is_project_member(user, project):
    return(
        project.owner == user or
        ProjectMember.objects.filter(project = project, user = user).exists()
    )


    

 

