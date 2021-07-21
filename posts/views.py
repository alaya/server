from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post, Media, Category, Comment
from . import serializers
from .permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
	#представление будет использоваться для get и post
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer
	#разрешение создавать для авторизированных
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user_id = self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	#представление будет использовать get, update и delete для одной сущности
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer
	#разрешение редактировать/удалять только владельцам поста
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = serializers.CommentSerializer
	#ТОЛЬКО авторизованным
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user_id = self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = serializers.CommentSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class CategoryDetail(generics.ListAPIView):
	#список категорий
	queryset = Category.objects.all()
	serializer_class = serializers.CategorySerializer