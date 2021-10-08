from django.urls import include, path
#из текущего пакета импортируем сожержание views.py в urls.py
from . import views
from django.conf import settings
from django.conf.urls.static import static

'''
Объединение представлений с этими URL-паттернами создает эндпоинты:
get posts/,
post posts/,
get posts/<int:pk>/,
put posts/<int:pk>/
и delete posts/<int:pk>/.
'''
urlpatterns = [
    #get metod READ
    #list
    path('', views.PostList.as_view()),
    #Список постов отфильтрованных по городу просматривающего
    path('list-city/<str:local>/', views.PostListLocalFilter.as_view(), name='postlist-city'),
    #Список постов пользователя для отображения в профиле
    path('list-user/<int:pk>/', views.PostListUserFilter.as_view(), name='postlist-user'),
    path('create/', views.PostCreate.as_view(), name='create-post'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail-post'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='update-post'),
    path('<int:pk>/comments', views.CommentList.as_view(), name='comments'),
    #path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('categories/', views.CategoryDetail.as_view(), name='categories'),
    path('media/', views.MediaDetail.as_view(), name='media-file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)