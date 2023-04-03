from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=255, unique=True, verbose_name="Название"
    )
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Надкатегория",
    )
    image = models.ImageField(
        upload_to="category",
        width_field=200,
        height_field=200,
        null=True,
        blank=True,
        verbose_name="Изображение",
    )

    def __str__(self):
        return f"#{self.id} - {self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]


class Product(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", unique=True
    )
    category_path = models.TextField(verbose_name="Входит в категории")

    def __str__(self):
        return f"#{self.id} - {self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["id"]


class CategoryProductRel(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="items"
    )

    class Meta:
        verbose_name = "Связь Продукт-Категория"
        verbose_name_plural = "Связи Продукт-Категория"
        unique_together = (
            "category",
            "product",
        )

    def __str__(self):
        return f"[{self.category}] - {self.product.title}"
