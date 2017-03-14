#from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from rest_framework import filters
from .Serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
	filter_fields = ('completed',)
	ordering = ('-date_created',)

# class DueTaskViewSet(viewsets.ModelViewSet):
# 	queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
# 	serializer_class = TaskSerializer

# class CompletedTaskViewSet(viewsets.ModelViewSet):
# 	queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
# 	serializer_class = TaskSerializer