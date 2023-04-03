from django.contrib import admin
from .models import Product, Category, CategoryProductRel
from .forms import ProductForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

    def save_model(self, request, obj, form, change):
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

        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(CategoryProductRel)
