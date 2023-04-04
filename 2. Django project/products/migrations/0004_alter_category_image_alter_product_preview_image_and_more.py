# Generated by Django 4.1 on 2023-04-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_category_image_alter_product_preview_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="category", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="preview_image",
            field=models.ImageField(blank=True, null=True, upload_to="products"),
        ),
        migrations.AlterField(
            model_name="product",
            name="thumb_image",
            field=models.ImageField(blank=True, null=True, upload_to="products"),
        ),
    ]
