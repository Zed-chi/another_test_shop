from rest_framework import serializers

from products.models import Category, CategoryProductRel, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "slug", "image", "parent"]
