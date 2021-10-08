from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from .models import FriendList, FriendRequest
from users.models import CustomUser
from . import serializers

# Список МОИХ друзей пользователя
class FriendsList(generics.ListAPIView):
	serializer_class = serializers.FriendListSerializer

	def get_queryset(self):
		user_id = self.request.user.pk
		#my_friend = user_id.friend.all()
		#user_id = self.kwargs['pk']
		#FriendList.objects.filter(pk = user_id)
		return FriendList.objects.filter(owner = user_id)
#Список друзей пользователя
class FriendsUserList(generics.ListAPIView):
	serializer_class = serializers.FriendListSerializer

	def get_queryset(self):
		user_id = self.kwargs['pk']
		#FriendList.objects.filter(pk = user_id)
		return FriendList.objects.filter(owner = user_id)

# Удалить пользователя из друзей		
class FriendDelete(generics.DestroyAPIView):
	serializer_class = serializers.FriendListSerializer

	def get_queryset(self):
		friend_list = FriendList.objects.get(pk = self.kwargs['pk'])
		return friend_list.friend.all()

# Добавить пользователя в друзья
class FriendAdd(generics.ListCreateAPIView):
	serializer_class = serializers.FriendUpdateSerializer
	
	def get_queryset(self):
		# список запросов к одному пользователю
		friend_request = FriendRequest.objects.filter(from_user = self.kwargs['pk'])
		return friend_request

	# Добавить пользователя в друзья / id от кого был запрос
	def perform_create(self, serializer):
		from_user_id = self.kwargs['pk']
		from_user = CustomUser.objects.get(pk = from_user_id)
		to_user_id=self.request.user.pk
		to_user= CustomUser.objects.get(pk = to_user_id)
		FriendList.make_friend(self.request.user, from_user)
		FriendList.make_friend(from_user, self.request.user)

		data1 ={'friend': from_user, 'owner': self.request.user}
		serializer = serializers.FriendListSerializer(data=data1)
		frequest = FriendRequest.objects.filter(from_user=from_user, to_user=self.request.user).first()
		frequest.delete()

		serializer.is_valid()
		serializer.save()

# создание запроса в друзья / id от меня - того кто подает запрос
class FriendRequestCreate(generics.CreateAPIView):
	serializer_class = serializers.FriendRequestSerializer

	def perform_create(self, serializer):
		to_user_id = self.kwargs['pk']
		to_user = CustomUser.objects.get(pk = to_user_id)
		serializer.save(from_user = self.request.user, to_user = to_user)

# список запросов текущему пользователю
class FriendRequestList(generics.ListAPIView):
	serializer_class = serializers.FriendRequestSerializer

	def get_queryset(self):
		friend_request = FriendRequest.objects.filter(to_user = self.kwargs['pk'])
		return friend_request
		#.from_user.all()


# отклонить запрос 
# удаление записи запроса из БД
class FriendReject(generics.RetrieveDestroyAPIView):
	serializer_class = serializers.FriendRequestSerializer

	def get_queryset(self):
		# сейчас получает список вообще всех запросов (?)
		return FriendRequest.objects.all()

	def perform_destroy(self, instance):
		instance.delete()

#Отменить запрос который мы ранее послали / id кому был отправлен запрос
class FriendRequestCancel(generics.RetrieveDestroyAPIView):
	serializer_class = serializers.FriendRequestSerializer

	def perform_destroy(self, instance):
		to_user_id = self.kwargs['pk']
		to_user = CustomUser.objects.get(pk = to_user_id)
		frequest = FriendRequest.objects.filter(
				from_user=self.request.user,
				to_user=to_user).first()
		frequest.delete()

	def get_queryset(self):
		# сейчас получает список вообще всех запросов (?)
		return FriendRequest.objects.all()