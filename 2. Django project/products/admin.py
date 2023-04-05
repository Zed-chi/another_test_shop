from django.contrib import admin

from .forms import ProductForm
from .models import Category, CategoryProductRel, Product, ProductImage


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 3
    verbose_name = "Изображение продукта"
    verbose_name_plural = "Изображения продукта"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ["title", "slug", "price", "available", "created_at"]
    list_filter = ["available", "created_at"]
    prepopulated_fields = {"slug": ["title"]}
    list_editable = ["price", "available"]
    inlines = [ProductImageInline]

    def save_model(self, request, obj, form, change):
        """Additional step for:
        - creating relations
        - updating relations
        """
        super().save_model(request, obj, form, change)
        category_relations = CategoryProductRel.objects.filter(
            product_id=obj.id
        )
        relations_ids = [i.category.id for i in category_relations]
        posted_ids = [int(i) for i in obj.category_path.split(" ")]
        for rel in category_relations:
            if rel.category.id not in posted_ids:
                rel.delete()
        for _id in posted_ids:
            if _id not in relations_ids:
                category = Category.objects.get(id=_id)
                CategoryProductRel.objects.create(
                    product=obj, category=category
                )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(CategoryProductRel)
