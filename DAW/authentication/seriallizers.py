from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['username', 'password', 'email', 'is_staff', 'is_superuser']


class UserMoreInfoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['first_name', 'last_name', 'birth_date']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(username=clean_data['username'], password=clean_data['password'])
        if not user:
            raise ValidationError('user not found')
        return user
