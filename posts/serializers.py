from rest_framework import serializers
from .models import Post, Media, Category, Comment
from users.models import CustomUser

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source = 'user_id.name')
    comments_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category_id = serializers.ReadOnlyField(source = 'category_id.name')
    
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'category_id', 'date', 'plus', 'minus', 'local', 'shop', 'description', 'price', 'currency']

class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media 
        fields = ['id', 'post_id', 'mediaFile' ]

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source = 'user_id.name')

    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'user_id', 'text', 'date']