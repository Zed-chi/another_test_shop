from django.db import models

# Create your models here.
class Order(models.Model):
    STATUSES = (
        (
            "created",
            "created",
        ),
        ("paid", "paid"),
        ("shipped", "shipped"),
        ("refunding", "refunding"),
        ("refunded", "refunded"),
    )
    address = models.TextField()
    shop_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=255, choices=STATUSES, default="created"
    )
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    shipping_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.id)
