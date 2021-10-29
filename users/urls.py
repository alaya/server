from django.urls import include, path
#из текущего пакета импортируем сожержание views.py в urls.py
from . import views

urlpatterns = [
	#post metod CREATE
	path('create/', views.UserCreate.as_view(), name = 'create-user'),
	#post metod login
	path('login/', views.LoginAPIView.as_view(), name = 'login-user'),
	#post metod refresh
	path('relogin/', views.refresh_token_view, name = 'refrash-token'),
	#get metod READ all users
	path('', views.UserList.as_view(),name = 'users-list'),
	#get metod READ
	path('<int:pk>/', views.UserDetail.as_view(), name = 'retrieve-user'),
	#put metod UPDAT
	path('update/<int:pk>/', views.UserUpdate.as_view(), name = 'update-user'),
	#delete metod DELETE
	path('delete/<int:pk>/', views.UserDelete.as_view(), name = 'delete-user'),
	#cities filter
	path('cities_filter/<int:pk>/', views.CityFilter.as_view(), name = 'cities_filter') 
]


