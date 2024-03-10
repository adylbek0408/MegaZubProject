from rest_framework import serializers
from .models import *


class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class ServicePhotosSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePhotos
        fields = '__all__'
