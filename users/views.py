from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from . import serializers
from cities_light.models import City, Country
from cities_light.contrib.restframework3 import CitySerializer
from .forms import RegistrationForm, UserCreationForm, UserChangeForm


class UserCreate(generics.ListCreateAPIView):
	#представление для POST создания нового объекта клиента
	serializer_class = serializers.UserSerializer
	form_class = RegistrationForm

	def get_queryset(self):
		return CustomUser.objects.all()

	'''
	# проверка пользователя при регистрации на случай если он уже зарегестрирован
	def perform_create(self, serializer):
		queryset = CustomUser.objects.filter(email=self.request.email)
		if queryset.exists():
			raise ValidationError('You have already signed up')
		serializer.save(user=self.request.user)
	'''

class UserList(generics.ListAPIView):
	#представление будет использоваться для перечисления всех пользователей в базе данных
	queryset = CustomUser.objects.all()
	serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
	#представление будет использоваться для одного клиента в базе данных
	queryset = CustomUser.objects.all()
	serializer_class = serializers.UserSerializer

class UserUpdate(generics.RetrieveUpdateAPIView):
	#представление позволяет обновлять записи пользователя в БД
	queryset = CustomUser.objects.all()
	serializer_class = serializers.UserSerializer
	form_class = UserChangeForm

class UserDelete(generics.RetrieveDestroyAPIView):
	#представление позволяет удалять записи пользователя в БД
	queryset = CustomUser.objects.all()
	serializer_class = serializers.UserSerializer

class CityFilter(generics.ListAPIView):
	#serializer_class = CitySerializer
	serializer_class = serializers.CityCustomSerializer
	def get_queryset(self):
		return City.objects.filter(country = self.kwargs['pk'])
		 