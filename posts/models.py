from django.db import models
from users.models import CustomUser

class Post(models.Model):
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
	category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
	date = models.DateTimeField("Дата публикации")
	plus = models.SmallIntegerField("За")
	minus = models.SmallIntegerField("Против")
	local = models.CharField(max_length = 20)
	shop = models.CharField(max_length = 20)
	description = models.CharField("Описание товара", max_length = 100)
	price = models.DecimalField("price", max_digits = 15, decimal_places = 2)
	currency = models.CharField("Валюта", max_length = 100)
	comment_count = models.SmallIntegerField("Количество комментариев")

	def __str__(self):
		return self.description

	class Meta:
		ordering = ['date']

class Media(models.Model):
	post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
	mediaFile = models.FileField(max_length = 100)
	
	def __str__(self):
		return self.mediaFile

class Category(models.Model):
	name = models.CharField("Название категории", max_length = 20)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = "Категории"

class Comment(models.Model):
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
	date = models.DateTimeField("Дата публикации")
	text = models.TextField("Текст комментария")

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = "Комментарии"
