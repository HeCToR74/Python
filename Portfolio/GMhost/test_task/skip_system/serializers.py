from rest_framework import serializers
from .models import Enter, Room, Key, Permission


class EnterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'date',
            'user',
            'room',
        )
        model = Enter

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
        )
        model = Room


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'key',
            'user'
            'expired',
            'active'
        )
        model = Key


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'room',            
            'user'
        )
        model = Permission