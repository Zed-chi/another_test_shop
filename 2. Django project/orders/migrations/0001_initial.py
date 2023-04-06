# Generated by Django 4.1 on 2023-04-05 15:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0008_alter_productimage_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                    "payment",
                    models.CharField(
                        choices=[
                            ("CASH", "Наличными"),
                            ("CARD", "Электронно"),
                        ],
                        default="CARD",
                        max_length=30,
                        verbose_name="Вид оплаты",
                    ),
                ),
                (
                    "firstname",
                    models.CharField(max_length=30, verbose_name="Имя"),
                ),
                (
                    "lastname",
                    models.CharField(max_length=50, verbose_name="Фамилия"),
                ),
                (
                    "phonenumber",
                    models.CharField(
                        max_length=32, verbose_name="Номер телефона"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        default="",
                        verbose_name="Комментарий к заказу",
                    ),
                ),
                ("address", models.TextField(verbose_name="Адрес доставки")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "draft"),
                            ("paid", "paid"),
                            ("shipped", "shipped"),
                            ("delivered", "delivered"),
                            ("refunding", "refunding"),
                            ("refunded", "refunded"),
                        ],
                        default="draft",
                        max_length=255,
                        verbose_name="Статус заказа",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Общая сумма",
                    ),
                ),
                (
                    "shipping_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Сумма доставки",
                    ),
                ),
                (
                    "delivered_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата доставки"
                    ),
                ),
                (
                    "refunded_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата возврата"
                    ),
                ),
                (
                    "handled_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата обработки"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "заказ",
                "verbose_name_plural": "заказы",
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                    "quantity",
                    models.IntegerField(default=1, verbose_name="Количество"),
                ),
                (
                    "item_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Сумма заказа",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="orders.order",
                        verbose_name="Заказ",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="products.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "unique_together": {("order", "product")},
            },
        ),
    ]
