from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ToDo
from .serializer import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ToDoListCreateView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_completed', 'title']

    def get_queryset(self):
        return  ToDo.objects.filter(user=self.request.user).order_by("-created_at")

class ToDoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)