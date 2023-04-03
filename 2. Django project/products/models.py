from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(
        upload_to="category",
        width_field=200,
        height_field=200,
        null=True,
        blank=True,
    )


class Product(models.Model):
    title = models.CharField(max_length=255)
    category_path = models.TextField()

    def get_categories(self):
        return [int(x) for x in self.category_path.split(" ")]


class CategoryProductRel(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="items"
    )
