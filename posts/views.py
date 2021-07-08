from django.shortcuts import render
from rest_framework import generics
from .models import Post, Media, Category, Comment
from . import serializers

class PostCreate(generics.CreateAPIView):
	#представление для создания нового объекта 
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer

class PostList(generics.ListAPIView):
	#представление будет использоваться для перечисления всех постов в базе данных
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer

class PostDetail(generics.RetrieveAPIView):
	#представление будет использоваться для поста в базе данных
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer

class PostUpdate(generics.RetrieveUpdateAPIView):
	#представление позволяет обновлять записи в БД
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer

class PostDelete(generics.RetrieveDestroyAPIView):
	#представление позволяет удалять записи  в БД
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer