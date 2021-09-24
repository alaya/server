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
    path('', views.PostList.as_view()),
    path('create/', views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/update', views.PostUpdate.as_view()),
    path('<int:pk>/comments', views.CommentList.as_view()),
    #path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryDetail.as_view()),
    path('media/', views.MediaDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)