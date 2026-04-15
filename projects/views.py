from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    data = request.data.copy()
    data['owner'] = request.user.id

    serializer = ProjectSerializer(data = data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 201)
    return Response(serializer.errors, status = 400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_projects(request):
    projects = Project.objects.filter(owner = request.user)
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_project(request, pk):
    project = get_object_or_404(Project, pk = pk, owner = request.user)
    serializer = ProjectSerializer(project, data = request.data, )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, {"message": "Project updated successfully"}, status = 200)
    return Response(serializer.errors,{"message": "Failed to update project"}, status = 400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_project(request, pk):
    project = get_object_or_404(Project, pk = pk, owner = request.user)
    project.delete()
    return Response({"message": "Project deleted successfully"}, status = 204)