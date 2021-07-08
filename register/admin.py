from django.contrib import admin
from .models import CustomUser, UserData

admin.site.register(CustomUser, UserData)
