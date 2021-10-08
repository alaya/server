#Модель списка друзей
class FriendList(models.Model):
	friend = models.ManyToMany(CustomUser, null = True)
	owner = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'owner', null = True)

	def make_friend(cls, owner, new_friend):
        friend,create = cls.objects.get_or_create(owner = owner)
        friend.users1.add(new_friend)

    def lose_friend(cls, owner, new_friend):
        friend, create = cls.objects.get_or_create(owner = owner)
        friend.friend.remove(new_friend)

#Модель запросов на дружбу
class Friendship(models.Model):
	created = models.DateTimeField(default=timezone.now)
	from_user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'from_user', null = True)
	to_user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'to_user', null = True)

	class Meta:
        verbose_name = "Friendship Request"
        verbose_name_plural = "Friendship Requests"
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
        verbose_name = "Friend"
        verbose_name_plural = "Friends"
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