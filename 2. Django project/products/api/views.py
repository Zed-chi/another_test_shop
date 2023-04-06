from products.models import Category
from rest_framework import generics

from .serializers import CategorySerializer


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
