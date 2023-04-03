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
    category = models.ForeignKey(to, on_delete)
