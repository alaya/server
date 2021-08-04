from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, RegistrationForm, UserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_form = UserCreationForm
	form = UserChangeForm
	model = CustomUser
	list_display = ['name', 'login', 'email', 'password', 'country', 'city']
	list_filter = ('is_superuser',)
	search_fields = ('name', 'login', 'email')
	ordering = ('email',)

	fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'login', 'country', 'city')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
        )
	add_fieldsets = (
		(None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
		('Personal info', {'fields': ('name', 'login', 'country', 'city')}),
		('Groups', {'fields': ('groups',)}),
		('Permissions', {'fields': ('user_permissions',)}),
		)
 

admin.site.register(CustomUser, CustomUserAdmin)