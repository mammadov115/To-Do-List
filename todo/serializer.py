from rest_framework import serializers
from .models import ToDo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'user']

    def create(self, validate_data):
        print("Creating ToDo with data:", validate_data)
        user = self.context["request"].user
        return ToDo.objects.create(user=user, **validate_data)