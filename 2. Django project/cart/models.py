from django.db import models
from django.conf import settings

from products.models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Пользователь",
    )

    def flush(self):
        try:
            items = self.items.all()
            for i in items:
                i.delete()
        except:
            pass

    def get_total_price(self):
        items = self.items.all()
        return sum([i.total_price() for i in items])


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Корзина",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name="Продукт",
    )
    quantity = models.IntegerField("Количество", default=1)
    item_price = models.DecimalField(
        "Цена позиции", decimal_places=2, max_digits=10
    )

    class Meta:
        unique_together = ["cart", "product"]

    def total_price(self):
        return self.product.price * self.quantity
