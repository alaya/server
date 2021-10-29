from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from cities_light.models import City, Country
from posts.models import Post, Comment

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    #related_name
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['pk', 'name', 'login', 'email', 'country', 'city', 
        'description', 'avatar', 'posts', 'comments', 
        'is_staff', 'is_superuser',
        'password1', 'password2', 'token' ]

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

class CityCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['pk', 'name', 'country']

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=128)
    name = serializers.CharField(max_length=128, read_only = True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        '''
        # Вызвать исключение, если не предоставлена почта.
        if email is None:
            raise serializers.ValidationError('An email address is required to log in.')
        # Вызвать исключение, если не предоставлен пароль.
        if password is None:
            raise serializers.ValidationError('A password is required to log in.')
        '''
        user = authenticate(username = email, password = password)
        
        if (user is None):
            raise serializers.ValidationError('A user with this email and password was not found.')

        if (email is None) or (password is None):
            raise exceptions.AuthenticationFailed('email and password required')

        if (user is None):
            raise exceptions.AuthenticationFailed('user not found')
        if (not user.check_password(password)):
            raise exceptions.AuthenticationFailed('wrong password')
        
        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)
        
        return {
            'email': user.email,
            'name': user.name,
            'token': access_token
        }