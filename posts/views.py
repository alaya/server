from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from rest_framework import generics, permissions
from .models import Post, Media, Category, Comment
from users.models import CustomUser
from . import serializers
from .permissions import IsOwnerOrReadOnly

#Shows ONLY List all of posts without filters
#представление будет использоваться для get и post
class PostList(generics.ListAPIView):
	serializer_class = serializers.PostSerializer
	#разрешение создавать только для авторизированных
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user_id = self.request.user)

	def get_queryset(self):
		return Post.objects.all()	

#Список постов отфильтрованных по городу проживания пользователя
class PostListLocalFilter(generics.ListAPIView):
	serializer_class = serializers.PostSerializer
	def get_queryset(self):
		post_local = self.kwargs['local']
		#user_city = CustomUser.objects.get(city=post_local)
		return Post.objects.filter(local=post_local)

#Список постов пользователя для отображения в профиле
class PostListUserFilter(generics.ListAPIView):
	serializer_class = serializers.PostSerializer

	def get_queryset(self):
		user = self.kwargs['pk']
		return Post.objects.filter(user_id=user)

#ONLY Create new post
class PostCreate(generics.CreateAPIView):
	serializer_class = serializers.PostSerializer
	#разрешение создавать для авторизированных

	def perform_create(self, serializer):
		serializer.save(user_id = self.request.user)

	def get_queryset(self):
		return Post.objects.all()

#Show detail for one object. ONLY READ
class PostDetail(generics.RetrieveAPIView):
	serializer_class = serializers.PostSerializer
	#разрешение просматривать только зарегистрированным пользователям

	def get_queryset(self):
		return Post.objects.all()

#Read/update/delete post ONLY OWNER
class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
	#представление будет использовать get, update и delete для одной сущности
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer
	#разрешение редактировать/удалять только владельцам поста
	permission_classes = [IsOwnerOrReadOnly]

class MediaDetail(generics.ListAPIView):
	#представление будет использовать get, update и delete для одной сущности
	queryset = Media.objects.all()
	serializer_class = serializers.MediaSerializer

#Read list and Create comment for ONE POST
class CommentList(generics.ListCreateAPIView):
	serializer_class = serializers.CommentSerializer
	#ТОЛЬКО авторизованным
	
	def perform_create(self, serializer):
		post_id = self.kwargs['pk']
		post = Post.objects.get(pk = post_id)
		serializer.save(user_id = self.request.user, post_id = post)

	def get_queryset(self):
		post_id = self.kwargs['pk']
		post = Post.objects.get(pk = post_id)
		return post.comments.all()

#Read/update/delete comment ONLY OWNER
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = serializers.CommentSerializer
	permission_classes = [IsOwnerOrReadOnly]

class CategoryDetail(generics.ListAPIView):
	#список категорий
	queryset = Category.objects.all()
	serializer_class = serializers.CategorySerializer