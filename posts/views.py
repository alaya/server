from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from rest_framework import generics, permissions
from .models import Post, Media, Category, Comment
from . import serializers
from .permissions import IsOwnerOrReadOnly
from .forms import CreatePostForm, CreateMedia

#Shows ONLY List all of posts without filters
class PostList(generics.ListAPIView):
	#представление будет использоваться для get и post
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer
	#разрешение создавать для авторизированных
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(user_id = self.request.user)

#ONLY Create new post
class PostCreate(generics.CreateAPIView):
	#представление будет использоваться для get и post
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer
	#разрешение создавать для авторизированных
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	form_class = CreatePostForm

	def perform_create(self, serializer):
		serializer.save(user_id = self.request.user)

#Show detail for one object. ONLY READ
class PostDetail(generics.RetrieveAPIView):
	#представление будет использовать get, update и delete для одной сущности
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer
	#разрешение просматривать только зарегистрированным пользователям
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#Read/update/delete post ONLY OWNER
class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
	#представление будет использовать get, update и delete для одной сущности
	queryset = Post.objects.all()
	serializer_class = serializers.PostSerializer
	#разрешение редактировать/удалять только владельцам поста
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class MediaDetail(generics.ListAPIView):
	#представление будет использовать get, update и delete для одной сущности
	queryset = Media.objects.all()
	serializer_class = serializers.MediaSerializer
	form_class = CreateMedia

#Read and Create comment for ONE POST
class CommentList(generics.ListCreateAPIView):
	serializer_class = serializers.CommentSerializer
	#ТОЛЬКО авторизованным
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	
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
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class CategoryDetail(generics.ListAPIView):
	#список категорий
	queryset = Category.objects.all()
	serializer_class = serializers.CategorySerializer