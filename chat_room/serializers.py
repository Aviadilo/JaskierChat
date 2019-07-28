from rest_framework import serializers
from chat_room.models import Room
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializers(serializers.ModelSerializer):
    room_creator = UserSerializer()
    invited_users = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ('room_creator', 'invited_users', 'created_date')
