from rest_framework import serializers
from .models import CustomUser
from .forms import RegistrationForm, UserCreationForm
from cities_light.models import City, Country
from posts.models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    #related_name
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['pk', 'name', 'login', 'email', 'country', 'city', 
        'description', 'avatar', 'posts', 'comments', 
        'is_staff', 'is_superuser',
        'password1', 'password2' ]

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep['country'] = instance.country.name
        rep['city'] = instance.city.name
        return rep

    def create(self, validated_data):
        password1 = validated_data.pop('password1', '')
        password2 = validated_data.pop('password2', '')

        if password1 and password2 and password1 != password2:
            raise ValidationError('password mismatch')

        user = CustomUser.objects.create(**validated_data)
        user.set_password(password1)
        user.save()
        return user