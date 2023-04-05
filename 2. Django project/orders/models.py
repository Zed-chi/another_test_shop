from django.conf import settings
from django.db import models

from cart.models import Cart
from products.models import Product


class Order(models.Model):
    STATUSES = (
        ("draft", "draft"),
        ("paid", "paid"),
        ("shipped", "shipped"),
        ("delivered", "delivered"),
        ("refunding", "refunding"),
        ("refunded", "refunded"),
    )
    PAYMENT_CHOICES = [
        ("CASH", "Наличными"),
        ("CARD", "Электронно"),
    ]
    payment = models.CharField(
        verbose_name="Вид оплаты",
        choices=PAYMENT_CHOICES,
        default="CARD",
        max_length=30,
    )
    firstname = models.CharField(verbose_name="Имя", max_length=30)
    lastname = models.CharField(verbose_name="Фамилия", max_length=50)
    phonenumber = models.CharField(verbose_name="Номер телефона", max_length=32)
    comment = models.TextField(
        verbose_name="Комментарий к заказу", blank=True, default=""
    )
    address = models.TextField(verbose_name="Адрес доставки")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    status = models.CharField(
        verbose_name="Статус заказа", max_length=255, choices=STATUSES, default="draft"
    )
    total_price = models.DecimalField(
        verbose_name="Общая сумма", decimal_places=2, max_digits=10
    )
    shipping_price = models.DecimalField(
        verbose_name="Сумма доставки", decimal_places=2, max_digits=10
    )
    delivered_at = models.DateTimeField(
        verbose_name="Дата доставки", null=True, blank=True
    )
    refunded_at = models.DateTimeField(
        verbose_name="Дата возврата", null=True, blank=True
    )
    handled_at = models.DateTimeField(
        verbose_name="Дата обработки", null=True, blank=True
    )

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items", verbose_name="Заказ"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="Продукт",
    )
    quantity = models.IntegerField(verbose_name="Количество", default=1)
    item_price = models.DecimalField(
        verbose_name="Сумма заказа", decimal_places=2, max_digits=10
    )

    class Meta:
        unique_together = ["order", "product"]

    def total_price(self):
        return self.item_price * self.quantity
