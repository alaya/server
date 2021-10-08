from django.contrib import admin
from .models import FriendList, FriendRequest

admin.site.register(FriendList) 

class FriendRequestdAdmin(admin.ModelAdmin):
    list_filter = ['from_user', 'to_user']
    list_display = ['from_user', 'to_user']
    search_fields = ['from_user__username', 'to_user__username']
    readonly_fields = ['id',]

    class Meta:
        model = FriendRequest

admin.site.register(FriendRequest, FriendRequestdAdmin)