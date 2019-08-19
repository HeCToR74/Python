from rest_framework import serializers
from .models import Action, Customer
from datetime import datetime

class ActionSerializer(serializers.Serializer):
    point = serializers.IntegerField()
    description = serializers.CharField()
    date = serializers.DateTimeField(default=datetime.now())
    name_id = serializers.IntegerField()

    def create(self, validated_data):
        return Action.objects.create(**validated_data)

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    balance = serializers.IntegerField()

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance

