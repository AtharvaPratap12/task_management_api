from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task 
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    tasks = Task.objects.filter(assigned_to = request.user)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project_tasks(request, project_id):
    tasks = Task.objects.filter(pk = project_id)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, pk):
    task = get_object_or_404(Task,pk = pk)

    serializer = TaskSerializer(task, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.delete()
    return Response({'message': 'Task is deleted successfully'})
 

