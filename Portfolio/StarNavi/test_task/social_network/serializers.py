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

    def update(self, instance, validated_data):
    	instance.title = validated_data.get('title', instance.title)
    	instance.body = validated_data.get('body', instance.body)
    	instance.like = validated_data.get('like', instance.like)
    	instance.unlike = validated_data.get('unlike', instance.unlike)
    	instance.author_id = validated_data.get('author_id', instance.author_id)
    	instance.save()
    	return instance

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return User.objects.create(**validated_data)