from rest_framework import serializers
from .models import ToDo
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'user']

    def create(self, validate_data):
        print("Creating ToDo with data:", validate_data)
        user = self.context["request"].user
        return ToDo.objects.create(user=user, **validate_data)
    

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.is_active = True
        user.set_password(validated_data['password'])
        user.save()
        return user