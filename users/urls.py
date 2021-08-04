from django.urls import include, path
#из текущего пакета импортируем сожержание views.py в urls.py
from . import views

urlpatterns = [
	#post metod CREATE
	path('create/', views.UserCreate.as_view(), name = 'create-user'),
	path('login',  views.UserList.as_view(), name = 'auth'),
	#get metod READ
	path('', views.UserList.as_view()),
	#get metod READ
	path('<int:pk>/', views.UserDetail.as_view(), name = 'retrieve-user'),
	#put metod UPDAT
	path('update/<int:pk>/', views.UserUpdate.as_view(), name = 'update-user'),
	#delete metod DELETE
	path('delete/<int:pk>/', views.UserDelete.as_view(), name = 'delete-user'),
    path('cities_light/api/', include('cities_light.contrib.restframework3')),
]