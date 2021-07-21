from django.contrib import admin
from .models import Post, Category, Media, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'category_id', 'date', 'plus', 'minus', 'local', 'shop', 'description', 'price', 'currency', 'comment_count')
	list_filter = ()
	exclude = []

admin.site.register(Category) 
admin.site.register(Media)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin) 
