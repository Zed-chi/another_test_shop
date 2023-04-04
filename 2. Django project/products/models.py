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
    title = models.CharField(
        max_length=255, verbose_name="Название", unique=True
    )
    category_path = models.TextField(verbose_name="Входит в категории")
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(
        upload_to="products",
        blank=True,
        null=True,
    )
    thumb_image = models.ImageField(
        upload_to="products",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"#{self.id} - {self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["id"]


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product")


class ProductThumb(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="thumb"
    )
    image = models.ImageField(upload_to="product")


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
