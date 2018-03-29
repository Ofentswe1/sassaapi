from rest_framework import serializers
from app import models
from django.contrib.auth.models import User
import json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validate_data):
        username = validate_data.get('username')
        first_name = validate_data.get('first_name')
        last_name = validate_data.get('last_name')
        email = validate_data.get('email')
        password = validate_data.get('password')
        user = User.objects.create(username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   password=password)
        return user
