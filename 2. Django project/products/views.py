from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product, CategoryProductRel


class ProductListView(ListView):
    pass


class ProductDetailView(DetailView):
    pass


class CategoryListView(ListView):
    queryset = Category.get_root_categories()
    template_name = "products/categories/list.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    template_name = "products/categories/detail.html"
    context_object_name = "category"
