from django.contrib import admin
from .models import Product, Category
from .forms import ProductForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
