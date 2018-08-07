from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('__all__')


class ValidateUsersRegister(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=15, min_length=5)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, max_length=128)
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=30)
    academic_level = serializers.CharField(required=True, max_length=30)
    address = serializers.CharField(required=True, max_length=150)
    city = serializers.CharField(required=True, max_length=30)
    country = serializers.CharField(required=True, max_length=30)


class ValidateUsersUpdate(serializers.Serializer):
    id_user = serializers.IntegerField(required=True)
    academic_level = serializers.CharField(required=True, max_length=30)
    address = serializers.CharField(required=True, max_length=150)
    city = serializers.CharField(required=True, max_length=30)
    country = serializers.CharField(required=True, max_length=30)
