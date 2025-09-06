from rest_framework import serializers
from .models import Category, Tag, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = ("id", "name")

class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tag 
        fields = ("id", "name")

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ("id", "name", "description", "category", "tags")

