from rest_framework import serializers

from __init__ import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'img')


class ShopSerializer(serializers.ModelSerializer):
    viloyat = serializers.IntegerField()
    tuman = serializers.IntegerField()
    
    class Meta:
        model = Shop
        fields = ('name', 'description', 'image', 'password', 'viloyat', 'tuman')


