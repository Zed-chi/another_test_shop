from rest_framework import serializers
from products.models import Product, Category, CategoryProductRel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "slug", "image", "parent"]
