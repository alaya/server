from rest_framework import serializers
from .models import CustomUser
from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['pk', 'name', 'login', 'email', 'password', 'country', 'city', 'description', 'avatar']