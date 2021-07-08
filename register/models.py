from django.db import models

class CustomUser(models.Model):
	name = models.CharField("Name", max_length = 50)
	login = models.CharField("login", max_length = 20)
	email = models.EmailField("email", max_length = 254)
	password = models.CharField("password", max_length = 20)
	country_cod = models.ForeignKey(Country)
	city_cod = models.ForeignKey(City)

	def __str__(self):
		return self.name

class UserData(models.Model):
	user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	gender = models.CharField("Пол", max_length = 5)
	description = models.CharField("О себе", max_length = 254)
	avatar = models.ForeignKey(Media)

	def __str__(self):
		return self.name 

class Country(models.Model):
	cod = models.CharField("Код страны", max_length=3)
	country = models.CharField("Страна", max_length=50)

	def __str__(self):
		return self.country 

class City(models.Model):
	country_cod = models.ForeignKey(Country)
	cod = models.CharField("Код страны", max_length=3)
	city = models.CharField("Город", max_length=50)

	def __str__(self):
		return self.city 

#Модель запросов на дружбу
class Friendship(models.Model):
	created = models.DateTimeField(default=timezone.now)
	friend_from = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'friendship_creator_set')
	friend_to = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'friend_set')

	class Meta:
        verbose_name = _("Friendship Request")
        verbose_name_plural = _("Friendship Requests")
        unique_together = ("friend_from", "friend_to")

    def __str__(self):
        return "%s" % self.friend_from_id

	#Подтверждение запроса
	def accept(self):
		Friend.object.create(friend_from = self.friend_from, friend_to = self.friend_to)
		Friend.object.create(friend_from = self.friend_to, friend_to = self.friend_from)


#Модель дружеских отношений
class Friend(models.Model):	
	created = models.DateTimeField(default=timezone.now)
	friend_from = models.ForeignKey(CustomUser, models.CASCADE, related_name = 'friends')
	friend_to = models.ForeignKey(CustomUser, models.CASCADE, related_name = '_unused_friend_relation')
	
	object = FriendshipManager()

	class Meta:
        verbose_name = _("Friend")
        verbose_name_plural = _("Friends")
        unique_together = ("friend_from", "friend_to")

    def __str__(self):
        return "User #%s is friends with #%s" % (self.friend_to_id, self.friend_from_id)

    def save(self, *args, **kwargs):
        # Пользователь не может дружить сам с собой
        if self.friend_to == self.friend_from:
            raise ValidationError("Users cannot be friends with themselves.")
        super(Friend, self).save(*args, **kwargs)

#Модель управления отношениями
class FriendshipManager(models.Model):
	pass