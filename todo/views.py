from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import ToDo
from .serializer import TodoSerializer, RegisterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
# Create your views here.

class ToDoListCreateView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['is_completed', 'title']

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']    
    ordering_fields = ['created_at', 'title']

    def get_queryset(self):
        return  ToDo.objects.filter(user=self.request.user).order_by("-created_at")

class ToDoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer