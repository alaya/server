import jwt
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from .utils import generate_access_token, generate_refresh_token
from .models import CustomUser
from . import serializers
from cities_light.models import City, Country
from cities_light.contrib.restframework3 import CitySerializer

from rest_framework import exceptions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

class UserCreate(generics.CreateAPIView):
	#представление для POST создания нового объекта клиента
	serializer_class = serializers.UserSerializer
	permission_classes = (AllowAny,)

	def get_queryset(self):
		return CustomUser.objects.all()

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

class UserDelete(generics.RetrieveDestroyAPIView):
	#представление позволяет удалять записи пользователя в БД
	queryset = CustomUser.objects.all()
	serializer_class = serializers.UserSerializer

class CityFilter(generics.ListAPIView):
	#serializer_class = CitySerializer
	serializer_class = serializers.CityCustomSerializer
	def get_queryset(self):
		return City.objects.filter(country = self.kwargs['pk'])

class LoginAPIView(APIView):
	permission_classes = (AllowAny,)
	serializer_class = serializers.LoginSerializer
	def post(self, request):
		email = request.data.get('email')
		password = request.data.get('password')
		response = Response()
		if (email is None) or (password is None):
			raise exceptions.AuthenticationFailed(
				'email and password required')

		user = CustomUser.objects.filter(email=email).first()
		if(user is None):
			raise exceptions.AuthenticationFailed('user not found')
		if (not user.check_password(password)):
			raise exceptions.AuthenticationFailed('wrong password')
		serialized_user = serializers.UserSerializer(user).data

		access_token = generate_access_token(user)
		refresh_token = generate_refresh_token(user)

		response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
		response.data = {
			'token': access_token,
			'user': serialized_user,}

		return response


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_protect
def refresh_token_view(request):
	refresh_token = request.COOKIES.get('refreshtoken')
	if refresh_token is None:
		raise exceptions.AuthenticationFailed(
		'Authentication credentials were not provided.')
	try:
		payload = jwt.decode(
			refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		raise exceptions.AuthenticationFailed('expired refresh token, please login again.')

	user = CustomUser.objects.filter(id=payload.get('user_id')).first()
	if user is None:
		raise exceptions.AuthenticationFailed('User not found')

	if not user.is_active:
		raise exceptions.AuthenticationFailed('user is inactive')

	access_token = generate_access_token(user)
	return Response({'token': access_token})
