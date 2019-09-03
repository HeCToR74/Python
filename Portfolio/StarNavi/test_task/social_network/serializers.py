from rest_framework import serializers
from .models import Post, User

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    like = serializers.IntegerField()
    unlike = serializers.IntegerField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return User.objects.create(**validated_data)