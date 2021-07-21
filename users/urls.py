from django.urls import include, path
#из текущего пакета импортируем сожержание views.py в urls.py
from . import views

urlpatterns = [
	#добавим кнопку «Log in» в графическое представление API
	path('api-auth/', include('rest_framework.urls')),
	#post metod CREATE
	path('create/', views.UserCreate.as_view(), name = 'create-user'),
	#get metod READ
	path('', views.UserList.as_view()),
	#get metod READ
	path('<int:pk>/', views.UserDetail.as_view(), name = 'retrieve-user'),
	#put metod UPDATE
	path('update/<int:pk>/', views.UserUpdate.as_view(), name = 'update-user'),
	#delete metod DELETE
	path('delete/<int:pk>/', views.UserDelete.as_view(), name = 'delete-user'),
]