from django.urls import include, path
#из текущего пакета импортируем сожержание views.py в urls.py
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #list friends by one user. список друзей одного пользователя +
    path('<int:pk>', views.FriendsUserList.as_view(), name='list-friend'),
    # <MY> list friends. МОЙ список друзей пользователя (+?)
    path('', views.FriendsList.as_view(), name='friend-list'),
    # удалить из дрзей
    path('delete/<int:pk>', views.FriendDelete.as_view(), name='remove-friend'),
    # создать запрос на добавление в друзья +
    path('request/<int:pk>', views.FriendRequestCreate.as_view(), name='send-friend-request'),
    # список запросов текущему пользователю +
    path('request-list/<int:pk>', views.FriendRequestList.as_view(), name='friend-requests_list'),
    # Принять запрос / id пользователя который просится в друзья
    path('accept/<int:pk>', views.FriendAdd.as_view(),  name='friend-request-accept'),
    # Отклонить запрос +/-
    path('reject/<int:pk>', views.FriendReject.as_view(),name='friend-request-reject'),
    #
    path('cancel/<int:pk>', views.FriendRequestCancel.as_view(), name='friend-request-cancel')
    ]