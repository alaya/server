from django.urls import include, path
#из текущего пакета импортируем сожержание views.py в urls.py
from . import views

urlpatterns = [
	#post metod CREATE
	path('create/', views.UserCreate.as_view(), name = 'create-user'),
	#get metod READ all users
	path('', views.UserList.as_view(),name = 'users-list'),
	#auth from main path('api-auth/', include('rest_framework.urls')),
	#path('login/', include('rest_framework.urls'), name = 'auth'),
	#get metod READ
	path('<int:pk>/', views.UserDetail.as_view(), name = 'retrieve-user'),
	#put metod UPDAT
	path('update/<int:pk>/', views.UserUpdate.as_view(), name = 'update-user'),
	#delete metod DELETE
	path('delete/<int:pk>/', views.UserDelete.as_view(), name = 'delete-user'),
	#cities filter
	path('cities_filter/<int:pk>/', views.CityFilter.as_view(), name = 'cities_filter')
]