from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("Username already exists")
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data["full_name"],
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        return validated_data