from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #добавим кнопку «Log in» в графическое представление API
    path('api-auth/', include('rest_framework.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('cities_light/api/', include('cities_light.contrib.restframework3')),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('friends/', include('friends.urls')),
]