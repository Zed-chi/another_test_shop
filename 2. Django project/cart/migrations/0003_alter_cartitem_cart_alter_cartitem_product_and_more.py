# Generated by Django 4.1 on 2023-04-04 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "products",
            "0004_alter_category_image_alter_product_preview_image_and_more",
        ),
        ("cart", "0002_alter_cart_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="cart.cart",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart_items",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
