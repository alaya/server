from django.db import models
from cities_light.models import City, Region
from smart_selects.db_fields import ChainedForeignKey
from .managers import CustomUserManager

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
	name = models.CharField("Имя Фамилия", max_length = 50)
	login = models.CharField("login", max_length = 20, unique=True)
	email = models.EmailField("email", max_length = 254, unique=True)
	country = models.ForeignKey(Region, on_delete = models.CASCADE)
	city = ChainedForeignKey(City, chained_field="country", chained_model_field="country", 
		show_all=False,
        auto_choose=True,
        sort=True)
	description = models.CharField("О себе", max_length = 254)
	avatar = models.ImageField(upload_to='uploads/', height_field = None , width_field = None , max_length = 100)

    #is_staff = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    
	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name', 'login', 'country', 'city']

	def __str__(self):
		return self.email 

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
