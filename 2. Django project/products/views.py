from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product, CategoryProductRel


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
    context_object_name = "product"


class CategoryListView(ListView):
    queryset = Category.get_root_categories()
    template_name = "products/categories/list.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    template_name = "products/categories/detail.html"
    context_object_name = "category"
