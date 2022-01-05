from django.utils.decorators import method_decorator
from .models import Project, Task
from .serializer import ProjectSerializer, TaskSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ProjectList(APIView):

    def get(self, request, format=None):
        projects = Project.objects.all()
        if projects is None:
            return Response({"error": "No Data Found"}, status=status.HTTP_204_NO_CONTENT)

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class ProjectDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            snippet = Project.objects.get(project_id=pk)

        except:
            print("error")
            return Response("Data Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(snippet)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            snippet = Project.objects.get(project_id=pk)
        except:
            return Response("Data Not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            project = Project.objects.get(project_id=pk)
        except:
            return Response("Data Not Found", status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response({"success": "Delete successfully"}, status=status.HTTP_204_NO_CONTENT)


@method_decorator(csrf_exempt, name='dispatch')
class TaskList(APIView):

    def get(self, request, format=None):
        task = Task.objects.all()
        if task is None:
            return Response("No Data Found", status=status.HTTP_204_NO_CONTENT)

        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("saveeeee")
            return Response({"success": "saved data", "code": 1}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class TaskDetail(APIView):

    def get(self, request, pk, format=None):
        try:

            snippet = Task.objects.get(id=pk)
        except:
            return Response("Data Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            snippet = Task.objects.get(id=pk)
        except:
            return Response("Data Not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):

        try:
            task = Task.objects.get(id=pk)
        except:

            return Response("Data Not Found", status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response({"success": 1}, status=status.HTTP_204_NO_CONTENT)
