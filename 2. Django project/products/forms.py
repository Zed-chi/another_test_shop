from django import forms

from products.form_widgets import CategoryListWidget

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            "category_path": CategoryListWidget(),
        }
        fields = [
            "title",
            "category_path",
            "slug",
            "description",
            "price",
            "available",
            "preview_image",
        ]
