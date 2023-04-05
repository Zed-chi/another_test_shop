from django.conf import settings
from django.db import models

from cart.models import Cart


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
        "Вид оплаты",
        choices=PAYMENT_CHOICES,
        default="CARD",
        max_length=30,
    )
    firstname = models.CharField("Имя", max_length=30)
    lastname = models.CharField("Фамилия", max_length=50)
    phonenumber = PhoneNumberField("Номер телефона", max_length=32)
    comment = models.TextField("Комментарий к заказу", blank=True, default="")
    address = models.TextField("Адрес доставки")
    user = model.ForeignKey(
        "Пользователь", settings.AUTH_USER_MODEL, on_delete
    )
    status = models.CharField(
        "Статус заказа", max_length=255, choices=STATUSES, default="draft"
    )
    total_price = models.DecimalField(
        "Общая сумма", decimal_places=2, max_digits=10
    )
    shipping_price = models.DecimalField(
        "Сумма доставки", decimal_places=2, max_digits=10
    )
    delivered_at = models.DateTimeField("Дата доставки", null=True, blank=True)
    refunded_at = models.DateTimeField("Дата возврата", null=True, blank=True)
    handled_at = models.DateTimeField("Дата обработки", null=True, blank=True)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Заказ", Order, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        "Продукт",
        Product,
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    quantity = models.IntegerField("Количество", default=1)
    item_price = models.DecimalField(
        "Сумма заказа", decimal_places=2, max_digits=10
    )

    class Meta:
        unique_together = ["order", "product"]

    def total_price(self):
        return self.item_price * self.quantity
