from django.db import models
from django.utils import timezone
from users.models import CustomUser

#Модель списка друзей
class FriendList(models.Model):
    friend = models.ManyToManyField(CustomUser, blank=True, related_name = 'friend')
    owner = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'owner')

    class Meta:
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'

    def __str__(self):
        return self.owner.name
    
    @classmethod
    def make_friend (cls, current_user, new_friend): 
        friends, create = cls.objects.get_or_create( 
            owner = current_user 
        ) 
        friends.friend.add(new_friend) 
        friends.save()
        return True

#Модель запросов на дружбу
class FriendRequest(models.Model):
    created = models.DateTimeField(default=timezone.now)
    from_user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'from_user')
    to_user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'to_user')

    class Meta:
        verbose_name = 'Friendship Request'
        verbose_name_plural = 'Friendship Requests'
        unique_together = ("from_user", "to_user")

    def __str__(self):
        return "%s" % self.from_user

    def save(self, *args, **kwargs):
        # Пользователь не может дружить сам с собой
        if self.to_user == self.from_user:
            raise ValidationError("Users cannot be friends with themselves.")
        super(FriendRequest, self).save(*args, **kwargs)
