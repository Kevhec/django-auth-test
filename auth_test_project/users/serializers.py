from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],
                                       first_name=validated_data['first_name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")