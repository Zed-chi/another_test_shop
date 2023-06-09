# Generated by Django 4.1 on 2023-04-04 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название"
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        height_field=200,
                        null=True,
                        upload_to="category",
                        verbose_name="Изображение",
                        width_field=200,
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="products.category",
                        verbose_name="Надкатегория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "category_path",
                    models.TextField(verbose_name="Входит в категории"),
                ),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField()),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("available", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="CategoryProductRel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="products.category",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Связь Продукт-Категория",
                "verbose_name_plural": "Связи Продукт-Категория",
                "unique_together": {("category", "product")},
            },
        ),
    ]
