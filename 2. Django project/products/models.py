from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Надкатегория",
        related_name="children",
    )
    image = models.ImageField(
        upload_to="category",
        null=True,
        blank=True,
        verbose_name="Изображение",
    )

    def __str__(self):
        return f"#{self.id} - {self.title}"

    @classmethod
    def get_root_categories(cls):
        return cls.objects.filter(parent=None)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", unique=True)
    category_path = models.TextField(verbose_name="Входит в категории")
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    available = models.BooleanField(default=False, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    preview_image = models.ImageField(
        upload_to="previews", blank=True, null=True, verbose_name="Фото для превью"
    )

    def __str__(self):
        return f"#{self.id} - {self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["id"]


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="Продукт"
    )
    image = models.ImageField(upload_to="product-images/", verbose_name="Изображение")

    class Meta:
        verbose_name = "Связь с изображением"
        verbose_name_plural = "Связь с изображениеми"


class CategoryProductRel(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Категория",
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="items", verbose_name="Продукт"
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
