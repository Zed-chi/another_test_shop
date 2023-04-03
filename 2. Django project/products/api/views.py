from rest_framework import generics
from .serializers import CategorySerializer
from products.models import Category


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
