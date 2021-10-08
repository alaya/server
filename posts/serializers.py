from rest_framework import serializers
from .models import Post, Media, Category, Comment
from users.models import CustomUser

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source = 'user_id.name')
    #related_name
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    mediaFiles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'category_id', 'date', 'plus',
        'minus', 'local', 'shop', 'description', 'price', 'currency', 'comments', 'mediaFiles', 'comment_count']

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['category_id'] = instance.category_id.name
        return rep

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media 
        fields = ['id', 'mediaFile' ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.ReadOnlyField(source = 'post_id.id')
    user_id = serializers.ReadOnlyField(source = 'user_id.name')

    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'user_id', 'text', 'date']