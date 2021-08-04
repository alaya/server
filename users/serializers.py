from rest_framework import serializers
from .models import CustomUser
from cities_light.models import City, Country
from posts.models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['pk', 'name', 'login', 'email', 'password', 'country', 'city', 'description', 'avatar', 'posts', 'comments']

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep['country'] = instance.country.name
        rep['city'] = instance.city.name
        return rep