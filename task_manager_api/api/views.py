from rest_framework import generics
from tasks.models import Task
from api.serializers import TaskSerializer
import django_filters.rest_framework as filters


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['completed']


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['completed']
