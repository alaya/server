import jwt
import datetime
from django.db import models
from cities_light.models import City, Country
from smart_selects.db_fields import ChainedForeignKey
from .managers import CustomUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
	name = models.CharField("Имя Фамилия", max_length=50)
	login = models.CharField("login", max_length=20, unique=True)
	email = models.EmailField("email", max_length=254, unique=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	city = ChainedForeignKey(City, 
		chained_field='country', 
		chained_model_field='country', 
		show_all=False, 
		auto_choose=True, 
		sort=True)
	description = models.CharField("О себе", max_length = 254, null=True)
	avatar = models.ImageField(upload_to='uploads/', height_field=None , width_field = None , max_length = 100, null=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)  # a superuser
    
	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name', 'login', 'country', 'city']

	def __str__(self):
		return self.email 

	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.login

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'