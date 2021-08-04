from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from . import serializers
from .forms import RegistrationForm, UserCreationForm, UserChangeForm


class UserCreate(generics.ListCreateAPIView):
	#представление для POST создания нового объекта клиента
	queryset = CustomUser.objects.all()
	serializer_class = serializers.UserSerializer
	form_class = RegistrationForm

class UserList(generics.ListAPIView):
	#представление будет использоваться для перечисления всех клиентов в базе данных
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