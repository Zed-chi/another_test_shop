from django.db import models
from django.conf import settings
from cart.models import Cart


class Order(models.Model):
    STATUSES = (
        (
            "draft",
            "draft",
        ),
        ("paid", "paid"),
        ("shipped", "shipped"),
        ("delivered", "delivered"),
        ("refunding", "refunding"),
        ("refunded", "refunded"),
    )
    address = models.TextField()
    user = model.ForeignKey(settings.AUTH_USER_MODEL, on_delete)
    status = models.CharField(max_length=255, choices=STATUSES, default="draft")
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    shipping_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    quantity = models.IntegerField(default=1)
    item_price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        unique_together = ["order", "product"]

    def total_price(self):
        return self.item_price * self.quantity
