# Generated by Django 4.1 on 2023-04-04 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "products",
            "0004_alter_category_image_alter_product_preview_image_and_more",
        ),
        ("cart", "0004_alter_cart_user"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="cartitem",
            unique_together={("cart", "product")},
        ),
    ]
