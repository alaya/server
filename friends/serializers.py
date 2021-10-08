from rest_framework import serializers
from users.models import CustomUser
from .models import FriendList, FriendRequest
from users.serializers import UserSerializer

class FriendListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'user.name')
    friend = UserSerializer(many=True, read_only=True)
    #serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = FriendList
        fields = ['pk', 'friend', 'owner']

    def create(self, validated_data):
        return FriendList(**validated_data)

class FriendUpdateSerializer(serializers.ModelSerializer):
    from_user = serializers.ReadOnlyField(source = 'from_user.name')
    to_user = serializers.ReadOnlyField(source = 'to_user.name')
    class Meta:
        model = FriendRequest
        fields = ['pk', 'from_user', 'to_user']

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = serializers.ReadOnlyField(source = 'from_user.name')
    created = serializers.ReadOnlyField()
    class Meta:
        model = FriendRequest
        fields = ['pk', 'created', 'from_user', 'to_user']

    def to_representation(self, instance):
        rep = super(FriendRequestSerializer, self).to_representation(instance)
        rep['to_user'] = instance.to_user.name
        return rep